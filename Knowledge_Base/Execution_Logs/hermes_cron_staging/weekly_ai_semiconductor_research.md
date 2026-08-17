# Weekly AI & Semiconductor Research Roundup
## Week of August 7–13, 2026 | Compiled Thursday, August 13, 2026

---

## 1. Key Earnings

### Hyperscaler Q2 2026 Earnings (Reported Late July)

The big four cloud providers all reported together and the narrative shifted decisively: the "AI CapEx without returns" thesis cracked.

| Company | Q2 Revenue | Cloud Growth | CapEx Guidance | Key Takeaway |
|---|---|---|---|---|
| **Microsoft (MSFT)** | Microsoft Cloud $214B annual run rate (+27%) | Azure $100B annual run rate, +43% YoY in June quarter; guided ~45% for Q3 | ~$190B FY2026 | Copilot: 30M+ paid M365 seats, net adds doubled QoQ, revenue accelerated 60% QoQ. Commercial RPO $678B (+84%), 90% of cloud revenue from non-frontier-model customers. |
| **Amazon (AMZN)** | AWS $42.2B (+36.7% YoY, fastest in 18 quarters) | AWS operating income $16.6B, ~39% margin (+650bps YoY ex one-off) | Raised to ~$220B (from ~$200B) | AI + chips each at $25B annual run rate, both growing triple-digit YoY. "AI margins tracking ahead of where core was at same point." Backlog $496B, triple-digit YoY growth. First time market cap crossed $3T. |
| **Alphabet (GOOGL)** | Consolidated $119.8B (+24% YoY) | Google Cloud $24.8B (+82% YoY), operating margin 35.6% (up from 20.7%) | Raised to $195–205B (from $180–190B) | Cloud backlog $514B (+~$50B QoQ); expects >50% recognized as revenue in 24 months. CFO: "dynamics look healthier than a year ago." Q2 CapEx alone $44.9B, ~2x YoY. |
| **Meta (META)** | $60.8B total (+28% YoY) | Family of Apps $60.4B; Instagram 2B daily actics | Raised to $130–145B | CapEx $31.1B in Q2 (~2x YoY). Four new revenue lines emerging: transactional, compute, APIs, subscriptions. Ad AI recommendations driving double-digit time-spent growth. |

** investors' takeaway:** Nobody is guiding CapEx down — but all four now frame it as two-part: land/data centers are long-lived flexible commitments, chips/servers are ordered just-in-time against visible demand. All four walked ROIC math in detail. Amazon explicitly said AI margins are tracking ahead of where "core" was at the same point in its evolution.

### Semiconductor Earnings

**AMD (Q2 2026):** Record revenue ~$11.5B driven by data center AI. MI300 series gaining traction with major cloud providers. Helios platform and MI400 series positioning for sovereign AI. Stock dropped ~7% post-earnings on guidance/volume, creating what some analysts call an attractive entry. PEG ratio ~0.4–0.5, 64% projected EPS growth for 2026 — significantly cheaper than Nvidia on growth-adjusted basis.

**Nvidia (Q2 FY2027 — reports August 26):** Consensus expects another strong quarter. Q2 actuals per AlphaSpread earnings-call summary: record total revenue $46.7B (+98% YoY, +46% sequential), data center dominant, networking record $7.3B (nearly 2x YoY). GB300 platform ramping; Blackwell grew 17% sequentially; Blackwell Ultra generated "tens of billions." Q3 guidance: $54B (±2%), gross margin 73.3%. Returned $10B to shareholders in Q2, authorized additional $60M buyback ($14.7B remaining). Gaming record $4.3B; automotive/Thor SoC shipments. Sovereign AI revenue on track for >$20B this year (2x last year). Jensen Huang framed NVIDIA at ~$35B of every $50B AI factory (per gigawatt). AI market now ~$600B/year just among large hyperscalers.

**Intel:** Turnaround narrative gaining traction — AI-fueled quarter beat estimates. 18A-P and 14A nodes central to foundry strategy. Stock volatile around earnings.

