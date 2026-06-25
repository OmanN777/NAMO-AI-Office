import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

export async function GET() {
  const filePath = path.join(process.cwd(), '..', 'Portfolios', 'Namo_History', 'my_portfolio.json');

  try {
    const content = await fs.readFile(filePath, 'utf-8');
    const data = JSON.parse(content);
    return NextResponse.json(data);

  } catch (error) {
    console.error('Error reading real portfolio:', error);
    return NextResponse.json({ error: 'Failed to fetch real portfolio data' }, { status: 500 });
  }
}

export async function POST(request: Request) {
  const filePath = path.join(process.cwd(), '..', 'Portfolios', 'Namo_History', 'my_portfolio.json');

  try {
    const body = await request.json();
    const content = await fs.readFile(filePath, 'utf-8');
    const data = JSON.parse(content);

    if (body.action === 'SYNC') {
      const { holdings: syncedHoldings } = body;
      if (!Array.isArray(syncedHoldings)) {
        return NextResponse.json({ error: 'Invalid payload. Expected "holdings" array.' }, { status: 400 });
      }

      const activeHoldings = syncedHoldings.filter((h: any) => {
        const shares = parseFloat(h.shares);
        return !isNaN(shares) && shares > 0;
      });

      const existingCategories = data.holdings.reduce((acc: any, h: any) => {
        acc[h.ticker] = h.category || "Unknown";
        return acc;
      }, {});

      const existingRealizedPl = data.holdings.reduce((acc: any, h: any) => {
        acc[h.ticker] = h.realized_pl || 0;
        return acc;
      }, {});

      let priceMap: any = {};
      try {
        const omanPath = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');
        const omanContent = await fs.readFile(omanPath, 'utf-8');
        const omanData = JSON.parse(omanContent);
        omanData.holdings.forEach((s: any) => {
          priceMap[s.ticker.toUpperCase()] = s.current_price;
        });
      } catch (e) {
        console.error("Failed to read oman holdings for sync pricing", e);
      }

      data.holdings = activeHoldings.map((h: any) => {
        const shares = parseFloat(h.shares);
        const avgCost = parseFloat(h.average_cost);
        const ticker = (h.ticker || "").toUpperCase();
        
        let currentPrice = parseFloat(h.current_price);
        if (priceMap[ticker] !== undefined) {
           currentPrice = priceMap[ticker];
        }

        const costBasis = shares * avgCost;
        const totalVal = shares * currentPrice;

        return {
          ticker,
          shares,
          average_cost: avgCost,
          current_price: currentPrice,
          total_value: totalVal,
          pl_usd: totalVal - costBasis,
          pl_pct: costBasis > 0 ? ((totalVal - costBasis) / costBasis) * 100 : 0,
          category: existingCategories[ticker] || "Unknown",
          allocation_pct: 0, 
          days_held: h.days_held || 0,
          realized_pl: existingRealizedPl[ticker] || 0,
          dividends: h.dividends || 0,
          trades_count: h.trades_count || 1
        };
      });

      let totalValue = 0;
      let totalCost = 0;

      data.holdings.forEach((h: any) => {
        totalValue += h.total_value;
        totalCost += h.shares * h.average_cost;
      });

      data.holdings.forEach((h: any) => {
        h.allocation_pct = totalValue > 0 ? (h.total_value / totalValue) * 100 : 0;
      });

      data.total_value = totalValue;
      data.total_cost = totalCost;
      data.total_pl = totalValue - totalCost;
      data.pl_percentage = totalCost > 0 ? (data.total_pl / totalCost) * 100 : 0;
      data.current_nav = totalValue + (data.cash_balance || 0);

      await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');
      return NextResponse.json({ success: true, portfolio: data });
    }

    // Legacy BUY / SELL logic
    const { ticker, action, shares, price } = body;

    if (!ticker || !action || !shares || !price) {
      return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
    }

    const tickerUpper = ticker.toUpperCase();
    const parsedShares = parseFloat(shares);
    const parsedPrice = parseFloat(price);

    if (isNaN(parsedShares) || isNaN(parsedPrice) || parsedShares <= 0 || parsedPrice <= 0) {
       return NextResponse.json({ error: 'Invalid shares or price' }, { status: 400 });
    }

    let holding = data.holdings.find((h: any) => h.ticker === tickerUpper);

    if (!holding) {
      if (action === 'SELL') {
        return NextResponse.json({ error: 'Cannot sell a stock you do not own' }, { status: 400 });
      }
      holding = {
        ticker: tickerUpper,
        shares: 0,
        average_cost: 0,
        current_price: parsedPrice,
        total_value: 0,
        pl_usd: 0,
        pl_pct: 0,
        category: "Unknown",
        allocation_pct: 0,
        days_held: 0,
        realized_pl: 0,
        dividends: 0,
        trades_count: 0
      };
      data.holdings.push(holding);
    }

    holding.current_price = parsedPrice;

    if (action === 'BUY') {
      const oldTotalCost = holding.shares * holding.average_cost;
      const newCost = parsedShares * parsedPrice;
      holding.shares += parsedShares;
      holding.average_cost = (oldTotalCost + newCost) / holding.shares;
      holding.trades_count += 1;
    } else if (action === 'SELL') {
      if (parsedShares > holding.shares) {
         return NextResponse.json({ error: 'Not enough shares to sell' }, { status: 400 });
      }
      holding.shares -= parsedShares;
      holding.trades_count += 1;
      const realized = (parsedPrice - holding.average_cost) * parsedShares;
      holding.realized_pl = (holding.realized_pl || 0) + realized;
      data.realized_pl_total = (data.realized_pl_total || 0) + realized;
      
      if (holding.shares < 0.0001) { 
         holding.shares = 0;
         holding.total_value = 0;
      }
    }

    let totalValue = 0;
    let totalCost = 0;

    data.holdings.forEach((h: any) => {
      h.total_value = h.shares * h.current_price;
      const costBasis = h.shares * h.average_cost;
      h.pl_usd = h.total_value - costBasis;
      h.pl_pct = costBasis > 0 ? (h.pl_usd / costBasis) * 100 : 0;
      
      totalValue += h.total_value;
      totalCost += costBasis;
    });

    data.holdings.forEach((h: any) => {
      h.allocation_pct = totalValue > 0 ? (h.total_value / totalValue) * 100 : 0;
    });

    data.holdings = data.holdings.filter((h: any) => h.shares > 0);

    data.total_value = totalValue;
    data.total_cost = totalCost;
    data.total_pl = totalValue - totalCost;
    data.pl_percentage = totalCost > 0 ? (data.total_pl / totalCost) * 100 : 0;
    data.current_nav = totalValue + (data.cash_balance || 0);

    await fs.writeFile(filePath, JSON.stringify(data, null, 2), 'utf-8');

    return NextResponse.json({ success: true, portfolio: data });

  } catch (error) {
    console.error('Error updating real portfolio:', error);
    return NextResponse.json({ error: 'Failed to update real portfolio' }, { status: 500 });
  }
}
