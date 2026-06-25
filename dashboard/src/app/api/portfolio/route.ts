import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic';

const PORTFOLIO_FILE = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const date = searchParams.get('date');
  
  let filePath = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');
  
  if (date) {
    const historyPath = path.join(process.cwd(), '..', 'Portfolios', 'Oman_Mock_Portfolio', 'history', `${date}.json`);
    try {
      await fs.access(historyPath);
      filePath = historyPath;
    } catch {
      // History file not found, fall back to current holdings.json
    }
  }

  try {
    const content = await fs.readFile(filePath, 'utf-8');
    const data = JSON.parse(content);
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error reading portfolio:', error);
    return NextResponse.json({ error: 'Failed to fetch portfolio data' }, { status: 500 });
  }
}