**Micron (MU):** AI-fueled forecast shattered estimates — stock surged. Memory pricing strong, supply tight. Management sees tightness persisting beyond mid-2027 (next capacity comes online then). Consensus estimates for calendar 2026: ~50% revenue growth, ~100% earnings growth. Stock more than tripled in 2026 but well off all-time highs on cyclicality fears. Gross margin 72.6%.

### Networking / Interconnect Semi Stocks Under the Radar

Four names highlighted as AI-cluster scale-up beneficiaries (Yahoo Finance / Zacks, July 23):
- **Broadcom (AVGO):** Networking = ~40% of AI revenue in Q2 vs. 1/3 in Q1. Taping out next-gen 200-terabit switch in FY2026. Custom XPUs for hyperscalers. Zacks Rank #2 (Buy).
- **Marvell (MRVL):** Custom silicon, interconnect, switching, optics driving records. TIAs/drivers expected to exceed $1B annualized run rate. Zacks Rank #3 (Hold).
- **Credo (CRDO):** Revenue surged 157% YoY to $437M in FQ2. EPS $1.16 (+12.6% YoY). Zacks Rank #1 (Strong Buy).
- **Astera Labs (ALAB):** PCIe Gen 6 signal conditioning + AI fabric switching. Gen 6 revenue >1/3 of total in Q1 2026. 2026 EPS consensus +61% YoY.

---

## 2. Policy & Regulatory Moves

### US AI Chip Export Controls — Being Rewritten Again

The US Commerce Department is formalizing a new framework called **"strategic AI accelerator export controls"** — scrapping earlier proposals. Per Reuters and Tom's Hardware (August 2026):

- The new rules target **specific performance thresholds** (interconnect bandwidth, compute density) and end uses rather than broad country-based bans.
- Exports of up to ~1,000 Nvidia GB300 GPUs (or equivalent) would face "fairly simple review" — but only for projects in allied countries, and host countries would need to make "matching" investments in US AI.
- Aim: prevent diversion to restricted destinations through intermediate countries. Procurement timelines for advanced AI hardware exposed to policy shifts until the formal rule lands.
- Earlier March 2026: Commerce withdrew a planned rule, then signaled a tougher replacement. Now the rewrite is in final stages.

### EU AI Act — Full Enforcement Begins August 2, 2026

Per CES Intelligence: The EU AI Act enters full enforcement with penalties up to **€35 million or 7% of global revenue**. Corporate implication: AI chip purchases, model licensing, and cloud architecture decisions now carry export-control, data-residency, and audit obligations that cannot be delegated to vendors. Boards are underestimating the operational burden.

### CHIPS Act — $52.7B Disbursed, Delays Ongoing

Over $52 billion in US incentives committed; execution phase revealed significant delays:
- TSMC Arizona Fab 2: delayed from 2026 to 2027–2028
- Intel Ohio: delayed from 2025 to 2027–2028
- Samsung Taylor, TX: delayed to 2025
- As of August 2024, ~40% of largest CHIPS-funded projects were delayed. Near-term manufacturing dominance remains in Asia.

### 25% Tariff on Advanced AI Chips Imported Into US

Per ML Strategies (Mintz): Acting under a completed Section 232 investigation, the administration imposed a 25% tariff on a limited set of advanced AI chips. Widely viewed as an indirect mechanism to enforce the 25% revenue-share demand from China exports — which could not be imposed directly as an export tax.

### Congressional Action on Nvidia Blackwell Exports

A bill would treat advanced semiconductor exports like weapons sales, prohibiting Blackwell chip sales to foreign entities of concern (China, Iran, North Korea, Russia, Venezuela) for two years — giving US manufacturers time to produce more advanced AI chips domestically.

---

## 3. Structural Analyst Insights

### Foundry War: TSMC Still Undisputed, Samsung Investing Aggressively

