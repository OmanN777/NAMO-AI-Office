const fs = require('fs');
const path = require('path');

const briefsDir = path.join(__dirname, '..', 'Knowledge_Base', 'Briefs');
const files = fs.readdirSync(briefsDir).filter(f => f.endsWith('.md'));

let missingCount = 0;

files.forEach(file => {
  const content = fs.readFileSync(path.join(briefsDir, file), 'utf-8');
  const sections = content.split(/## /);
  
  const hasMoat = sections.some(s => s.toLowerCase().includes("moat") || s.toLowerCase().includes("overview"));
  const hasFinancial = sections.some(s => s.toLowerCase().includes("financial") || s.toLowerCase().includes("earnings") || s.toLowerCase().includes("insight"));
  const hasSentiment = sections.some(s => s.toLowerCase().includes("sentiment") || s.toLowerCase().includes("risk") || s.toLowerCase().includes("buzz"));
  const hasSegments = sections.some(s => s.toLowerCase().includes("segment") || s.toLowerCase().includes("strategy") || s.toLowerCase().includes("conclusion"));
  
  const missing = [];
  if (!hasMoat) missing.push("Moat");
  if (!hasFinancial) missing.push("Financial");
  if (!hasSentiment) missing.push("Sentiment");
  if (!hasSegments) missing.push("Segments");
  
  if (missing.length > 0) {
    console.log(`${file} is missing: ${missing.join(', ')}`);
    missingCount++;
  }
});

console.log(`\nTotal briefs needing updates: ${missingCount} / ${files.length}`);
