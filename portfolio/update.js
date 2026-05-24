const fs = require('fs');
const path = require('path');

const portfolioPath = path.join(__dirname, 'holdings.json');
const historyPath = path.join(__dirname, 'history', '2026-05-21.json');

const newPrices = {
  'VRT': 315.67,
  'AVGO': 417.49,
  'CRM': 180.10,
  'GOOGL': 388.91,
  'CCJ': 103.50
};

try {
  let data = JSON.parse(fs.readFileSync(portfolioPath, 'utf-8'));
  let totalHoldingsValue = 0;

  for (let holding of data.holdings) {
    if (newPrices[holding.ticker]) {
      const price = newPrices[holding.ticker];
      holding.total_value = parseFloat((holding.shares * price).toFixed(2));
    }
    totalHoldingsValue += holding.total_value;
  }

  const newNav = totalHoldingsValue + data.cash_balance;
  data.current_nav = parseFloat(newNav.toFixed(2));

  // Update allocation percentages
  for (let holding of data.holdings) {
    holding.allocation_pct = parseFloat(((holding.total_value / data.current_nav) * 100).toFixed(2));
  }

  // Update performance history
  const omanReturn = parseFloat((((newNav - data.initial_nav) / data.initial_nav) * 100).toFixed(2));
  
  const historyEntry = data.performance_history.find(h => h.date === '2026-05-21');
  if (historyEntry) {
    historyEntry.oman_return = omanReturn;
  }

  fs.writeFileSync(portfolioPath, JSON.stringify(data, null, 2));
  fs.writeFileSync(historyPath, JSON.stringify(data, null, 2));
  
  console.log('Successfully updated prices. New NAV:', newNav);
} catch (e) {
  console.error('Error updating prices:', e);
}
