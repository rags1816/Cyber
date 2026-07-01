# 🛡️ CyberScore Pro

**Cyber Security Health Check, Risk Quantification & Optimisation Toolkit**

A self-contained single-page HTML tool that assesses an organisation's cyber security maturity across 8 control domains, quantifies business risk exposure, calculates the cost of inaction, and generates an optimised remediation roadmap — aligned to 12+ industry frameworks including the Five Eyes AI & Cyber Resilience principles.

> **v1.9** — All result tabs fully implemented. Open `index.html` and everything works out of the box.

---

## ✨ Features

| Capability | Detail |
|---|---|
| **CyberScore™** | 0–100 maturity score across 8 security domains |
| **Business Risk Score** | Sector-adjusted risk exposure (0–100, lower = better) |
| **Cost of Inaction** | FAIR-based annualised loss expectancy in £/€/$ |
| **Domain Score Bars** | Per-domain bars with Δ vs sector peer benchmark |
| **Risk Matrix** | Likelihood × impact heat grid for 6 top threat scenarios |
| **Framework Adherence** | Coverage % for 12+ frameworks auto-selected by sector & region |
| **Gap Register** | 14 pre-built gaps with severity, effort, cost, framework refs, Five Eyes tags |
| **Optimiser** | Budget/time/capacity sliders with ranked actions + before/after projection |
| **Certification Roadmap** | Phased 4-quarter plan sequenced by severity and target cert |
| **Five Eyes Alignment** | 7-principle scoring panel (joint statement 22 Jun 2026 + Agentic AI May 2026) |
| **AI Narratives** | Claude or Gemini — executive summary, gap insights, cost narrative |
| **PDF Export** | Full A4 report with scores, gaps, cost model, and roadmap |
| **History** | Auto-save, export/import JSON, trend chart, side-by-side comparison |

---

## 🚀 Quick Start

No installation, no dependencies, no server required.

1. Download `index.html`
2. Open it in any modern browser (Chrome, Firefox, Edge, Safari)
3. Click **▶ Run Demo** to see sample results, or **Begin Assessment** for your own

That's it. Everything runs locally in your browser.

---

## 🔑 API Key Setup (Optional — for AI features)

AI-powered narratives and gap insights require a key from:

