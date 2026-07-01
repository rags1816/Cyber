# CyberScore Pro — Developer Handover Document

**Version:** 1.3  
**Frozen date:** 15 June 2026  
**File:** `index.html` (2,807 lines, ~176KB)  
**Status:** ✅ Active development build

---

## 1. What This Tool Is

CyberScore Pro is a self-contained, single-file HTML web application that delivers a full cyber security health check for any business. It requires no server, no backend, no npm, and no build step. Open `index.html` in a browser and it runs.

The tool produces three scored outputs from a questionnaire:

| Output | Description |
|---|---|
| **CyberScore™** | 0–100 security maturity score across 8 control domains |
| **Business Risk Score** | 0–100 risk exposure (lower = better), sector-adjusted |
| **Cost of Inaction** | Annualised expected loss in £/€/$ using FAIR methodology |

These feed into a framework adherence matrix, a gap register, an optimisation engine, a certification roadmap, and optional AI-generated narratives.

---

## 2. File Structure

There is one deliverable file. Everything — HTML, CSS, JavaScript, data, logic — lives inside it.

```
index.html                  ← entire application
README.md                   ← public-facing documentation
HANDOVER.md                 ← this document
.gitignore                  ← protects secrets, system files
```

### Internal structure of index.html

| Section | Lines (approx) | Purpose |
|---|---|---|
| Freeze stamp comment | 1–16 | Version control marker |
| `<head>` / CDN imports | 17–11 | Fonts, Chart.js, jsPDF |
| CSS `:root` variables | ~13–27 | Design tokens — colours, radii, fonts |
| CSS component styles | ~28–410 | All visual styles, 60+ component classes |
| HTML — Admin bar | ~413–410 | Fixed bottom bar (mode, AI, key, currency) |
| HTML — Welcome screen | ~415–456 | Mode selector (Quick/Deep), start button |
| HTML — Context screen | ~458–646 | Org profile, frameworks preview, risk prefs |
| HTML — Quiz screen | ~648–705 | Dynamic question renderer |
| HTML — Results screen | ~707–810 | 7-tab results layout (all tabs) |
| JS — State variables | ~813–830 | Global app state |
| JS — Currency helpers | ~831–833 | `fmtCurr()`, `CURR_SYMBOLS`, `CURR_RATES` |
| JS — `DOMAINS` array | ~838–976 | 8 domains × 5 questions each (40 total) |
| JS — `ALL_FRAMEWORKS` | ~980–994 | 12 framework definitions |
| JS — Demo data | ~998–1008 | `DEMO_ANSWERS`, `DEMO_CTX` |
| JS — Admin / API functions | ~1012–1040 | Mode toggle, AI toggle, key save/load |
| JS — Navigation | ~1046–1061 | `showScreen()`, `selectMode()`, etc. |
| JS — Framework matcher | ~1066–1082 | `updateFrameworks()` auto-selection logic |
| JS — Quiz engine | ~1085–1148 | `startQuiz()`, `renderDomain()`, `quizNext()` |
| JS — Scoring engine | ~1152–1175 | `calculateScores()`, FAIR ALE calculation |
| JS — `SECTOR_BENCHMARKS` | ~1175 | Peer benchmark scores by sector |
| JS — Results renderers | ~1177–1421 | All `render*()` functions |
| JS — `GAP_DB` array | ~1425–1467 | 10 pre-built gap definitions |
| JS — Gap register | ~1468–1470 | `renderGapRegister()`, `filterGaps()` |
| JS — Optimiser | ~1471–1526 | `setOptMode()`, `updateOptimiser()` |
| JS — Roadmap | ~1527–1572 | `renderRoadmap()` |
| JS — Charts | ~1577–1603 | Chart.js radar + bar chart |
| JS — Tab navigation | ~1598–1605 | `switchTab()` |
| JS — AI functions | ~1609–1663 | `runAI()`, `generateAISummary()`, etc. |
| JS — PDF export | ~1664–1726 | `downloadPDF()` using jsPDF |
| JS — Five Eyes constants | ~1399–1470 | `FE_PRINCIPLES` array, 7 principles with domain mappings + AI question indices |
| JS — Five Eyes scoring | ~1472–1560 | `calcFiveEyesScore()`, `getFEBand()`, `dismissFEAlert()` |
| JS — Five Eyes render | ~1561–1640 | `renderFiveEyes()`, `generateFEAnalysis()` |
| JS — Toast system | ~2181–2355 | `showToast()`, `toastFirstSave()`, smart state logic, all toast triggers |
| JS — History system | ~1828–2145 | `saveAssessmentToHistory()`, `renderHistoryTab()`, `compareWithPrevious()`, export/import |
| JS — localStorage | ~2148–2217 | `savePrefs()`, `loadPrefs()`, `clearSavedKey()` |
| JS — Init | ~2218–2222 | `DOMContentLoaded` bootstrap |

