import json
import re
from collections import defaultdict

log_file = r"C:\Users\namo_\.gemini\antigravity-cli\brain\686e8484-0310-4ad6-ab39-93cdd3121ae3\.system_generated\logs\transcript.jsonl"
agent_counts = defaultdict(int)
total = 0

with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        if "TypeName" in line and "invoke_subagent" in line:
            # find all "TypeName":"AgentName"
            matches = re.findall(r'"TypeName":"([^"]+)"', line)
            for m in matches:
                agent_counts[m] += 1
                total += 1

if total == 0:
    print("No agents invoked yet.")
else:
    for agent, count in sorted(agent_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total) * 100
        print(f"{agent}: {pct:.2f}% ({count} calls)")
