# CyberScore Pro — Quick Reference Card
**v1.3** · Single-page cheat sheet · Keep this open while using the tool

---

## ⚡ Getting Started in 60 Seconds

```
1. Open index.html in Chrome, Firefox, Edge, or Safari
2. Click "Begin Assessment" on the welcome screen
3. Fill in your organisation profile (sector, region, size, revenue)
4. Answer the questions — click any option to select it
5. Click "See Results →" on the final domain
   → Results are saved to History automatically
```

No login. No installation. No internet required (after first load).

---

## 🎛️ Admin Bar (bottom of screen — always visible)

| Control | What it does |
|---|---|
| **Demo** button | Loads pre-filled Financial Services example — good for presentations |
| **Live AI** button | Switches to live mode — shows API key fields |
| **AI Narrative** toggle | ON = AI writes board report & gap insights (needs key) |
| **Claude / Gemini** selector | Pick your AI provider |
| **API key field** | Paste key here — stored in browser only, never in the file |
| **Remember in browser** checkbox | Tick to save key between sessions |
| **Save** button | Saves key and provider preference |
| **Clear** button | Removes saved key from browser storage |
| **£ GBP / € EUR / $ USD** | Changes all cost figures instantly |

---

## 🗺️ Screen Flow

```
Welcome → Context → Quiz (8 domains) → Results (8 tabs)
                                            ↓
        Domains · Risk · Cost · Frameworks · Gaps · Optimiser · Roadmap · History
```

---

## 🛡️ The Three Scores

| Score | Range | What it means |
|---|---|---|
| **CyberScore™** | 0–100 | Higher = more mature security. 75+ = Advanced. |
| **Risk Score** | 0–100 | **Lower = better.** Risk exposure adjusted for your sector. |
| **Cost of Inaction** | £/€/$ | Annualised expected loss at your current posture. |

---

## 📊 CyberScore Bands

| Band | Score | What it means |
|---|---|---|
| 🔴 Critical | 0–39 | Significant breach risk. Immediate action required. |
| 🟠 Developing | 40–59 | Basic controls only. Common in small/growing businesses. |
| 🟡 Established | 60–74 | Structured programme. Cyber Essentials Plus achievable. |
| 🟢 Advanced | 75–89 | Mature, measurable programme. ISO 27001 within reach. |
| ⭐ Leading | 90–100 | Industry benchmark. SOC 2, NIST, DORA alignment. |

---

## 📂 History Tab — Quick Actions

| Action | How |
|---|---|
| **Auto-save** | Every completed assessment saves automatically |
| **Load & View** | Click any history card, or click "Load & View" button |
| **Compare** | Click "Compare with previous" on any record (needs 2+) |
| **Export one** | "⬇ Export" on a card → saves .json file |
| **Export all** | "⬇ Export all (JSON)" button at top of History tab |
| **Import** | "⬆ Import JSON" button, or drag-and-drop .json onto drop zone |
| **Delete one** | "🗑 Delete" on a card |
| **Clear all** | "🗑 Clear all" button (irreversible — export first!) |
| **Search** | Type org name or sector in the search box |
| **Trend chart** | Appears automatically when 2+ assessments exist |

---

## 📋 Framework Tags

| Tag colour | Meaning |
|---|---|
| 🔴 Red chip | Mandatory regulatory requirement for your profile |
| 🔵 Blue chip | Internationally recognised standard (recommended) |
| 🟣 Purple chip | Certification you can pursue |

---

## 🎯 Gap Register — Severity Levels

| Level | Meaning | Typical action timeline |
|---|---|---|
| **CRITICAL** | High likelihood, severe business impact | Within 30 days |
| **HIGH** | Significant risk, likely to be exploited | Within 90 days |
| **MEDIUM** | Moderate risk, part of planned programme | Within 6 months |

---

## 🔧 Optimiser — Three Objective Modes

| Mode | Prioritises | Best used when |
|---|---|---|
| 📉 Reduce risk fastest | Highest risk-reduction per action | Post-breach, board pressure |
| 💰 Best value per spend | Most risk removed per £ spent | Budget constraints |
| 📋 Reach cert soonest | Cert-critical gaps first | Tender deadline, contract requirement |

### Optimiser Sliders

| Slider | Range | Effect |
|---|---|---|
| Annual budget | £5k – £500k | Filters actions to fit envelope |
| Time horizon | 3 – 24 months | Reprioritises quick wins vs structural |
| Internal capacity | 1 – 20 days/month | Flags items needing external resource |
| Risk appetite | Low / Medium / High | Adjusts acceptable residual risk |

---

## 🤖 AI Features

| Feature | Where | How to trigger |
|---|---|---|
| Executive summary | Domains tab | Auto-generated on results load (if AI on) |
| Gap insights | Gaps tab | Auto-generated per gap (if AI on) |
| Board report | Roadmap tab | Click "Generate Board Report" button |

**To enable:** Admin bar → Live AI → paste key → Save → toggle AI Narrative ON

**Providers:**
- **Claude Haiku** (Anthropic) — ~$0.003 per 1,000 tokens. Get key: console.anthropic.com
- **Gemini 1.5 Flash** (Google) — Free tier available. Get key: aistudio.google.com

---

## 📄 PDF Export

Click **⬇ PDF Report** in the results header bar. Generates an A4 document containing:
- Three scores summary · Domain scores vs peer benchmark
- Top 5 security gaps · Cost of inaction breakdown · Footer disclaimer

---

## ⌨️ Assessment Modes

| Mode | Questions | Time | Use for |
|---|---|---|---|
| **Quick Check** ⚡ | 16 (2 per domain) | ~15 min | First pass, leadership briefing, demo |
| **Deep Dive** 🔬 | 40 (5 per domain) | ~45 min | Certification gap analysis, board report |

