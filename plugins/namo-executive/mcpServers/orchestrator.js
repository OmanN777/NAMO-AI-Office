const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const workspaceDir = 'C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace';
const memoryManagerPath = path.join(workspaceDir, 'Knowledge_Base', 'Memory', 'memory_manager.py');

// Buffer for incoming stdin chunks
let buffer = '';
process.stdin.on('data', chunk => {
  buffer += chunk.toString();
  let lineEnd;
  while ((lineEnd = buffer.indexOf('\n')) !== -1) {
    const line = buffer.slice(0, lineEnd).trim();
    buffer = buffer.slice(lineEnd + 1);
    if (line) {
      handleMessage(line);
    }
  }
});

function handleMessage(line) {
  try {
    const request = JSON.parse(line);
    if (request.method === 'initialize') {
      sendResponse(request.id, {
        protocolVersion: '2024-11-05',
        capabilities: {
          tools: {}
        },
        serverInfo: {
          name: 'namo-orchestrator',
          version: '1.0.0'
        }
      });
    } else if (request.method === 'tools/list') {
      sendResponse(request.id, {
        tools: [
          {
            name: 'update_portfolio_prices',
            description: 'Fetch latest stock prices using Yahoo Finance and update both portfolios (Oman mock and Namo real).',
            inputSchema: {
              type: 'object',
              properties: {
                target: {
                  type: 'string',
                  enum: ['both', 'oman', 'real'],
                  description: 'Which portfolio to update'
                }
              },
              required: ['target']
            }
          },
          {
            name: 'get_portfolio_status',
            description: 'Get a summary of the latest NAV, daily change, and holdings for both portfolios.',
            inputSchema: {
              type: 'object',
              properties: {}
            }
          },
          {
            name: 'run_qa_tests',
            description: 'Run the Playwright test suite in the QA portfolio and return the status and the AI analysis report.',
            inputSchema: {
              type: 'object',
              properties: {}
            }
          },
          {
            name: 'save_agent_memory',
            description: 'Store or update a persistent fact or reference in the SQLite memory bank. Perfect for remembering user preferences, rules, or decisions across CLI sessions.',
            inputSchema: {
              type: 'object',
              properties: {
                category: {
                  type: 'string',
                  description: 'Category of the memory (e.g., Rules, UserProfile, PortfolioDetails)'
                },
                key: {
                  type: 'string',
                  description: 'Key identifier for the memory'
                },
                value: {
                  type: 'string',
                  description: 'The exact fact or memory content to save'
                }
              },
              required: ['category', 'key', 'value']
            }
          },
          {
            name: 'get_agent_memory',
            description: 'Retrieve a specific persistent memory from the SQLite memory bank by its category and key.',
            inputSchema: {
              type: 'object',
              properties: {
                category: {
                  type: 'string',
                  description: 'Category of the memory'
                },
                key: {
                  type: 'string',
                  description: 'Key identifier for the memory'
                }
              },
              required: ['category', 'key']
            }
          },
          {
            name: 'search_agent_memories',
            description: 'Search the SQLite memory bank for any persistent facts or memories matching a keyword.',
            inputSchema: {
              type: 'object',
              properties: {
                keyword: {
                  type: 'string',
                  description: 'Keyword search query'
                }
              },
              required: ['keyword']
            }
          },
          {
            name: 'get_market_data',
            description: 'Fetch historical prices, company news, or business profile for a stock using the OpenBB SDK.',
            inputSchema: {
              type: 'object',
              properties: {
                command: {
                  type: 'string',
                  enum: ['price', 'news', 'profile'],
                  description: 'The type of data to fetch'
                },
                ticker: {
                  type: 'string',
                  description: 'The stock ticker symbol (e.g., PLTR, AAPL)'
                }
              },
              required: ['command', 'ticker']
            }
          },
          {
            name: 'control_spotify',
            description: 'Control your Spotify music playback (status, play, pause, next, previous, volume). Note: requires active Spotify client running.',
            inputSchema: {
              type: 'object',
              properties: {
                command: {
                  type: 'string',
                  enum: ['status', 'play', 'pause', 'next', 'previous', 'volume'],
                  description: 'The playback control command to execute'
                },
                volume: {
                  type: 'integer',
                  minimum: 0,
                  maximum: 100,
                  description: 'Volume level percent (only required for command="volume")'
                }
              },
              required: ['command']
            }
          },
          {
            name: 'web_search',
            description: 'Search the web using DuckDuckGo Lite to get real-time news, articles, and research (grounding).',
            inputSchema: {
              type: 'object',
              properties: {
                query: {
                  type: 'string',
                  description: 'The search query string'
                }
              },
              required: ['query']
            }
          }
        ]
      });
    } else if (request.method === 'tools/call') {
      handleToolCall(request.id, request.params.name, request.params.arguments || {});
    } else {
      if (request.id !== undefined) {
        sendError(request.id, -32601, 'Method not found');
      }
    }
  } catch (e) {
    // Ignore invalid JSON-RPC lines
  }
}

