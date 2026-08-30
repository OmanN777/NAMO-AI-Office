import os
import sys
import json
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Multi-Channel Discord Webhook Router
DISCORD_WEBHOOKS = {
    'daily': 'https://discord.com/api/webhooks/1543334492457009322/zVCTRfqTGGdtZWWXpb3MidxAm7KRQ6FRZQNko3Ea4v5GrlcrFMZfLh2MQSVtd_ZMHHFZ',      # Mallicord (General & Daily Briefing)
    'stocks': 'https://discord.com/api/webhooks/1543334926815072326/TaOsBJqdMlgVPfYO7YmEVZMmnxxIK00yn7GuZRpfzXV_-lby-RJlzv7CLZchmGzI6Zvg',     # Mallitock (Oman, Fundamentokung, Vera, Newwy)
    'qa': 'https://discord.com/api/webhooks/1543335045694095400/2ZKXSPnx4c8QSTHDBetJbTkpqhD2l3VJllbQKKS9A76BKCcrlGCBh5mfTytXHu8oIZNh',         # Malliqa (QA Automation, Job Alerts, Tests)
    'youtube': 'https://discord.com/api/webhooks/1543335115613147276/l0A0ovCq4NMDnEi26ocnLsRT2IHNSzxBY5KIaMm9wFA_jui1j2LPzhLTQ4xUoLVKbFeh'     # Mallitube (Tubemaster, CapCut, Shorts Ideas)
}

def send_to_channel(channel='daily', content=None, embeds=None, username=None, avatar_url=None):
    """
    Sends message/embeds to a specific Discord channel ('daily', 'stocks', 'qa', 'youtube').
    """
    webhook_url = DISCORD_WEBHOOKS.get(channel, DISCORD_WEBHOOKS['daily'])
    payload = {}
    if username:
        payload['username'] = username
    if avatar_url:
        payload['avatar_url'] = avatar_url
    if content:
        payload['content'] = content
    if embeds:
        payload['embeds'] = embeds if isinstance(embeds, list) else [embeds]
        
    try:
        resp = requests.post(webhook_url, json=payload, timeout=10)
        return resp.status_code in [200, 204]
    except Exception as e:
        print(f'Error sending to Discord [{channel}]: {e}', file=sys.stderr)
        return False

def broadcast_all_greeting():
    """
    Sends greeting and initial status to all 4 channels.
    """
    # 1. Mallicord (Daily HQ)
    send_to_channel(
        channel='daily',
        username='Malli (Chief Secretary)',
        embeds=[{
            'title': '🌸 Mallicord (Daily HQ) Connected!',
            'description': 'ช่องทางหลักสำหรับรายงานสรุปประจำวัน **`/malli-daily`** และภารกิจสำคัญของบอสค่ะ',
            'color': 0xFF69B4,
            'footer': {'text': 'Executive Office • Mallicord'}
        }]
    )
    
    # 2. Mallitock (Stock & Investment)
    send_to_channel(
        channel='stocks',
        username='Agent Oman (CIO)',
        embeds=[{
            'title': '📈 Mallitock (Investment Radar) Online!',
            'description': 'ศูนย์บัญชาการพอร์ตการลงทุนและเฝ้าระวัง **Master Universe 25 ตัว** พร้อมรายงานงบ 10-K และสัญญาณ Insider Trading จาก SEC EDGAR ครับ',
            'color': 0x2ECC71,
            'footer': {'text': 'Financial Division • Mallitock'}
        }]
    )
    
    # 3. Malliqa (QA & Career)
    send_to_channel(
        channel='qa',
        username='Malli (QA Specialist)',
        embeds=[{
            'title': '💼 Malliqa (QA & Career Radar) Online!',
            'description': 'แจ้งเตือนงานไอที/QA Automation รอบใหม่จากบริษัทชั้นนำ พร้อมรายงานผลการรัน Test Automation Suite ค่ะ',
            'color': 0x3498DB,
            'footer': {'text': 'Career & QA Engineering • Malliqa'}
        }]
    )
    
    # 4. Mallitube (YouTube Gaming)
    send_to_channel(
        channel='youtube',
        username='Tubemaster (Viral Director)',
        embeds=[{
            'title': '🎬 Mallitube (YouTube Pipeline) Ready!',
            'description': 'ศูนย์รวมไอเดียคลิปสั้น Gaming Shorts, สคริปต์วิดีโอ, และการตัดต่ออัตโนมัติผ่าน CapCut MCP Server ครับ',
            'color': 0xE74C3C,
            'footer': {'text': 'Content Division • Mallitube'}
        }]
    )

if __name__ == '__main__':
    print('Broadcasting greeting to all 4 Discord channels...')
    broadcast_all_greeting()
    print('Finished dispatching to all 4 webhooks successfully!')
