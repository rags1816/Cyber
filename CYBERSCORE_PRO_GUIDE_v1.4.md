# CyberScore Pro — Complete Guide v1.4
**Last updated:** 18 June 2026  
**Current build:** v1.4 (active development — supersedes v1.3 frozen)  
**File:** `index.html` — single self-contained file, no build step, no npm, no server required.

---

## Table of Contents
1. [What it is](#1-what-it-is)
2. [How to deploy (GitHub Pages)](#2-how-to-deploy-github-pages)
3. [How to use — Demo mode](#3-how-to-use--demo-mode)
4. [How to use — Live AI mode](#4-how-to-use--live-ai-mode)
5. [Admin bar reference](#5-admin-bar-reference)
6. [Context screen fields](#6-context-screen-fields)
7. [Optimiser — full reference](#7-optimiser--full-reference)
8. [Understanding the results](#8-understanding-the-results)
9. [Making changes after freeze](#9-making-changes-after-freeze)
10. [Known limitations](#10-known-limitations)
11. [Changelog](#11-changelog)

---

## 1. What it is

CyberScore Pro is a self-contained, browser-based cyber security maturity assessment tool. It runs entirely in a single HTML file with no server, no build step, and no external dependencies beyond CDN libraries.

### What it produces
- **CyberScore (0–100)** — weighted maturity score across 8 security domains
- **Business Risk Score** — actuarial model of financial exposure
- **Cost of Inaction** — estimated annual financial loss if gaps go unaddressed
- **Gap register** — prioritised list of identified control weaknesses
- **Framework adherence matrix** — coverage across 12+ compliance standards
- **Optimised remediation roadmap** — constraint-aware action plan
- **AI-written board narrative** — optional, using Claude or Gemini API
- **PDF export** — downloadable report via jsPDF
- **Assessment history** — localStorage persistence with trend charts

### Key design principles

| Principle | Detail |
|---|---|
| Single file | All code, styles and content in one index.html. No npm, no server, no build. |
| No data leaves the browser | Assessment data, answers and scores stay on the user's device. |
| API keys never embedded | Keys are runtime-only. Optional localStorage with explicit opt-in. |
| GBP default currency | All cost figures in GBP by default. EUR and USD switching available. |
| Pre-populated + override | Context fields are pre-filled with sensible defaults; all are editable. |

---

## 2. Deployment — GitHub Pages

### First deployment
1. Create a GitHub repository (public or private)
2. Upload `index.html` to the root of the `main` branch
3. Go to **Settings → Pages** in the repository
4. Set Source: **Deploy from a branch**, Branch: `main`, Folder: `/ (root)`
5. Click Save — site will be live within 1–2 minutes at `https://YOUR-USERNAME.github.io/YOUR-REPO/`

### Updating after changes
1. Replace `index.html` in the repo (commit directly or via pull request)
2. GitHub Pages rebuilds automatically
3. Check progress at `github.com/YOUR-USERNAME/YOUR-REPO/actions`
4. Wait for the green ✓ on the "pages build and deployment" workflow before testing

### Changes not appearing?
> GitHub Pages can take 30–90 seconds after a commit. Always wait for the Actions workflow to complete before testing.

- **Hard refresh:** `Ctrl+Shift+R` (desktop) or `Cmd+Shift+R` (Mac)
- **Mobile:** open in a private/incognito tab to bypass cache
- **Check the Actions tab** in GitHub — the deployment workflow must show a green tick
- Confirm the correct file is at the repo root on the correct branch (check Settings → Pages)

---

## 3. How to use — Demo mode

Demo mode lets anyone see a complete set of results instantly using pre-filled data for a fictional Financial Services company (Acme Financial Ltd). It is the default mode when the page loads.

### Step-by-step
1. Open the page — the **Demo** pill in the admin bar is highlighted purple
2. On the welcome screen, tap **"⚡ Skip to Demo Results →"** for instant results, **OR**
3. Tap **"Begin Assessment →"** to walk through the pre-filled screens manually:
   - Context screen opens pre-populated with Acme Financial Ltd
   - Tap **"Start Assessment →"** — quiz loads with answers already in memory
   - Click **"Next Domain →"** through all 8 domains (no changes needed)
   - Tap **"See Results →"** on the last domain

### What clients see in Demo mode
- Full scoring and reporting capability without answering any questions
- Pre-filled responses at a mid-market Financial Services maturity level
- A purple **"Demo Assessment Responses"** panel on the results screen showing every question and pre-filled answer (Level 1–5) — this only appears when Skip to Demo Results was used
- All results tabs: Domain Scores, Risk Analysis, Cost Model, Frameworks, Gap Register, Optimiser, Roadmap
- Results header shows **"⚡ Demo"** badge (purple) so it's clear this is demonstration data

### Running a real assessment while Demo is selected in admin bar
Selecting Demo in the admin bar only pre-fills the **context form** as a starting point — you can overwrite it. When you click "Start Assessment →" your answers are blank and you answer the questions yourself. The demo answers panel will **not** appear on your results.

---

## 4. How to use — Live AI mode

Live AI mode enables AI-generated narrative summaries. It does **not** require an API key to run an assessment — you can complete a full assessment without AI and optionally add a key to enable narratives.

### Step-by-step
1. Open the admin bar — tap **"⚙ Admin ▲"** at the bottom
2. Tap the **Live AI** pill — it turns cyan; the API key fields expand in the panel
3. Select your AI provider: **Claude (Anthropic)** or **Gemini (Google)**
4. Paste your API key into the password field
5. Optionally tick **"Remember in browser"** to persist the key across sessions
6. Tap **Save** — the AI Narrative toggle activates automatically; status shows ✅ AI ready
7. On mobile the panel closes automatically after Save
8. Run the assessment normally — AI summaries generate on the results screen

> **No API key?** That's fine. Switch to Live AI mode and run the assessment without one. The results header will show **"✦ AI Off"** and the AI sections will show a prompt to enter a key. You can add a key at any time and re-run.

### Getting API keys

| Provider | Where | Cost |
|---|---|---|
| Claude (Anthropic) | https://console.anthropic.com/ | ~$0.003 per 1,000 tokens |
| Gemini (Google) | https://aistudio.google.com/app/apikey | Free tier available |

### Key security
- Keys are **never written to the HTML file** or sent anywhere other than the AI provider's API
- Keys stored in localStorage are device-specific and browser-specific
- The **"Remember in browser"** checkbox must be explicitly ticked — opt-in only
- Use the **Clear** button to remove a saved key at any time

---

## 5. Admin bar reference

The admin bar is fixed to the bottom of every screen. It collapses to a single slim row and expands to show all settings. **On mobile, the panel auto-collapses after you select a mode or save a key.**

### Collapsed row — always visible

| Element | What it does |
|---|---|
| **⚙ Admin ▲/▼** | Tap to expand or collapse the full settings panel |
| **Demo** pill (purple when active) | Switch to Demo mode — pre-fills context form, shows Skip to Results |
| **Live AI** pill (cyan when active) | Switch to Live mode — reveals API key fields in the panel |
| Status text | Shows current mode or last action (e.g. ✅ Key saved, Live mode — enter API key to enable AI) |

### Expanded panel

| Element | What it does |
|---|---|
| AI Narrative toggle | Enables/disables AI-generated text on the results screen |
| Provider selector | Claude (Anthropic) or Gemini (Google) |
| API key field | Paste your key — stored in memory only unless Remember is ticked |
| Remember in browser | Saves key to localStorage so it persists across sessions |
| **Save** | Reads the key, activates AI, saves preferences. Collapses panel on mobile. |
| **Clear** | Removes key from localStorage and clears the input field |
| Currency selector | £ GBP / € EUR / $ USD — re-renders all cost figures immediately |

### Mobile behaviour
- Tapping **Demo** or **Live AI** pill auto-collapses the panel (mode is set, no need to keep it open)
- Tapping **Save** auto-collapses the panel (key is saved, done)
- On desktop the panel stays open so you can enter a key without reopening

---

## 6. Context screen fields

These fields shape the entire assessment: which frameworks apply, how risk is modelled, and what peer benchmarks are used. Every field has a **?** tooltip in the application.

| Field | What it does |
|---|---|
| **Organisation name** | Appears on the PDF report. No data sent externally. |
| **Contact name** | Appears on the PDF report cover. Optional. |
| **Industry sector** | Triggers sector-specific frameworks (e.g. Financial Services → DORA, PCI-DSS, FCA). Sets peer benchmark scores. |
| **Region / Jurisdiction** | Sets region-specific regulations (UK → NCSC/ICO, EU → NIS2/GDPR, US → NIST/HIPAA/CCPA). |
| **Company size** | Scales the cost-of-inaction model. Some frameworks only apply above certain sizes (e.g. DORA). |
| **Annual revenue** | Used in the actuarial cost-of-inaction formula. Stays in the browser only. |
| **Security budget (annual)** | Used by the Optimiser to filter actions that fit within your real spend capacity. |
| **Risk appetite** | Low = fix everything. Medium = critical + high gaps. High = critical only, accept residual risk. |
| **Priority certification target** | Sets the Roadmap sequence and compliance-mode objective in the Optimiser. |
| **Optimisation objective** | Default priority in the Optimiser tab. Can be changed and combined in the Optimiser. |
| **Currency** | Applies globally to all cost figures. Can also be changed from the admin bar at any time. |

---

## 7. The Optimiser — full reference

The Optimiser tab analyses all identified gaps and calculates the best order to fix them given your real-world constraints.

> The Optimiser is a constraint-aware prioritisation engine. It scores every gap against your selected objectives, filters by budget/capacity/appetite, ranks them, and shows which 6 actions to do first — along with the projected financial impact.

### Objectives — single or multi-select
Tap one or more objectives. When multiple are selected, the scoring engine averages across all selected priorities.

| Objective | Scoring logic |
|---|---|
| **📉 Reduce risk fastest** | Ranks by risk reduction score, penalised by effort level |
| **💰 Best value per spend** | Ranks by risk reduction per unit of cost — favours cheap, high-impact actions |
| **📋 Reach cert soonest** | Boosts actions that cover your target certification framework |
| **🚫 Do nothing** | Exclusive — clears all other objectives. Shows annual Cost of Inaction only. |

### The four sliders

**Annual security budget**
Sets total available spend. Low (< £20k): only low-cost controls qualify. High (> £150k): all gaps in reach. Effect hint names exactly which actions were added or removed.

**Time horizon**
Sets programme duration. Short (≤ 6 months): quick wins only, high-effort projects deprioritised. Long (≥ 18 months): phased complex projects become viable.

**Internal team capacity**
Person-days/month for remediation. Low (≤ 3 days): outsourced controls prioritised. High (≥ 12 days): complex internal projects viable.

**Risk appetite**

| Setting | What is included |
|---|---|
| Low | All gaps: critical + high + medium severity |
| Medium (default) | Critical and high gaps only. Medium deferred. |
| High | Critical gaps only. Medium and high accepted as residual risk. |

### Diff-aware effect hints
Every slider move shows what specifically changed vs the previous position — named actions added/removed/reordered, not generic text. Amber = constraint, green = improvement, grey = neutral reorder.

### Action plan badges
- **`NEW`** (cyan) — action just entered the top 6
- **`▲ 2`** / **`▼ 1`** (purple) — moved up/down in priority

### Projected impact panel
Struck-through red = current position. Green = projected after completing all 6 recommended actions. ▲/▼ delta shows exact change when a slider moves.

### Do Nothing mode
Hides the action plan, greys out sliders, shows the annual financial exposure if nothing is done. Use when presenting to leadership to make the cost-of-inaction case.

---

## 8. Understanding the results

### Results header badges
The results header always shows two status badges:

| Badge | What it shows |
|---|---|
| **⚡ Demo** (purple) | Results came from Skip to Demo — pre-filled data |
| **⚡ Quick Check** (green) | Real assessment, 16 questions (2 per domain) |
| **🔬 Deep Dive** (cyan) | Real assessment, 48 questions (full depth) |
| **✦ AI On (Claude/Gemini)** (amber) | AI narratives are active and will generate |
| **✦ AI Off** (grey) | No API key — AI sections will prompt for a key |

### Three headline scores

**CyberScore (0–100)**
Weighted average across 8 domains.

| Band | Score | Meaning |
|---|---|---|
| 🔴 Critical | 0–39 | Significant gaps. Immediate action required. |
| 🟠 Developing | 40–59 | Basic controls, inconsistently applied. Material risk. |
| 🟡 Established | 60–74 | Core programme in place. Gaps in advanced controls. |
| 🟢 Advanced | 75–89 | Strong programme. Approaching certification-ready. |
| ⭐ Leading | 90–100 | Best-in-class. Continuous improvement culture. |

**Business Risk Score (0–100)**
`(100 − CyberScore) × sector_multiplier × 0.85`. Higher = more exposed.

**Cost of Inaction (annual)**
Actuarial model: `(Asset Value × Exposure Factor × Annual Rate of Occurrence) + (Revenue × 0.02)`. Based on IBM Cost of Data Breach 2024 benchmarks.

### The 8 assessment domains

| Domain (weight) | What it covers |
|---|---|
| Identity & Access Mgmt (15%) | MFA, SSO, PAM, privileged access, directory services |
| Network Security (13%) | Firewalls, segmentation, IDS/IPS, VPN, DNS security |
| Detection & Response (14%) | SIEM, EDR, XDR, incident response, SOC capability |
| Cloud Security (12%) | CSPM, cloud IAM, DevSecOps, container security |
| Data Protection (12%) | Classification, DLP, encryption, backup, CASB |
| Supply Chain (10%) | Vendor risk, SBOM, third-party assessment |
| Governance & Policy (12%) | CISO, policies, risk register, board reporting |
| People & Awareness (12%) | Training, phishing simulation, culture, insider threat |

### Assessment depth
- **Quick Check** — 16 questions (first 2 per domain). ~15 minutes. Good for first-pass or senior leadership overview.
- **Deep Dive** — 48 questions (full domain depth). ~45 minutes. Required for certification gap analysis and board reporting.

Both modes use the same scoring model. Quick Check samples the most diagnostic questions from each domain.

---

## 9. Making changes

To make changes, create a new branch (`v1.5-dev`), copy `index.html`, make and test changes, then merge.

### Safe to change
- `DEMO_CTX` and `DEMO_ANSWERS` — update the demo company profile
- `GAP_DB` array — add/remove/edit gap entries (keep all required fields)
- `ALL_FRAMEWORKS` array — add new frameworks
- CSS custom properties (`:root` vars) — colours and fonts
- Text content in HTML — labels, descriptions, button text

### Requires care

| Component | Why |
|---|---|
| `DOMAINS` array | Question order matters — Quick Check takes first 2 per domain |
| `calculateScores()` | Domain weights must sum to 1.0 |
| `updateOptimiser()` | `_prevOptState` structure must stay in sync |
| Admin bar HTML | ID names referenced throughout JS |
| Tooltip engine | Uses `data-tt` attribute — don't use `title` alongside it |

### Key JS functions

| Function | What it does |
|---|---|
| `calculateAndRender()` | Entry point after assessment. Resets `_prevOptState` and `demoResultsLoaded`. |
| `updateOptimiser()` | Scores actions, diffs vs previous state, renders hints and action plan. |
| `toggleOptMode(m)` | Multi-select objective toggle. Do Nothing is exclusive. |
| `setAdminMode(mode)` | Switches Demo/Live. Updates pills, shows/hides API fields, auto-collapses on mobile. |
| `skipToDemo()` | Sets `demoResultsLoaded = true`, loads DEMO_CTX and DEMO_ANSWERS, calls calculateAndRender(). |
| `startQuiz()` | Clears `answers = {}` and `demoResultsLoaded = false` — always a fresh assessment. |
| `renderDemoAnswersPanel()` | Shows pre-filled Q&A grid only when `demoResultsLoaded === true`. |
| `scrollToSection(id)` | Activates the containing tab panel first, then scrolls. |
| `saveAdminKey()` | Reads key, activates AI toggle, saves to localStorage if opted in. Auto-collapses on mobile. |

---

## 10. Known limitations

| Limitation | Notes |
|---|---|
| Gap register is static | All 10 gaps show regardless of answers. Future: filter by actual weak domains. |
| Framework coverage % is estimated | Not a substitute for formal gap analysis or certification audit. |
| AI narrative requires user's own API key | No key = no AI. Gemini free tier is a good starting point. |
| History stored in localStorage | Clears if user clears browser data. No server-side persistence. |
| PDF export | Uses jsPDF. Complex layouts may not render perfectly in all browsers. |
| Mobile | Functional but optimised for desktop. Some tab labels truncate on very small screens. |
| Quick mode scoring | Uses first 2 questions per domain — ensure most diagnostic questions are listed first. |

---

## 11. Changelog

### v1.4 — 18 June 2026
- Fixed: Stray visible text banner at top of page (old comment block not wrapped in `<!-- -->`)
- Fixed: Quick Check / Deep Dive now correctly drives the quiz — demo answers were silently overwriting real answers in `startQuiz()`
- Fixed: Demo answers panel now only appears when Skip to Demo Results was used (`demoResultsLoaded` flag), not on every real assessment run in Demo admin mode
- Fixed: Begin Assessment in Live mode now clears the context form — no more stale Acme Financial Ltd data showing for real users
- New: Results header now shows assessment mode badge (⚡ Demo / ⚡ Quick Check / 🔬 Deep Dive) and AI status badge (✦ AI On / ✦ AI Off) on every results screen
- New: Admin panel auto-collapses on mobile after Demo/Live AI pill selection
- New: Admin panel auto-collapses on mobile after Save is pressed
- New: Live AI pill no longer forces the API key warning banner — switching mode is just intent; warning only shows if AI Narrative toggle is explicitly turned ON without a key
- New: Live AI status text updated to "Live mode — enter API key to enable AI" (was misleadingly "using API key" even when no key was present)

### v1.3 — 16 June 2026 (frozen baseline)
- Collapsible admin bar: always-visible Demo/Live AI mode pills in collapsed row
- Demo mode: "Skip to Results" button on welcome screen for instant demo
- Demo mode: Pre-filled answers panel on results screen showing all Q&A with maturity levels
- Fixed: Optimiser button in results header now jumps to Optimiser tab
- Fixed: API key not activating AI when pasted after toggle
- Fixed: Duplicate `id="opt-section"` on optimiser tab panel
- Fixed: `optMode` not syncing from context screen to Optimiser
- Fixed: JS syntax error — unescaped apostrophe in `haven't` string
- Fixed: `beforeAfter` and `actionList` undeclared in isNothing block
- Optimiser: Multi-select objectives, Do Nothing mode, diff-aware hints, action badges, delta indicators
- Tooltips: JS body-attached engine with touch/mobile support on all fields
- Mobile: Improved responsive CSS throughout

### v1.2 — 15 June 2026
- Initial build: 8 domains, 48 questions, 12+ frameworks, scoring engine
- Business risk score and cost-of-inaction actuarial model
- Gap register, framework heatmap, optimiser, roadmap
- AI narrative (Claude + Gemini), PDF export, assessment history
- Currency switcher: GBP / EUR / USD
