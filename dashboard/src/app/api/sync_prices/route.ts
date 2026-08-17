import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export const dynamic = 'force-dynamic';

export async function POST() {
  const projectRoot = path.join(process.cwd(), '..');
  const pythonPath = 'C:\\Users\\namo_\\AppData\\Local\\Programs\\Python\\Python312\\python.exe';
  const realScript = path.join(projectRoot, 'Scripts', 'update_live_prices.py');
  const omanScript = path.join(projectRoot, 'Scripts', 'update_oman_prices.py');

  try {
    // Run both price update scripts
    await Promise.allSettled([
      execAsync(`"${pythonPath}" "${realScript}"`),
      execAsync(`"${pythonPath}" "${omanScript}"`)
    ]);

    // Read updated real portfolio
    const realPath = path.join(projectRoot, 'Portfolios', 'Namo_History', 'my_portfolio.json');
    const realContent = await fs.readFile(realPath, 'utf-8');
    const realData = JSON.parse(realContent);

    // Read updated oman portfolio
    const omanPath = path.join(projectRoot, 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');
    const omanContent = await fs.readFile(omanPath, 'utf-8');
    const omanData = JSON.parse(omanContent);

    return NextResponse.json({
      success: true,
      message: 'Prices updated successfully!',
      realPortfolio: realData,
      omanPortfolio: omanData
    });
  } catch (error: any) {
    console.error('Error during price sync:', error);
    return NextResponse.json({
      success: false,
      error: error?.message || 'Failed to sync live prices'
    }, { status: 500 });
  }
}
