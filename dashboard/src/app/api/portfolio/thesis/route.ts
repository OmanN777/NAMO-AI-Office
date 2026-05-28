import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

const THESIS_FILE = path.join(process.cwd(), '..', 'portfolio', 'investment_thesis.md');

export async function GET() {
  try {
    const content = await fs.readFile(THESIS_FILE, 'utf-8');
    return NextResponse.json({ content });
  } catch (error) {
    console.error('Error reading thesis:', error);
    return NextResponse.json({ error: 'Failed to fetch thesis' }, { status: 500 });
  }
}