---

## 3. Key Data Structures

### 3.1 DOMAINS array (line ~838)

Each domain object defines a scoring pillar:

```javascript
{
  id: 'iam',                    // unique key used throughout
  name: 'Identity & Access',    // display name
  icon: '🔐',                   // emoji used in UI
  color: '#00C9FF',             // domain accent colour (hex)
  desc: 'Description text',     // shown in quiz header
  weight: 0.15,                 // weighting in overall CyberScore (all weights sum to 1.0)
  questions: [                  // array of 5 question objects
    {
      q: 'Question text',
      hint: 'Hint shown below question',
      opts: [                   // exactly 5 options, scored 0–4
        'Lowest maturity (score 0)',
        'Basic (score 1)',
        'Developing (score 2)',
        'Established (score 3)',
        'Best practice (score 4)'
      ]
    }
  ]
}
```

**The 8 domains and their weights:**

| Domain | ID | Weight |
|---|---|---|
| Identity & Access | `iam` | 15% |
| Network Security | `network` | 12% |
| Detection & Response | `detection` | 15% |
| Cloud & Asset Management | `cloud` | 12% |
| Data Protection | `data` | 12% |
| Supply Chain & 3rd Party | `supplychain` | 10% |
| Governance & Policy | `governance` | 12% |
| Awareness & Culture | `awareness` | 12% |

> Weights must always sum to exactly 1.00. Adjust with care — changing weights changes all historical score comparisons.

### 3.2 ALL_FRAMEWORKS array (line ~980)

```javascript
{
  id: 'ISO27001',
  name: 'ISO 27001:2022',
  sub: 'International gold standard cert',
  tag: 'certification',          // 'certification' | 'regulatory' | 'international'
  regions: ['UK','EU','US'],     // or 'all'
  sectors: ['Financial Services'], // or 'all'
  sizes: ['sme','mid','large','enterprise'], // or 'all'
  controls: ['iam','network','detection','cloud','data','supplychain','governance','awareness'],
                                 // which domain IDs this framework maps to
  weight: 1.0                    // coverage calculation multiplier (0.75–1.0)
}
```

Framework is auto-selected when: `regions` matches ctx.region AND `sectors` matches ctx.sector AND `sizes` matches ctx.size.

### 3.3 GAP_DB array (line ~1425)

```javascript
{
  domain: 'detection',           // which domain this gap belongs to
  title: 'Gap title',            // shown as heading in gap register
  severity: 'critical',          // 'critical' | 'high' | 'medium'
  effort: 'High',                // 'Low' | 'Medium' | 'High'
  cost: '£15,000–£40,000/yr',    // display string
  riskReduction: 22,             // points subtracted from Risk Score if fixed
  frameworks: ['ISO27001','NIST'], // frameworks this gap affects
  controlRef: 'ISO 27001 A.8.15 / NIST DE.CM-1', // control reference
  body: 'Explanation text',      // shown in gap card body
  aiInsight: ''                  // populated at runtime by AI
}
```

### 3.4 SECTOR_BENCHMARKS (line ~1175)

Maps sector names to peer average CyberScore. Used for delta calculations in domain bars and bar chart.

```javascript
const SECTOR_BENCHMARKS = {
  'Financial Services': 72,
  'Healthcare & Life Sciences': 68,
  'Technology & SaaS': 74,
  // ... etc
}
```

### 3.5 DEMO_CTX and DEMO_ANSWERS (line ~998)

Pre-filled data loaded in Demo mode. `DEMO_CTX` sets all context screen fields. `DEMO_ANSWERS` provides a complete answer set for a UK Financial Services mid-market firm with deliberately weak Detection and Supply Chain scores to show meaningful gaps.

