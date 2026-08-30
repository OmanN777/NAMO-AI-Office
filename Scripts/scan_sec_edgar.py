import os
import sys
import json
import urllib.request
import xml.etree.ElementTree as ET

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {'User-Agent': 'NamoInvestmentAgent namo.nanon5@gmail.com'}
FEED_URL = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4&owner=only&count=40&output=atom'

def fetch_insider_trades():
    print('Scanning SEC EDGAR for latest Form 4 (Insider Trading) filings...')
    try:
        req = urllib.request.Request(FEED_URL, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            root = ET.fromstring(resp.read())
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')
            print(f'Found {len(entries)} recent filings.')
            results = []
            for e in entries:
                title = e.find('{http://www.w3.org/2005/Atom}title').text
                link = e.find('{http://www.w3.org/2005/Atom}link').attrib.get('href', '')
                updated = e.find('{http://www.w3.org/2005/Atom}updated').text
                summary_elem = e.find('{http://www.w3.org/2005/Atom}summary')
                summary = summary_elem.text if summary_elem is not None else ''
                results.append({'title': title, 'link': link, 'date': updated, 'summary': summary})
            return results
    except Exception as e:
        print(f'Error fetching SEC EDGAR: {e}', file=sys.stderr)
        return []

if __name__ == '__main__':
    filings = fetch_insider_trades()
    for f in filings[:5]:
        print(f['date'], '-', f['title'])
