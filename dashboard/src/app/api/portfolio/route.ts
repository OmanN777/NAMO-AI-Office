import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

const PORTFOLIO_FILE = path.join(process.cwd(), '..', 'portfolio', 'holdings.json');

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const date = searchParams.get('date');
  
  let filePath = path.join(process.cwd(), '..', 'portfolio', 'holdings.json');
  
  if (date && date !== '2026-05-19') {
    filePath = path.join(process.cwd(), '..', 'portfolio', 'history', `${date}.json`);
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
