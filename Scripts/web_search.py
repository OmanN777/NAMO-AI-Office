import sys
import urllib.request
import urllib.parse
import re
import json
import html

def clean_html(text):
    text = re.sub(r'<[^>]+>', '', text)
    return html.unescape(text).strip()

def search(query):
    # Fetch DuckDuckGo Lite search results using POST to avoid challenges
    url = "https://lite.duckduckgo.com/lite/"
    data = urllib.parse.urlencode({"q": query}).encode('utf-8')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            page_content = response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return {"error": f"Failed to fetch search results: {e}"}
        
    results = []
    # Pattern to match link and snippet sequentially in DDG Lite HTML
    pattern = r"<a rel=\"nofollow\" href=\"(?P<url>[^\"]+)\" class='result-link'>(?P<title>.*?)</a>.*?<td class='result-snippet'>(?P<snippet>.*?)</td>"
    matches = re.finditer(pattern, page_content, re.DOTALL)
    
    for m in matches:
        url = m.group('url')
        # Clean redirect proxy if exists
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
        
    return {"results": results[:5]}  # Limit to top 5 results for token efficiency

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    if len(sys.argv) < 2:
        print(json.dumps({"error": "Query is required"}))
        return
        
    query = sys.argv[1]
    res = search(query)
    print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