---

## 4. Scoring Engine

### 4.1 CyberScore calculation (line ~1152)

```
For each domain:
  domain_score = (sum of answers 0–4) / (max possible answers) × 100

Overall CyberScore = Σ (domain_score × domain_weight)
```

Quick mode uses only 2 questions per domain (first 2 in the array). Deep Dive uses all 5. The scoring formula is identical — only the denominator changes.

### 4.2 Risk Score calculation (line ~1163)

```
sector_multiplier = lookup table by sector (1.1 – 1.4)
Risk Score = MIN(100, ROUND((100 - CyberScore) × sector_multiplier × 0.85))
```

Higher sector multiplier = higher risk for same CyberScore. Financial Services (1.4) and Energy (1.35) are highest risk sectors by default.

### 4.3 Cost of Inaction — FAIR-based ALE (line ~1166)

```
SLE (Single Loss Expectancy) = revenue × 0.18
ARO (Annual Rate of Occurrence) = (RiskScore / 100) × 0.7
ALE = SLE × ARO + (revenue × 0.02)
```

The `0.18` exposure factor (18% of revenue) and `0.02` ongoing compliance cost are calibrated against IBM Cost of a Data Breach 2024 averages for UK/EU mid-market. These are the primary tuning parameters for cost model accuracy.

---

## 5. AI Integration (line ~1609)

### 5.1 `runAI(system, user)` — core function

Unified AI caller supporting two providers. Returns a plain text string.

```javascript
// Claude (Anthropic)
POST https://api.anthropic.com/v1/messages
Headers: x-api-key, anthropic-version, anthropic-dangerous-allow-browser
Model: claude-haiku-4-5-20251001
Max tokens: 1000

// Gemini (Google)
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent
Model: gemini-1.5-flash
Max tokens: 1000
```

> `anthropic-dangerous-allow-browser: true` is required for direct browser→Anthropic API calls. This is intentional and documented — keys are user-supplied at runtime.

### 5.2 AI functions

| Function | Trigger | Output location | Prompt length |
|---|---|---|---|
| `generateAISummary()` | Auto on results load (if AI on) | `#ai-domain-content` | ~180 words |
| `generateGapInsight(i)` | Called per gap on gap tab | `#gap-ai-{i}` | 40 words max |
| `generateBoardReport()` | Button click on Roadmap tab | `#ai-roadmap-content` | ~250 words |

### 5.3 localStorage key persistence (line ~1737)

```javascript
LS_KEY_API   = 'csp_api_key'    // stored only if user ticks "Remember in browser"
LS_KEY_PROV  = 'csp_provider'   // always saved on Save click
LS_KEY_CURR  = 'csp_currency'   // always saved on currency change
LS_KEY_MODE  = 'csp_adm_mode'   // always saved on mode toggle
```

Key is **opt-in** — only persisted if `#adm-remember` checkbox is ticked. `clearSavedKey()` removes it immediately.

---

## 6. External Dependencies

All loaded from CDN — no npm, no local node_modules.

| Library | Version | CDN | Purpose |
|---|---|---|---|
| Chart.js | 4.4.1 | cdnjs.cloudflare.com | Radar + bar charts |
| jsPDF | 2.5.1 | cdnjs.cloudflare.com | PDF generation |
| Google Fonts | — | fonts.googleapis.com | DM Sans, DM Serif Display, DM Mono |

> If CDN access is unavailable (air-gapped environments), download these libraries and reference them as local files.

---

## 7. Admin Bar Reference

The admin bar is `#admin-bar`, fixed to `bottom: 0`. It is always visible.

| Element ID | Function | Notes |
|---|---|---|
| `#adm-demo-btn` | Switch to demo mode | Loads `DEMO_CTX` + `DEMO_ANSWERS` |
| `#adm-live-btn` | Switch to live mode | Shows API key fields |
| `#adm-mode-badge` | Shows current mode | Text: Demo / Live |
| `#ai-toggle` | Enables AI features | Requires API key to be functional |
| `#adm-provider` | Claude / Gemini selector | Persisted to localStorage |
| `#adm-key` | Password input for API key | Never written to file |
| `#adm-remember` | Opt-in key persistence | Saves to `csp_api_key` in localStorage |
| `#adm-status` | Status message | Updated by save/load functions |
| `#adm-currency` | GBP / EUR / USD | Calls `setCurrency()`, rerenders costs |

