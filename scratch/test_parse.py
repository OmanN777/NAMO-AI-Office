import re
import urllib.parse

def clean_html(text):
    text = re.sub(r'<[^>]+>', '', text)
    # Decode HTML entities
    import html
    text = html.unescape(text)
    return text.strip()

with open('scratch/ddg_lite.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"<a rel=\"nofollow\" href=\"(?P<url>[^\"]+)\" class='result-link'>(?P<title>.*?)</a>.*?<td class='result-snippet'>(?P<snippet>.*?)</td>"
matches = re.finditer(pattern, content, re.DOTALL)

results = []
for m in matches:
    url = m.group('url')
    # Clean redirect proxy
    if 'uddg=' in url:
        try:
            parsed = urllib.parse.urlparse(url)
            qs = urllib.parse.parse_qs(parsed.query)
            if 'uddg' in qs:
                url = qs['uddg'][0]
        except Exception:
            pass
            
    title = clean_html(m.group('title'))
    snippet = clean_html(m.group('snippet'))
    
    results.append({
        "title": title,
        "url": url,
        "snippet": snippet
    })

print(f"Found {len(results)} results.")
if results:
    import json
    print(json.dumps(results[:3], indent=2))
