import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

const UNIVERSE_FILE = path.join(process.cwd(), '..', 'portfolio', 'universe.json');

export async function GET() {
  try {
    const content = await fs.readFile(UNIVERSE_FILE, 'utf-8');
    const data = JSON.parse(content);
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error reading universe:', error);
    return NextResponse.json({ items: [] });
  }
}