- **TSMC:** ~90% share of leading-edge foundry; 3nm lead times now **surpassing one year** (Digitimes, June 25). Considering 10–15% price hikes on 3nm; 2nm wafers projected at ~$30,000 each. Arizona Fab 1 now producing (4nm); Fab 2 delayed to 2027–2028 (2nm + 3nm). Arizona Fab 3 (2nm or more advanced) still in planning.
- **Samsung Foundry:** 4nm production fully booked through next year (August 10, 2026 announcement). Boosting 2nm capacity **163% by 2026**. $460B long-term plan to challenge TSMC. 2nm yields reported ~60% for some chips, ~50% for Exynos 2600 (per SamMobile/Hankyung). South Korea approving 14 trillion won in low-interest loans for chip infrastructure. Yongin mega-cluster: 16 new fabs, 622 trillion won private investment by 2047.
- **Intel Foundry:** 18A-P and 14A nodes central to turnaround. U.S.-based manufacturing with EMIB/Foveros advanced packaging. Still in early stages of winning major external customers; success would meaningfully rebalance industry geography.

### Custom Silicon Trend Accelerating — Long-Term Risk to Merchant Vendors

Industry forecasts: Nvidia's AI accelerator share could slip from ~80% to ~75% by end of 2026 as hyperscalers' custom chips gain ground. Google TPU, Amazon Trainium/Inferentia, Microsoft's reported custom accelerators. TSMC pricing power (10–15% hikes on advanced nodes) is itself accelerating this trend — hyperscalers want to control their own costs and destiny.

### Networking & Interconnect: The "Silent Winners" of AI Buildout

As AI clusters scale, the networking layer (Ethernet switches, optics, DSPs, retimers, PCIe signal conditioning) is seeing unprecedented demand. $120.6B global semiconductor sales in May 2026 — +9.2% sequentially, +104.1% YoY, 15th consecutive month of growth. Broadcom, Marvell, Credo, Astera Labs are the pure-play names. Co-packaged optics reshaping supply chains (Astute Group, August 12).

### Memory: Tight Through Mid-2027

Micron management: no new production capacity until mid-2027. Memory prices elevated, HBM critical bottleneck for AI. Amazon raised CapEx guidance partly due to memory prices. SK Hynix planning US ADR debut (Bloomberg).

### Nvidia Positioning

- ~80% AI accelerator share, CUDA moat intact, gross margins mid-70% range
- Forward P/E ~24x — cheap for the growth rate per Motley Fool (August 9)
- $500 billion AI infrastructure financing initiative (BlackRock partnership) — Jensen Huang framing NVIDIA as the "operating system" of AI factories
- Morgan Stanley TMT Conference keynote: Jensen Huang on AI, compute, tokens, and the new global economy
- 7 Japanese industrial giants signed into Nvidia Physical AI coalition (Motley Fool, August 13)

### Semiconductor Market Cap Leaders (as of August 7, 2026)

1. Nvidia — $5.304T (most valuable semiconductor company)
2. TSMC — $2.168T
3. Samsung — $1.071T
(TSMC challenges Intel for most valuable semiconductor company title.)

---

## 4. Watchlist for the Coming Week (August 14–20, 2026)

### Immediate Catalysts

| Date/Window | Event | Why It Matters |
|---|---|---|
| **Aug 12–13** | CPI report + Fed decision proximity | August CPI expected 3.4% YoY; Fed funds rate at 3.5–3.75%; markets pricing ~56.5% probability of at least one 25bps rate move in 2026. Tech/growth stock sensitivity high. |
| **Aug 13** | Nvidia analyst day / Morgan Stanley TMT follow-ups | Multiple Motley Fool pieces published Aug 13: "Nvidia Stock Investors Just Got Good News From Wall Street," "Jensen Huang Signed 7 Japanese Industrial Giants Into Physical AI Coalition," "Prediction: Nvidia Worth $6T by End of 2026." |
| **Aug 26** | **Nvidia Q2 FY2027 earnings** | The single biggest scheduled event. Consensus expects blowout; Q3 guide of $54B (±2%) already given. Key questions: Blackwell Ultra trajectory, Rubin platform timeline, gross margin sustainability at 73.3%, sovereign AI progress, competitive framing vs. custom silicon. |
| **Ongoing** | EU AI Act enforcement (since Aug 2) | First compliance audits and enforcement actions could surface. Enterprise AI deployment decisions now carry legal weight. |
| **Ongoing** | US strategic AI accelerator export control rule | Expected formal publication timing unclear. Until it lands, procurement uncertainty for advanced GPUs/ASICs, especially Middle East and Southeast Asia destinations. |

