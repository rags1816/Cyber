# 🛡️ CyberScore Pro

**Cyber Security Health Check, Risk Quantification & Optimisation Toolkit**

A self-contained single-page HTML tool that assesses an organisation's cyber security maturity across 8 control domains, quantifies business risk exposure, calculates the cost of inaction, and generates an optimised remediation roadmap — aligned to 12+ industry frameworks.

---

## ✨ Features

| Capability | Detail |
|---|---|
| **CyberScore™** | 0–100 maturity score across 9 security domains (including new **Policy Review** domain) |
| **Business Risk Score** | Sector-adjusted risk exposure (0–100, lower = better), dynamically controlled by editable **Risk Settings** multipliers |
| **Cost of Inaction** | FAIR-based annualised loss expectancy in £/€/$ |
| **Risk Matrix** | Likelihood × impact visualisation for top threat scenarios |
| **Framework Adherence** | Coverage % for 12+ frameworks auto-selected by sector & region |
| **Gap Register** | Control-level gaps with severity, effort, cost, and framework references |
| **Optimiser** | Budget/time/capacity sliders with before/after projection |
| **Certification Roadmap** | Phased 18-month plan to target certification (CE, ISO 27001, SOC 2, etc.) |
| **Supplier Evidence** | Client-side document upload (PDF, DOCX, Images < 1MB) with thumbnail previews and downloads using IndexedDB |
| **AI FAQ Toolbar** | Offline copilot lookup panel for immediate answers to common questions |
| **AI Narratives** | Claude or Gemini-powered board report, gap insights, executive summary |
| **PDF Export** | Full A4 report with scores, gaps, cost model, and roadmap |

---

## 🚀 Quick Start

No installation, no dependencies, no server required.

1. Download `cyberscore_pro.html`
2. Open it in any modern browser (Chrome, Firefox, Edge, Safari)
3. Click **Begin Assessment**

That's it. Everything runs locally in your browser.

---

## 🔑 API Key Setup (Optional — for AI features)

AI-powered narratives, gap insights, and the board report require an API key from either:

- **[Anthropic Claude](https://console.anthropic.com/)** — ~$0.003 per 1,000 tokens (Claude Haiku)
- **[Google Gemini](https://aistudio.google.com/app/apikey)** — Free tier available (Gemini 1.5 Flash)

### How to add your key safely

1. Open the tool in your browser
2. Click **Live AI** in the admin bar (bottom of screen)
3. Select your provider (Claude or Gemini)
4. Paste your API key
5. Tick **"Remember in browser"** if you want it to persist between sessions
6. Click **Save**

> ⚠️ **Your key is stored in your browser's localStorage only.** It is never written to the HTML file, never sent to GitHub, and never transmitted to any server other than the AI provider's API directly from your browser.

### To remove your saved key

Click the **Clear** button in the admin bar, or clear your browser's localStorage for the page.

---

## 🔒 Security & Privacy

| Concern | Answer |
|---|---|
| Is my API key in the source code? | **No.** Never. It is entered at runtime only. |
| Does the tool phone home? | **No.** Entirely client-side. No backend, no analytics. |
| Where is assessment data stored? | **Browser memory only.** Cleared when you close the tab. |
| Is it safe to put this on a public GitHub repo? | **Yes** — as long as you never paste your key into the HTML before pushing. |
| What if I accidentally commit a key? | Revoke it immediately at your provider's console, then push a new commit without it. |

---

## 🏗️ Architecture

```
cyberscore_pro.html          ← entire application (self-contained)
├── HTML structure           ← 9 screens (welcome, context, quiz, results…)
├── CSS (embedded)           ← dark theme, responsive layout
└── JavaScript (embedded)
    ├── Scoring engine       ← FAIR-based ALE, domain weighting, sector multipliers
    ├── Framework matcher    ← auto-selects from 12+ frameworks by sector/region/size
    ├── Gap register         ← 10 pre-built gaps with control references
    ├── Optimiser            ← budget/time/risk-mode action ranking
    ├── AI integration       ← Claude & Gemini API calls (runtime key only)
    ├── Chart.js             ← radar + bar charts (CDN)
    ├── jsPDF                ← PDF export (CDN)
    └── localStorage         ← key persistence (browser only)
```

---

## 📋 Supported Frameworks

| Framework | Type | Region/Sector |
|---|---|---|
| Cyber Essentials / CE+ | Certification | UK — all sectors |
| ISO 27001:2022 | Certification | International |
| NIST CSF 2.0 | International | All sectors |
| DORA | Regulatory | EU Financial Services |
| NIS2 Directive | Regulatory | EU Critical Infrastructure |
| SOC 2 Type II | Certification | US/Global SaaS |
| PCI DSS 4.0 | Regulatory | Payment card data |
| HIPAA Security Rule | Regulatory | US Healthcare |
| CIS Controls v8 | International | All sectors |
| FCA SYSC / PS21/3 | Regulatory | UK Financial Services |
| IASME Cyber Assurance | Certification | UK SMEs |

---

## 🎯 Assessment Modes

| Mode | Questions | Time | Best for |
|---|---|---|---|
| Quick Check | 16 (2 per domain) | ~15 min | Senior leadership overview, first-pass |
| Deep Dive | 40 (5 per domain) | ~45 min | Certification gap analysis, board reporting |

---

## ⚙️ Admin Bar Reference

The admin bar is pinned to the bottom of the screen.

| Control | Purpose |
|---|---|
| Demo / Live toggle | Demo uses pre-filled answers for a Financial Services company |
| AI Narrative toggle | Enables AI-generated summaries (requires API key) |
| Provider selector | Choose Claude (Anthropic) or Gemini (Google) |
| API key input | Runtime only — never saved to file |
| Remember in browser | Persists key in localStorage on your device |
| Clear | Removes key from browser storage |
| Currency | Switch between £ GBP, € EUR, $ USD |

---

## 🗺️ Roadmap / Planned Enhancements

- [ ] Sector-specific question variants (healthcare, finserv, defence)
- [ ] Comparison mode — assess multiple sites or business units
- [x] Historical tracking — save and compare assessments over time (Implemented in v1.8+)
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