function handleToolCall(id, toolName, args) {
  if (toolName === 'update_portfolio_prices') {
    const target = args.target || 'both';
    let commands = [];
    if (target === 'oman' || target === 'both') {
      commands.push(`python "${path.join(workspaceDir, 'Scripts', 'update_oman_prices.py')}"`);
    }
    if (target === 'real' || target === 'both') {
      commands.push(`python "${path.join(workspaceDir, 'Scripts', 'update_live_prices.py')}"`);
    }

    const command = commands.join(' && ');
    exec(command, { cwd: workspaceDir }, (err, stdout, stderr) => {
      let outputText = `Execution completed.\nStdout:\n${stdout}\n`;
      if (stderr) {
        outputText += `Stderr:\n${stderr}\n`;
      }
      sendResponse(id, {
        content: [{ type: 'text', text: outputText }],
        isError: !!err
      });
    });

  } else if (toolName === 'get_portfolio_status') {
    try {
      const omanPath = path.join(workspaceDir, 'Portfolios', 'Oman_Mock_Portfolio', 'holdings.json');
      const realPath = path.join(workspaceDir, 'Portfolios', 'Namo_History', 'my_portfolio.json');

      let omanSummary = 'Oman Mock Portfolio: Data not available';
      let realSummary = 'Namo Real Portfolio: Data not available';

      if (fs.existsSync(omanPath)) {
        const d = JSON.parse(fs.readFileSync(omanPath, 'utf-8'));
        omanSummary = `📈 Oman Mock Portfolio (NAV: $${d.current_nav.toLocaleString()}, Daily Change: $${d.daily_change_usd} (${d.daily_change_pct}%))\n` +
          `   Holdings: ${d.holdings.map(h => `${h.ticker} (${h.shares} shares @ $${h.current_price}, allocation: ${h.allocation_pct}%)`).join(', ')}`;
      }

      if (fs.existsSync(realPath)) {
        const d = JSON.parse(fs.readFileSync(realPath, 'utf-8'));
        realSummary = `👑 Namo Real Portfolio (NAV: $${d.current_nav.toLocaleString()}, Total P/L: $${d.total_pl} (${d.pl_percentage}%))\n` +
          `   Holdings: ${d.holdings.map(h => `${h.ticker} (${h.shares.toFixed(4)} shares @ $${h.current_price}, allocation: ${h.allocation_pct}%)`).join(', ')}`;
      }

      const report = `# 📊 Portfolios Summary\n\n${omanSummary}\n\n${realSummary}\n`;
      sendResponse(id, {
        content: [{ type: 'text', text: report }]
      });
    } catch (e) {
      sendError(id, -32603, `Failed to summarize portfolios: ${e.message}`);
    }

  } else if (toolName === 'run_qa_tests') {
    const qaPath = path.join(workspaceDir, 'AI_QA_Portfolio');
    exec('npx playwright test', { cwd: qaPath }, (err, stdout, stderr) => {
      let outputText = '';
      if (!err) {
        outputText = `✅ Playwright tests completed successfully!\n\nStdout:\n${stdout}`;
      } else {
        outputText = `🚨 Playwright tests failed.\n\n`;
        const reportPath = path.join(qaPath, 'ai-failure-report.md');
        if (fs.existsSync(reportPath)) {
          const aiReport = fs.readFileSync(reportPath, 'utf-8');
          outputText += `### AI Failure Analysis Report:\n\n${aiReport}`;
        } else {
          outputText += `Error details:\n${stdout}\n${stderr}`;
        }
      }
      sendResponse(id, {
        content: [{ type: 'text', text: outputText }]
      });
    });

  } else if (toolName === 'save_agent_memory') {
    // Shell escape wrapper (simple escaping for command line safety)
    const category = args.category.replace(/"/g, '\\"');
    const key = args.key.replace(/"/g, '\\"');
    const value = args.value.replace(/"/g, '\\"');

    const cmd = `python "${memoryManagerPath}" save "${category}" "${key}" "${value}"`;
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Failed to save memory: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else if (toolName === 'get_agent_memory') {
    const category = args.category.replace(/"/g, '\\"');
    const key = args.key.replace(/"/g, '\\"');

    const cmd = `python "${memoryManagerPath}" get "${category}" "${key}"`;
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Failed to retrieve memory: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else if (toolName === 'search_agent_memories') {
    const keyword = args.keyword.replace(/"/g, '\\"');

    const cmd = `python "${memoryManagerPath}" search "${keyword}"`;
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Failed to search memory bank: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else if (toolName === 'get_market_data') {
    const command = args.command.replace(/"/g, '\\"');
    const ticker = args.ticker.replace(/"/g, '\\"');
    const fetcherPath = path.join(workspaceDir, 'Scripts', 'openbb_fetcher.py');

    const cmd = `python "${fetcherPath}" "${command}" "${ticker}"`;
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Failed to fetch market data via OpenBB: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else if (toolName === 'control_spotify') {
    const command = args.command.replace(/"/g, '\\"');
    const volume = args.volume !== undefined ? String(args.volume).replace(/"/g, '\\"') : '';
    const spotifyScriptPath = path.join(workspaceDir, 'Scripts', 'spotify_controller.py');

    const cmd = `python "${spotifyScriptPath}" "${command}" ${volume}`.trim();
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Spotify control failed: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else if (toolName === 'web_search') {
    const query = args.query.replace(/"/g, '\\"');
    const searchScriptPath = path.join(workspaceDir, 'Scripts', 'web_search.py');

    const cmd = `python "${searchScriptPath}" "${query}"`;
    exec(cmd, (err, stdout, stderr) => {
      if (err) {
        sendError(id, -32603, `Web search failed: ${stderr || err.message}`);
      } else {
        sendResponse(id, {
          content: [{ type: 'text', text: stdout.trim() }]
        });
      }
    });

  } else {
    sendError(id, -32601, 'Tool not found');
  }
}

function sendResponse(id, result) {
  process.stdout.write(JSON.stringify({
    jsonrpc: '2.0',
    id,
    result
  }) + '\n');
}

function sendError(id, code, message) {
  process.stdout.write(JSON.stringify({
    jsonrpc: '2.0',
    id,
    error: { code, message }
  }) + '\n');
}
