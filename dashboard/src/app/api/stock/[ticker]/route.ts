import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

export async function GET(
  request: Request,
  { params }: { params: Promise<{ ticker: string }> }
) {
  const resolvedParams = await params;
  const ticker = resolvedParams.ticker.toUpperCase();
  console.log(`[API] Fetching data for ticker: ${ticker}`);
  const projectRoot = path.join(process.cwd(), '..');

  try {
    // 1. Fetch Thesis
    const thesisPath = path.join(projectRoot, 'portfolio', 'investment_thesis.md');
    const thesisContent = await fs.readFile(thesisPath, 'utf-8');
    
    const sections = thesisContent.split(/###/);
    const thesisSection = sections.find(section => {
      const firstLine = section.split('\n')[0];
      return firstLine.toUpperCase().includes(`(${ticker})`);
    })?.trim() || "No specific thesis found.";

    // 2. Fetch Briefs & Parse Sections
    const briefPath = path.join(projectRoot, 'briefs', `${ticker}.md`);
    let brief = "No detailed brief available yet.";
    let moat = "";
    let financial = "";
    let sentiment = "";
    let segments = "";
    
    try {
      const briefContent = await fs.readFile(briefPath, 'utf-8');
      brief = briefContent;
      
      const briefSections = briefContent.split(/## /);
      moat = briefSections.find(s => s.includes("Competitive Moat")) || "";
      financial = briefSections.find(s => s.includes("Financial Health")) || "";
      sentiment = briefSections.find(s => s.includes("Market Buzz")) || "";
      segments = briefSections.find(s => s.includes("Strategy Alignment") || s.includes("Segment")) || "";
    } catch { 
      console.log(`[API] No brief found for ${ticker}`);
    }

    // 3. Check for source files
    const sourceDir = path.join(projectRoot, 'sources', ticker);
    let sourceFiles: string[] = [];
    try {
      sourceFiles = await fs.readdir(sourceDir);
    } catch { 
      // Directory may not exist
    }

    const responseData = {
      ticker,
      thesis: thesisSection,
      brief,
      moat: moat.trim(),
      financial: financial.trim(),
      sentiment: sentiment.trim(),
      segments: segments.trim(),
      sourcesCount: sourceFiles.length,
      sourceFiles: sourceFiles,
      lastUpdated: new Date().toISOString()
    };

    return NextResponse.json(responseData);
  } catch (error) {
    console.error(`[API ERROR] for ${ticker}:`, error);
    return NextResponse.json({ error: 'Failed to fetch stock data', details: String(error) }, { status: 500 });
  }
}
