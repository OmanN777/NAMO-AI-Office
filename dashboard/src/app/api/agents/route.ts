import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

const AGENTS_DIR = path.join(process.cwd(), '..', '..', '.gemini', 'agents');

export async function GET() {
  try {
    const files = await fs.readdir(AGENTS_DIR);
    const agents = await Promise.all(
      files
        .filter((file) => file.endsWith('.md'))
        .map(async (file) => {
          const content = await fs.readFile(path.join(AGENTS_DIR, file), 'utf-8');
          const id = file.replace('.md', '');
          
          // Basic parser for persona and commands
          const nameMatch = content.match(/# Agent: (.*)/);
          const personaMatch = content.match(/\*\*Persona:\*\* (.*)/);
          const descriptionMatch = content.match(/description: (.*)/);
          
          return {
            id,
            name: nameMatch ? nameMatch[1] : id,
            description: descriptionMatch ? descriptionMatch[1] : '',
            persona: personaMatch ? personaMatch[1] : '',
            content
          };
        })
    );
    return NextResponse.json(agents);
  } catch (error) {
    console.error('Error reading agents:', error);
    return NextResponse.json({ error: 'Failed to fetch agents' }, { status: 500 });
  }
}
