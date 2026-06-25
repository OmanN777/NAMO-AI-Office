import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

export async function GET() {
  try {
    const historyDir = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'history');
    const files = await fs.readdir(historyDir);
    
    // Extract dates from history files (e.g., '2026-05-17.json' -> '2026-05-17')
    const historyDates = files
      .filter(file => file.endsWith('.json'))
      .map(file => file.replace('.json', ''));

    // Also get the current 'LIVE' date from holdings.json
    const holdingsPath = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');
    let liveDate = null;
    try {
      const holdingsContent = await fs.readFile(holdingsPath, 'utf-8');
      const holdingsData = JSON.parse(holdingsContent);
      if (holdingsData.last_updated) {
        liveDate = holdingsData.last_updated;
      }
    } catch (e) {
      console.warn("Could not read holdings.json for live date");
    }

    // Combine and sort dates
    const allDates = new Set([...historyDates]);
    if (liveDate) {
      allDates.add(liveDate);
    }

    const sortedDates = Array.from(allDates).sort((a, b) => a.localeCompare(b));
    
    return NextResponse.json({ dates: sortedDates, liveDate });
  } catch (error) {
    console.error('Error fetching dates:', error);
    return NextResponse.json({ error: 'Failed to fetch dates' }, { status: 500 });
  }
}
