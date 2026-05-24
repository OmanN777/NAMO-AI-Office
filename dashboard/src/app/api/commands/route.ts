import { promises as fs } from 'fs';
import path from 'path';
import { NextResponse } from 'next/server';

const COMMANDS_DIR = path.join(process.cwd(), '..', '..', '.gemini', 'commands');

export async function GET() {
  try {
    const files = await fs.readdir(COMMANDS_DIR);
    const commands = await Promise.all(
      files
        .filter((file) => file.endsWith('.md'))
        .map(async (file) => {
          const content = await fs.readFile(path.join(COMMANDS_DIR, file), 'utf-8');
          const id = file.replace('.md', '');
          
          // Match either "# Description: text" or "description: text"
          const descriptionMatch = content.match(/# Description:\s*(.*)/) || content.match(/description:\s*(.*)/);
          
          return {
            id,
            name: `/${id}`,
            description: descriptionMatch ? descriptionMatch[1].trim() : '',
          };
        })
    );
    return NextResponse.json(commands);
  } catch (error) {
    console.error('Error reading commands:', error);
    return NextResponse.json([], { status: 200 }); // Return empty array if dir doesn't exist
  }
}