### Structural Themes to Track

1. **TSMC pricing power vs. custom silicon acceleration** — watch hyperscaler CapEx allocation shifts. If budgets move from merchant silicon (Nvidia/AMD) to internal R&D + direct foundry orders, that validates the structural threat.

2. **Samsung 2nm ramp** — 163% capacity increase by 2026; yield progress (currently ~50–60%) is the key metric. If yields cross 70%, Samsung becomes a credible alternative for customers wanting non-TSMC options.

3. **Intel 18A external customer wins** — the foundry diversification thesis hinges on Intel landing meaningful third-party designs. Any announced wins would be significant.

4. **Memory pricing trajectory** — supply tight through mid-2027 per Micron. Any sign of demand softening or capacity coming online early would hit memory names (MU, SK Hynix, Samsung memory).

5. **Networking/interconnect companies** — Broadcom 200T switch tape-out, Marvell optics $1B run rate, Credo and Astera Labs hyperscaler adoption. These are the picks-and-shovels plays of AI infrastructure.

6. **Nvidia earnings positioning** — the stock has risen ~17% YTD vs. S&P 500 ~7%, underperforming earlier in the year. Trading at ~24x forward earnings. Analyst targets: $225–230 by month-end (Intellectia AI). The earnings reaction could be the catalyst that resets the AI stock rotation.

---

## Sources

- CRN: "AWS Vs. Microsoft Vs. Google Cloud Earnings Q2 2026 Face-Off" (Aug 3, 2026)
- Yahoo Finance / Daniel Howley: "Amazon, Meta, and Microsoft stocks surge as AI hyperscalers post strong earnings" (Aug 3, 2026)
- UncoverAlpha: "Amazon, Google, Microsoft, Meta Q2 earnings: The AI CapEx ROIC is bad thesis is DEAD" (Aug 3, 2026)
- AlphaSpread: NVDA Q2-2026 Earnings Call summary
- Intelellectia.AI: "Nvidia Stock Earnings August 2026: Q2 Preview & Investment Outlook" (Aug 13, 2026)
- Digitimes: "TSMC 3nm lead times surpass one year as Samsung faces Intel in foundry push" (Jun 25, 2026)
- SemiWiki: "TSMC vs Intel Foundry vs Samsung Foundry 2026" (Feb 13, 2026)
- Enki: "TSMC Semiconductor Capacity, 15% Price Hike on 3nm Chips, 90% Market Share, and $40B Arizona Fab Delays" (2026)
- Astute Group: "US reworks AI chip export controls, raising uncertainty for global semiconductor supply chains" (Aug 6, 2026)
- CES Intelligence: "AI Sovereignty 2026: Export Controls, EU AI Act & Corporate Implications"
- ML Strategies / Mintz: "2026 AI Policy and Semiconductor Outlook" (Feb 4, 2026)
- Yahoo Finance / Subham Roy: "4 Networking Semiconductor Stocks to Watch in August 2026" (Jul 23, 2026)
- Investing.com: "Beyond Nvidia: 5 Semiconductor Stocks Set to Dominate 2026"
- Motley Fool / Keithen Drury: "3 Artificial Intelligence (AI) Stocks to Load Up On in August" (Aug 9, 2026)
- Motley Fool / multiple authors: Nvidia coverage Aug 10–13, 2026
- Bloomberg: "Semiconductor Stocks Slide Amid AI Spending Concerns" (Aug 2026)
- Facebook/GlobalstatsX: Largest Semiconductor Companies by Market Cap as of Aug 7, 2026
- Semiconductor Industry Association: "Semiconductor Supply Chain Investments" (ongoing tracking)

---

*Generated by Hermes Agent weekly research roundup. Data as of August 13, 2026 close. For informational purposes only — not investment advice.*