---

## 8. Screen & Tab Flow

```
screen-welcome
    └─→ screen-context  (startAssessment())
            └─→ screen-quiz  (startQuiz())
                    └─→ screen-results  (calculateAndRender())
                            ├─ tab: domains      (default)
                            ├─ tab: risk
                            ├─ tab: cost
                            ├─ tab: frameworks
                            ├─ tab: gaps
                            ├─ tab: optimiser
                            └─ tab: roadmap
```

Screen switching: `showScreen('screen-id')` — adds `.active` class, removes from all others.

Tab switching: `switchTab('tabname')` — shows `#tab-{tabname}`, activates button.

---

## 9. CSS Design Tokens

All colours, radii, and fonts are defined as CSS custom properties on `:root` (line ~13).

| Token | Value | Used for |
|---|---|---|
| `--bg` | `#0B0F1A` | Page background |
| `--bg2` | `#111827` | Card backgrounds |
| `--bg3` | `#1a2236` | Nested card / code backgrounds |
| `--cyan` | `#00C9FF` | Primary accent, scores, links |
| `--cyan-d` | `#0099CC` | Darker cyan for gradients, buttons |
| `--blue` | `#3B82F6` | Secondary gradient colour |
| `--red` | `#EF4444` | Critical severity, risk |
| `--amber` | `#F59E0B` | High severity, cost, warnings |
| `--green` | `#10B981` | Good scores, success states |
| `--purple` | `#8B5CF6` | AI features, roadmap |
| `--ink` | `#F0F4FF` | Primary text |
| `--ink2` | `#A8B8D8` | Secondary text |
| `--ink3` | `#6B82A8` | Muted/hint text |
| `--border` | `rgba(255,255,255,0.08)` | Default border |
| `--font` | `'DM Sans'` | All body text |
| `--serif` | `'DM Serif Display'` | Headings, hero text |
| `--mono` | `'DM Mono'` | Code refs, formula display |

---

## 10. Known Limitations (v1.0)

| Limitation | Impact | Suggested fix |
|---|---|---|
| ✅ Assessment history now persists | History tab saves all results automatically | — implemented in v1.1 |
| Gap DB is static (10 gaps) | Does not adapt dynamically to specific answers | Map gap visibility to domain scores < threshold |
| Sector benchmark scores are hardcoded | May become stale over time | Connect to a data source or make admin-editable |
| AI gap insights called individually | N API calls for N gaps — can be slow/costly | Batch all gaps into one API call, parse JSON response |
| No mobile optimisation | Some tables/grids overflow on small screens | Add `@media (max-width: 480px)` breakpoints to results |
| PDF is basic | No charts in PDF, no cover page | Use html2canvas to capture Chart.js canvases before PDF |
| No i18n / translation | English only | Externalise all strings to a language object |
| Single file size (~130KB) | Fine for current scope | Split into modules if adding significantly more features |

---

## 11. Planned v1.1 Features (Priority Order)

### Must have (next sprint)
- [ ] **Dynamic gap filtering** — only show gaps where domain score < 60, not all 10 always
- [ ] **Answer persistence** — save quiz state to sessionStorage so page refresh doesn't lose progress
- [ ] **Batch AI gap insights** — single API call returns all gap insights as JSON, parse and render
- [ ] **Mobile layout fix** — results tabs and tables need responsive treatment below 480px

### ✅ Completed in v1.1
- [x] **History tab** — auto-save, load/restore, export/import (JSON), trend chart, delta strip, side-by-side comparison, drag-and-drop import, search/filter, delete per record or clear all

### Should have (v1.1)
- [ ] **Email report** — send PDF to email via Web3Forms (key already in ESG toolkit)
- [ ] **Multiple assessment comparison** — save 2 assessments, show delta
- [ ] **Expanded gap DB** — grow from 10 to 30 gaps, all dynamically filtered by domain score
- [ ] **Sector-specific question variants** — different question emphasis for FinServ vs Healthcare
- [ ] **Charts in PDF** — use `html2canvas` to embed radar chart in PDF export