- **[Google Gemini](https://aistudio.google.com/app/apikey)** — Free tier available (Gemini 1.5 Flash) ✅ recommended
- **[Anthropic Claude](https://console.anthropic.com/)** — ~$0.003 per 1,000 tokens (Claude Haiku)

### How to add your key

1. Open the tool
2. Click **⚙ Settings** (bottom mini-bar, or gear icon)
3. Select your provider (Gemini or Claude)
4. Paste your API key
5. Tick **"Remember in browser"** to persist between sessions
6. Click **Save & enable AI**

> ⚠️ **Your key is stored in your browser's localStorage only.** It is never written to the HTML file, never sent to GitHub, and never transmitted to any server other than the AI provider's API directly from your browser.

---

## 🔒 Security & Privacy

| Concern | Answer |
|---|---|
| Is my API key in the source code? | **No.** Never. Entered at runtime via Settings panel only. |
| Does the tool phone home? | **No.** Entirely client-side. No backend, no analytics. |
| Where is assessment data stored? | **Browser localStorage only.** |
| Is it safe to put this on a public GitHub repo? | **Yes** — as long as you never paste your key into the HTML before pushing. |
| What if I accidentally commit a key? | Revoke it immediately at your provider's console, then push a new commit without it. |

---

## 🏗️ Architecture

```
index.html                   ← entire application (self-contained, ~226 KB)
├── HTML structure           ← 9 screens (welcome, context, quiz, results…)
├── CSS (embedded)           ← dark theme, responsive layout, glassmorphism
└── JavaScript (embedded)
    ├── Scoring engine       ← FAIR-based ALE, domain weighting, sector multipliers
    ├── Framework matcher    ← auto-selects from 12+ frameworks by sector/region/size
    ├── GAP_DB               ← 14 pre-built gaps with severity, controls, Five Eyes tags
    ├── renderDomainBars()   ← domain bars + benchmark strip
    ├── renderRiskAnalysis() ← risk bars, heat matrix, qualitative grid
    ├── renderCostModel()    ← ALE formula, cost cards, regulatory fine bars
    ├── renderFrameworks()   ← framework adherence table
    ├── renderGapRegister()  ← severity-filtered gap list
    ├── updateOptimiser()    ← ROI-ranked actions + before/after projection
    ├── renderRoadmap()      ← phased 4-quarter remediation timeline
    ├── renderCharts()       ← Chart.js radar + horizontal bar
    ├── renderFiveEyes()     ← 7-principle alignment panel
    ├── runAI()              ← Gemini & Claude API runner
    ├── History engine       ← localStorage, export/import JSON, trend chart
    ├── Chart.js             ← radar + bar charts (CDN)
    ├── jsPDF                ← PDF export (CDN)
    └── localStorage         ← key & prefs persistence (browser only)
```

---

## 📋 Supported Frameworks

| Framework | Type | Region/Sector |
|---|---|---|
| Cyber Essentials / CE+ | Certification | UK — all sectors |
| ISO 27001:2022 | Certification | International |
| NIST CSF 2.0 | Standard | All sectors |
| CIS Controls v8 | Standard | All sectors |
| DORA | Regulatory | EU Financial Services |
| NIS2 Directive | Regulatory | EU Critical Infrastructure |
| SOC 2 Type II | Certification | SaaS / Cloud services |
| PCI DSS 4.0 | Regulatory | Payment card processing |
| HIPAA Security Rule | Regulatory | US Healthcare |
| FCA SYSC / PS21/3 | Regulatory | UK Financial Services |
| IASME Cyber Assurance | Certification | UK SMEs |
| **Five Eyes AI & Cyber Resilience** | **International** | **All — 7 principles scored** |

---

## 🎯 Assessment Modes

| Mode | Questions | Time | Best for |
|---|---|---|---|
| Quick Check | 16 (2 per domain) | ~15 min | Senior leadership overview, first-pass |
| Deep Dive | 40+ (5 per domain + Five Eyes AI Qs) | ~45 min | Certification gap analysis, board reporting |

---

## ⚙️ Controls Reference

### Bottom mini-bar (always visible)
| Control | Purpose |
|---|---|
| AI status dot | Green = AI active and key saved |
| **🚀 Start Assessment** | Context-aware start / restart button |
| **⚙ Admin Settings** | Opens Admin panel (password-protected) |

### ⚙ Settings panel (slide-in)
| Control | Purpose |
|---|---|
| Currency buttons | Switch between £ GBP, € EUR, $ USD — updates all figures instantly |
| Provider selector | Gemini (free) or Claude |
| API key field | Runtime only — never saved to the HTML file |
| Remember in browser | Persists key in localStorage on your device |
| Save & enable AI | Activates AI narratives |
| Clear saved key | Removes key from browser storage |

---

## 📊 CyberScore Bands

| Band | Score | Meaning |
|---|---|---|
| 🔴 Critical | 0–39 | Significant breach risk. Immediate action required. |
| 🟠 Developing | 40–59 | Basic controls only. |
| 🟡 Established | 60–74 | Structured programme. Cyber Essentials Plus achievable. |
| 🟢 Advanced | 75–89 | Mature programme. ISO 27001 within reach. |
| ⭐ Leading | 90–100 | Industry benchmark. |

---

## 🗺️ Roadmap

### ✅ Completed
- [x] 8 security domains with Quick Check + Deep Dive modes
- [x] FAIR-based risk scoring with sector multipliers
- [x] 12+ framework auto-selection by sector/region/size
- [x] All 8 result tabs fully implemented (v1.9)
- [x] Five Eyes AI & Cyber Resilience alignment panel
- [x] 14-gap register with Five Eyes-tagged gaps
- [x] ROI-ranked optimiser with 3 objective modes
- [x] Phased 4-quarter remediation roadmap
- [x] Radar + horizontal bar charts
- [x] AI narratives (Gemini + Claude)
- [x] PDF export
- [x] History with auto-save, export/import, trend chart, comparison modal
- [x] Currency switching (GBP/EUR/USD)
- [x] Toast notification system

### 🔮 Planned
- [ ] Sector-specific question variants (healthcare, finserv, defence)
- [ ] Comparison mode — assess multiple sites or business units
- [ ] Email report delivery via Web3Forms
- [ ] Embeddable widget mode for consultancy websites
- [ ] CMMI-style maturity level mapping alongside numeric scores

---

## 📄 Disclaimer

CyberScore Pro is a **self-reported maturity assessment tool**. Scores are based on answers provided by the user and are indicative only. This tool does not constitute a professional cyber security audit, penetration test, or compliance certification. Organisations should engage qualified cyber security professionals for formal assessments and certification.

---

## 📬 Contact

Built and maintained as an open diagnostic tool. Contributions, issues, and feature requests welcome via GitHub Issues.

---

*Single-file HTML app — no build step, no npm, no server. Just open and go.*  
*CyberScore Pro v1.9 · Last updated 23 June 2026*