---

## 🌐 Supported Frameworks (auto-selected by your profile)

| Framework | Type | Applies to |
|---|---|---|
| Cyber Essentials / CE+ | Certification | UK — all sectors |
| ISO 27001:2022 | Certification | International |
| NIST CSF 2.0 | Standard | All sectors |
| DORA | Regulatory | EU Financial Services |
| NIS2 Directive | Regulatory | EU Critical Infrastructure |
| SOC 2 Type II | Certification | SaaS / Cloud services |
| PCI DSS 4.0 | Regulatory | Payment card processing |
| HIPAA Security Rule | Regulatory | US Healthcare |
| CIS Controls v8 | Standard | All sectors |
| FCA SYSC / PS21/3 | Regulatory | UK Financial Services |
| IASME Cyber Assurance | Certification | UK SMEs |

---

## 🔒 Data & Privacy

| Question | Answer |
|---|---|
| Where is my data stored? | Browser localStorage (survives tab close). History tab shows all saved records. |
| Is my API key in the HTML file? | Never. Entered at runtime only. |
| Does anything get sent to a server? | Only AI calls go to Anthropic/Google — nothing else. |
| Can I use it offline? | Yes, after the initial page load. |
| How do I back up my history? | History tab → "⬇ Export all (JSON)" |

---

## 🛡️ Five Eyes AI & Cyber Resilience — Quick Reference

**Issued today: 22 June 2026** — joint statement from NCSC (UK), CISA/NSA (US), ACSC (AU), CCCS (CA), NCSC-NZ

### The two source documents
| Document | Date | Key message |
|---|---|---|
| Five Eyes Joint Leadership Statement | 22 Jun 2026 | "Frontier AI threats: months, not years. Secure-by-design must be standard." |
| Careful Adoption of Agentic AI Services | May 2026 | 30-page guidance: 23 risk categories for autonomous AI systems |

### The 7 principles scored in CyberScore Pro
| # | Principle | Source | Icon |
|---|---|---|---|
| 1 | Secure by Design | Secure-by-Design 2023/24 | 🏗️ |
| 2 | Secure by Default | 22 Jun statement | 🔒 |
| 3 | Defence in Depth | 22 Jun statement | 🛡️ |
| 4 | Transparency & Accountability | May 2026 — Accountability risk class | 🔍 |
| 5 | Human Oversight of AI | May 2026 — Behavioural risk class | 👤 |
| 6 | Least Privilege for AI | May 2026 — Privilege risk class | 🔑 |
| 7 | Resilience over Reliance | May 2026 — Structural risk class | ⚡ |

### Five Eyes AI questions (Deep Dive only)
Five additional questions appear in the Governance domain in Deep Dive mode, prefixed with `[Five Eyes]`:
1. AI security and procurement policy
2. AI systems auditable and explainable?
3. Human override capability for AI security decisions?
4. AI agents assessed for over-permissioning?
5. Tested fallback if AI tool fails?

### Where to find it in the tool
- **Alert banner** — top of results screen (dismissable, links to official guidance)
- **Frameworks tab** — Five Eyes row (purple highlight, NEW badge) + full alignment panel below
- **Gap Register** — three new `[Five Eyes]` tagged gaps
- **Toast** — "Five Eyes statement issued today" appears 2 seconds after results load
- **AI analysis** — if AI enabled, auto-generates in Frameworks tab (purple AI box)

### Five Eyes Alignment Score bands
| Band | Score | Meaning |
|---|---|---|
| ⭐ Exemplary | 85–100 | Strong alignment across all 7 principles |
| 🟢 Aligned | 70–84 | Good alignment, minor gaps |
| 🟡 Developing | 50–69 | Partial alignment, gaps in AI governance |
| 🟠 Partial | 30–49 | Significant gaps — AI security not yet governed |
| 🔴 Significant gaps | 0–29 | Urgent action required across multiple principles |


---

## 🔔 Toast Notifications — What They Mean

Toasts appear bottom-right and auto-dismiss. Click ✕ to close early, or click the action link.

| Toast | Type | What it means / What to do |
|---|---|---|
| **Assessment saved to this browser** | 🟢 Green | First-ever save. Click "Open History tab →" to view and export. |
| **Assessment saved** *(with export nudge)* | 🔵 Blue | Saved but you haven't exported yet. Export now for a permanent backup. |
| **Assessment saved** *(returning user)* | 🟢 Green | Routine confirmation. Shows total record count. |
| **Assessment not saved** | 🟡 Amber | localStorage unavailable (private/incognito mode). Download PDF immediately. |
| **Export complete** | 🟢 Green | File downloaded. Store it safely — it can be re-imported on any device. |
| **Nothing to export** | 🟡 Amber | History is empty. Complete an assessment first. |
| **N record(s) imported** | 🟢 Green | Import succeeded. Shows how many were new and how many were skipped as duplicates. |
| **Import failed** | 🔴 Red | File wasn't valid JSON or wasn't a CyberScore export. Check the file and try again. |
| **Record deleted** | 🔵 Blue | Confirmation after deleting one record. Re-import from a .json export to restore. |
| **N record(s) cleared** | 🔴 Red | All history removed. Import a .json backup to restore. |
| **Nothing to clear** | 🔵 Blue | History was already empty — nothing was deleted. |


---

## 🔁 Starting Over

Click **← Restart** in the results header bar. Your history is preserved — only the active session is cleared.

---

*CyberScore Pro v1.3 · Self-reported maturity assessment · Not a substitute for professional audit*