### Nice to have (v1.2)
- [ ] **Historical tracking** — store past assessments in localStorage, show trend line
- [ ] **Embeddable widget mode** — `?embed=true` hides admin bar, uses query-string context
- [ ] **White-label mode** — logo URL, brand colour, and org name via URL params or admin config
- [ ] **CMMI maturity levels** — overlay 1–5 maturity levels alongside numeric scores
- [ ] **Threat intelligence feeds** — pull live sector breach data from NCSC or ENISA APIs
- [ ] **Multi-site mode** — assess multiple sites/BUs, show consolidated group score

---

## 12. How to Add a New Domain

1. Add a new object to the `DOMAINS` array (line ~838) following the exact schema in Section 3.1
2. Set `weight` — ensure all 9 domain weights still sum to `1.0` (adjust one existing domain)
3. Add the domain's `id` to any `controls` arrays in `ALL_FRAMEWORKS` where relevant
4. Add the domain `id` to `DEMO_ANSWERS` with a test array of 5 answer values (0–4)
5. No other changes needed — all render functions iterate `DOMAINS` dynamically

---

## 13. How to Add a New Framework

1. Add a new object to `ALL_FRAMEWORKS` (line ~980) following the schema in Section 3.2
2. Set `regions`, `sectors`, `sizes` correctly — use `'all'` for universal applicability
3. List the `controls` (domain IDs) that this framework maps to
4. Set `weight` between 0.75–1.0 (affects coverage % calculation)
5. No HTML changes needed — the framework table and chip preview render dynamically

---

## 14. How to Add a New Gap

1. Add a new object to `GAP_DB` (line ~1425) following the schema in Section 3.3
2. Set `domain` to an existing domain ID — this determines which tab the gap appears under
3. Set `riskReduction` (typically 8–30) — this feeds the Optimiser's ranking model
4. Leave `aiInsight: ''` — populated at runtime by `generateGapInsight()`
5. Gaps are displayed in the order they appear in `GAP_DB` within each severity level

---

## 15. How to Update Sector Benchmarks

Edit `SECTOR_BENCHMARKS` (line ~1175). Values are peer average CyberScores (0–100).

Sources for calibration:
- NCSC Cyber Security Longitudinal Survey (annual, UK)
- Verizon DBIR (annual, global, by sector)
- CrowdStrike Global Threat Report (annual)
- Microsoft Digital Defense Report (annual)

---

## 16. Deployment

### GitHub Pages (current)
Push `index.html`, `README.md`, `.gitignore` to a public repo. Enable Pages → Deploy from branch → main → / (root). Live at `https://username.github.io/repo-name/`.

### Netlify (recommended for production)
Drag the folder to app.netlify.com/drop. Instant deploy, custom domain, HTTPS. If adding server-side API key proxy (Option C security model), use Netlify Functions.

### Air-gapped / local
Just open `index.html` in a browser. No network needed except for Google Fonts (cosmetic only) and CDN libraries (Chart.js, jsPDF). Download those locally if needed.

---

## 17. Version Control Convention

```
v1.0   2026-06-15  Initial frozen release
v1.1   2026-06-15  History system: auto-save, restore, export/import,
                   trend chart, delta strip, comparison modal (this version)
v1.2   2026-06-15  Toast notifications (smart save/export/import/delete alerts)
v1.3   2026-06-22  Five Eyes framework (joint statement 22 Jun 2026 + May 2026 agentic AI)
v1.4   TBD         Dynamic gaps, batch AI, mobile fix, answer persistence
v1.3   TBD         White-label, email report, Supabase cloud option
```

Each frozen version should have the version stamp updated in:
1. The HTML comment block at line 1 of `index.html`
2. The `<title>` tag (add version suffix)
3. This HANDOVER.md header
4. A git tag: `git tag v1.0 && git push origin v1.0`

---

## 18. Contact & Ownership

| Item | Detail |
|---|---|
| Built with | Claude Sonnet (Anthropic) — June 2026 |
| Reference tools | ESG Health Check v3, Career Suite (Career Toolkit) |
| Design system | DM Sans / DM Serif Display type stack, dark navy palette |
| Scoring methodology | FAIR (Factor Analysis of Information Risk) for cost model |
| Framework sources | NCSC, ISO, NIST, ENISA, CISA, FCA |

---

*This document should be kept alongside the frozen `index.html` in the repository root and updated with each new version.*
