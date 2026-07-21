# CyberScore Pro — Technical & Developer Guide

**Version 1.3** · For developers, technical architects, and security engineers  
*Assumes working knowledge of HTML, CSS, and JavaScript*

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Technology Stack](#2-technology-stack)
3. [Design System](#3-design-system)
4. [Application State](#4-application-state)
5. [Screen & Navigation System](#5-screen--navigation-system)
6. [Scoring Engine — Deep Dive](#6-scoring-engine--deep-dive)
7. [Framework Matching Algorithm](#7-framework-matching-algorithm)
8. [Optimiser Algorithm](#8-optimiser-algorithm)
9. [AI Integration Layer](#9-ai-integration-layer)
10. [localStorage Persistence](#10-localstorage-persistence)
11. [History System](#11-history-system)
12. [Toast Notification System](#12-toast-notification-system)
13. [Five Eyes Framework](#13-five-eyes-framework)
20. [PDF Generation](#13-pdf-generation)
20. [Chart Rendering](#12-chart-rendering)
20. [Security Model](#13-security-model)
20. [Performance Considerations](#14-performance-considerations)
20. [Testing Strategy](#15-testing-strategy)
20. [Extension Patterns](#16-extension-patterns)
20. [Build & Deployment](#17-build--deployment)
21. [Troubleshooting](#18-troubleshooting)

---

## 1. Architecture Overview

CyberScore Pro is a **zero-dependency, single-file SPA** (Single Page Application). There is no build pipeline, no module bundler, no package manager, and no server-side code. Everything runs in the browser.

```
┌─────────────────────────────────────────────────────────┐
│                     Browser (Client)                    │
│                                                         │
│  index.html                                             │
│  ├── CSS (embedded)         ← design system             │
│  ├── HTML (embedded)        ← 9 screens, all pre-built  │
│  └── JavaScript (embedded)                              │
│      ├── State management   ← plain JS global variables │
│      ├── Scoring engine     ← pure functions, no deps   │
│      ├── Render functions   ← innerHTML injection       │
│      ├── AI caller          ← fetch() to Anthropic/Google│
│      └── PDF builder        ← jsPDF (CDN)               │
│                                                         │
│  CDN dependencies (loaded at runtime)                   │
│  ├── Chart.js 4.4.1         ← charts                    │
│  ├── jsPDF 2.5.1            ← PDF export                │
│  └── Google Fonts           ← DM Sans, DM Serif, DM Mono│
│                                                         │
│  External API calls (only when AI enabled)              │
│  ├── api.anthropic.com      ← Claude Haiku              │
│  └── generativelanguage.googleapis.com ← Gemini Flash   │
└─────────────────────────────────────────────────────────┘
```

### Design decisions

**Single file** — makes distribution trivial. Email it, put it on a USB drive, host it on GitHub Pages. No deployment complexity.

**No framework** — React, Vue, Angular would add build complexity and dependency chains for no benefit at this scale. Vanilla JS with innerHTML rendering is fast enough and far simpler to maintain.

**No backend** — all data stays in the browser. No GDPR compliance issues with data storage, no server costs, no API keys to manage server-side.

**CDN for libraries** — Chart.js and jsPDF are large (>200KB minified). Loading from CDN avoids bloating the HTML file and leverages browser caching.

---

## 2. Technology Stack

| Layer | Technology | Version | Source |
|---|---|---|---|
| Markup | HTML5 | — | Embedded |
| Styling | CSS3 with custom properties | — | Embedded |
| Logic | Vanilla JavaScript (ES2020+) | — | Embedded |
| Charts | Chart.js | 4.4.1 | cdnjs.cloudflare.com |
| PDF | jsPDF | 2.5.1 | cdnjs.cloudflare.com |
| Fonts | Google Fonts (DM family) | — | fonts.googleapis.com |
| AI — Claude | Anthropic Messages API | 2023-06-01 | api.anthropic.com |
| AI — Gemini | Google Generative Language API | v1beta | generativelanguage.googleapis.com |

### Browser compatibility

Requires ES2020 support. Tested on:
- Chrome 100+
- Firefox 100+
- Safari 15+
- Edge 100+

Not compatible with Internet Explorer (any version).

---

## 3. Design System

### CSS Custom Properties (`:root`, line ~13)

All visual tokens are defined as CSS custom properties. Override any of these to retheme the tool without touching component styles.

```css
:root {
  /* Background layers */
  --bg:   #0B0F1A;   /* Page background */
  --bg2:  #111827;   /* Card surfaces */
  --bg3:  #1a2236;   /* Nested/code surfaces */

  /* Typography */
  --ink:  #F0F4FF;   /* Primary text */
  --ink2: #A8B8D8;   /* Secondary text */
  --ink3: #6B82A8;   /* Muted/hint text */

  /* Brand accent */
  --cyan:   #00C9FF; /* Primary accent */
  --cyan-d: #0099CC; /* Darker for gradients/buttons */
  --blue:   #3B82F6; /* Secondary gradient */
  --blue-d: #1D4ED8;

  /* Semantic colours */
  --red:    #EF4444; /* Critical / danger */
  --amber:  #F59E0B; /* Warning / cost */
  --green:  #10B981; /* Success / good score */
  --purple: #8B5CF6; /* AI features / roadmap */

  /* Borders */
  --border:  rgba(255,255,255,0.08);  /* Default */
  --border2: rgba(255,255,255,0.14);  /* Emphasis */

  /* Radii */
  --radius:    12px;
  --radius-lg: 16px;
  --radius-xl: 20px;

  /* Typography stacks */
  --font:   'DM Sans', system-ui, sans-serif;
  --serif:  'DM Serif Display', Georgia, serif;
  --mono:   'DM Mono', monospace;
}
```

### Component naming convention

Classes follow a BEM-lite pattern with domain prefixes:

```
.ctx-*      Context screen components
.quiz-*     Quiz screen components
.res-*      Results screen components
.domain-*   Domain score display
.gap-*      Gap register items
.opt-*      Optimiser controls and output
.adm-*      Admin bar controls
.ai-*       AI narrative boxes
.fw-*       Framework table/chips
.rm-*       Risk matrix cells
.btn-*      Buttons
.field-*    Form fields
.sc-*       Score cards (triple scores)
.ba-*       Before/after cards
```

---

## 4. Application State

All state is held in plain JavaScript global variables declared at the top of the script block (line ~813). There is no state management library.

```javascript
let appMode = 'demo';       // 'demo' | 'live'
let aiEnabled = false;       // boolean — AI narrative toggle
let apiKey = '';             // string — runtime only, not persisted to file
let apiProvider = 'anthropic'; // 'anthropic' | 'gemini'
let currency = 'GBP';       // 'GBP' | 'EUR' | 'USD'
let assessMode = 'quick';   // 'quick' | 'deep'
let ctx = {};               // object — context screen values (org, sector, etc.)
let answers = {};           // object — domainId → [0..4] per question
let scores = {};            // object — domainId → 0..100
let overallCyber = 0;       // number — weighted CyberScore
let overallRisk = 0;        // number — risk exposure score
let costOfInaction = 0;     // number — ALE in GBP
let applicableFrameworks = []; // array — filtered from ALL_FRAMEWORKS
let currentDomainIdx = 0;   // number — current domain in quiz
let optMode = 'risk';       // 'risk' | 'cost' | 'compliance'

// Chart instances (held for destroy-before-redraw)
let radarChart, barChart;
```

### State flow

```
appMode / aiEnabled / apiKey / currency     ← set by admin bar
assessMode                                  ← set by welcome screen
ctx                                         ← set by context screen
answers                                     ← set by quiz screen
scores / overallCyber / overallRisk
  / costOfInaction                          ← calculated by calculateScores()
applicableFrameworks                        ← set by updateFrameworks()
optMode                                     ← set by optimiser tab
```

There is no reactive binding — when state changes, the relevant render function must be called manually. `renderResults()` calls all render sub-functions in sequence and is the main entry point for the results screen.

---

## 5. Screen & Navigation System

### Screen architecture

All screens are `<div class="screen">` elements that are hidden by default (`display:none`). The active screen has `.active` added, which sets `display:block`.

```javascript
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo(0, 0);
}
```

### Screen IDs

| ID | Screen |
|---|---|
| `screen-welcome` | Landing / mode selection |
| `screen-context` | Organisation profile form |
| `screen-quiz` | Domain question renderer |
| `screen-results` | Results with tab navigation |

### Tab system (within results)

Tabs within the results screen use a similar pattern with `.tab-panel` divs and `.tab-btn` buttons:

```javascript
function switchTab(tab) {
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + tab).classList.add('active');
  event.target.classList.add('active');
}
```

Tab panel IDs: `tab-domains`, `tab-risk`, `tab-cost`, `tab-frameworks`, `tab-gaps`, `tab-optimiser`, `tab-roadmap`.

---

## 6. Scoring Engine — Deep Dive

### Domain score calculation (`calculateScores()`, line ~1152)

```javascript
DOMAINS.forEach(d => {
  const qs = getQuestionsForDomain(d);       // 2 (quick) or 5 (deep)
  const domAnswers = answers[d.id] || [];
  let total = 0;
  const max = qs.length * 4;                 // max score = num_questions × 4
  qs.forEach((_, qi) => {
    total += (domAnswers[qi] ?? 0);           // unanswered = 0
  });
  scores[d.id] = Math.round((total / max) * 100);
});
```

Each answer is 0–4 (maps to the 5 option buttons). Maximum score per question is 4. Domain score = (sum of answers) / (number of questions × 4) × 100.

Quick mode uses `d.questions.slice(0, 2)` — the first 2 questions in each domain's array. This means question ordering matters: put the most diagnostic questions first.

### Overall CyberScore calculation

```javascript
overallCyber = Math.round(
  Object.entries(scores).reduce((acc, [id, v]) => {
    const d = DOMAINS.find(d2 => d2.id === id);
    return acc + (v * (d?.weight || 0.125));
  }, 0)
);
```

Weighted average of domain scores. Weights are defined per domain in the `DOMAINS` array and must sum to 1.0.

**Current weights:**

| Domain | Weight | Rationale |
|---|---|---|
| IAM | 0.15 | MFA alone blocks ~99% of automated attacks |
| Detection | 0.15 | Dwell time drives total breach cost |
| Network | 0.12 | Perimeter remains foundational |
| Cloud | 0.12 | Fastest-growing attack surface |
| Data | 0.12 | Regulatory and reputational driver |
| Governance | 0.12 | Required by ISO 27001, DORA, NIS2 |
| Awareness | 0.12 | #1 initial access vector (phishing) |
| Supply Chain | 0.10 | Highest-growth attack vector |

### Risk Score calculation

```javascript
const sectorMultiplier = {
  'Financial Services': 1.4,
  'Healthcare & Life Sciences': 1.3,
  'Technology & SaaS': 1.25,
  'Energy & Utilities': 1.35,
  'Public Sector & Government': 1.2,
  'Retail & E-commerce': 1.15
}[ctx.sector] || 1.1;

overallRisk = Math.min(100,
  Math.round((100 - overallCyber) * sectorMultiplier * 0.85)
);
```

Sector multipliers reflect published breach frequency and severity data from IBM CODB 2024 and Verizon DBIR 2024. The `0.85` factor caps risk growth to avoid artificially high scores for borderline cases.

### FAIR-based cost model

```javascript
const sle = rev * 0.18;          // Single Loss Expectancy
const aro = (overallRisk / 100) * 0.7;  // Annual Rate of Occurrence
costOfInaction = Math.round(sle * aro + rev * 0.02);
```

**Calibration constants:**
- `0.18` — 18% of revenue as SLE. IBM CODB 2024 UK average breach cost as % of revenue for mid-market firms.
- `0.7` — ARO ceiling. Ensures max breach probability doesn't exceed 70% even at Risk Score 100.
- `0.02` — 2% ongoing compliance cost. Covers audit friction, insurance, manual processes.

To recalibrate for a different market or dataset, adjust these three constants. The `0.18` is most sensitive — a 5-point change materially affects all cost outputs.

---

## 7. Framework Matching Algorithm

```javascript
applicableFrameworks = ALL_FRAMEWORKS.filter(f => {
  const regionOk = f.regions === 'all' || f.regions.includes(region);
  const sectorOk = f.sectors === 'all' || f.sectors.includes(sector);
  const sizeOk   = f.sizes === 'all' || !size || f.sizes.includes(size);
  return regionOk && sectorOk && sizeOk;
});
```

Three-way AND filter. A framework appears if all three conditions are met. `'all'` is a wildcard that matches any value.

### Framework coverage calculation

```javascript
const domScores = f.controls.map(c => scores[c] || 0);
const avg = Math.round(domScores.reduce((a, b) => a + b, 0) / domScores.length);
const coverage = Math.round(avg * f.weight);
```

Coverage % = average domain score across the framework's mapped control domains × the framework's weight multiplier. Weight is a complexity/breadth factor — ISO 27001 (weight 1.0) requires deeper coverage than Cyber Essentials (weight 0.8).

**Thresholds:**
- ≥70% → Ready (green chip)
- 45–69% → Partial (amber chip)
- <45% → Significant gaps (red chip)

---

## 8. Optimiser Algorithm

The optimiser ranks `GAP_DB` items by a scoring function that varies by objective mode.

```javascript
const actions = GAP_DB.map(g => {
  let score = 0;

  if (optMode === 'risk') {
    // Prioritise highest risk reduction, penalise high effort
    score = g.riskReduction * 3
          - (g.effort === 'High' ? 30 : g.effort === 'Medium' ? 15 : 0);

  } else if (optMode === 'cost') {
    // Prioritise best risk-£-per-implementation-£
    score = g.riskReduction * 50
          / (g.effort === 'High' ? 3 : g.effort === 'Medium' ? 1.5 : 1);

  } else {
    // Compliance: boost actions covering the target cert, bias to critical
    score = (g.frameworks.includes(ctx.certTarget) || g.severity === 'critical' ? 50 : 0)
          + g.riskReduction;
  }

  return { ...g, _score: score };
}).sort((a, b) => b._score - a._score);
```

The `_score` property is only used internally for sorting and is not displayed to the user.

### Before/After projection

```javascript
const topActions = actions.slice(0, 6);
const totalRiskReduction = topActions.reduce((a, g) => a + g.riskReduction, 0);
const newCyber = Math.min(100, overallCyber + Math.round(totalRiskReduction * 0.7));
const newRisk  = Math.max(0,   overallRisk  - Math.round(totalRiskReduction));
const newCost  = Math.round(costOfInaction * ((100 - totalRiskReduction * 0.8) / 100));
```

The `0.7` and `0.8` factors model diminishing returns — implementing controls improves the score but not by the full theoretical maximum, because some risk sources are outside control scope.

### ROI per action

```javascript
const saved = Math.round(
  costOfInaction * CURR_RATES[currency] * (g.riskReduction / 100) * 0.8
);
```

Annualised risk reduction in currency. The `0.8` applies the same diminishing returns factor.

---

## 9. AI Integration Layer

### Core caller — `runAI(system, user)` (line ~1609)

Single unified function supporting two providers. Returns `Promise<string>`.

```javascript
async function runAI(system, user) {
  if (!apiKey) throw new Error('No API key');

  if (apiProvider === 'gemini') {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/`
              + `gemini-1.5-flash:generateContent?key=${apiKey}`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{ parts: [{ text: `${system}\n\n${user}` }] }],
        generationConfig: { temperature: 0.6, maxOutputTokens: 1000 }
      })
    });
    if (!res.ok) { const e = await res.json(); throw new Error(e.error?.message); }
    const data = await res.json();
    return data.candidates?.[0]?.content?.parts?.[0]?.text || '';

  } else { // anthropic
    const res = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'anthropic-dangerous-allow-browser': 'true'  // required for browser calls
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 1000,
        system,
        messages: [{ role: 'user', content: user }]
      })
    });
    if (!res.ok) { const e = await res.json(); throw new Error(e.error?.message); }
    const data = await res.json();
    return data.content?.map(c => c.text || '').join('') || '';
  }
}
```

### AI function signatures

```javascript
generateAISummary()        // no args — uses global scores + ctx
generateGapInsight(i)      // i = index into GAP_DB array
generateBoardReport()      // no args — uses global scores + ctx + GAP_DB
```

### Prompt engineering patterns

All prompts follow the same structure:

```
System: Role definition + output constraints (word count, format, no bullet points, etc.)
User:   Specific data injection (scores, sector, region, top gaps)
```

**Gap insight prompt is deliberately constrained to 40 words** to keep it scannable and avoid API cost accumulation when rendering 10 gaps simultaneously.

### Error handling pattern

All AI functions catch errors and render them inline to the target element rather than using `alert()`:

```javascript
try {
  const text = await runAI(system, prompt);
  el.innerHTML = '<div class="ai-content">' + text + '</div>';
} catch(e) {
  el.innerHTML = `<div style="color:var(--red);font-size:12px">AI error: ${e.message}</div>`;
}
```

### Upgrading to a better model

To switch Claude model, change line ~1632:
```javascript
model: 'claude-haiku-4-5-20251001'
// → 'claude-sonnet-4-6'  (more capable, ~15× more expensive)
// → 'claude-opus-4-6'    (most capable, ~75× more expensive)
```

To switch Gemini model, change line ~1612:
```javascript
'gemini-1.5-flash'
// → 'gemini-1.5-pro'     (more capable, consumes free tier faster)
```

---

## 10. localStorage Persistence

### Keys

```javascript
const LS_KEY_API  = 'csp_api_key';    // API key (opt-in only)
const LS_KEY_PROV = 'csp_provider';   // 'anthropic' | 'gemini'
const LS_KEY_CURR = 'csp_currency';   // 'GBP' | 'EUR' | 'USD'
const LS_KEY_MODE = 'csp_adm_mode';   // 'demo' | 'live'
```

All keys use the `csp_` prefix to avoid collisions with other tools that may be opened in the same origin.

### Opt-in key persistence

The API key is only written to localStorage if `#adm-remember` is checked. This is a deliberate security decision — storing a key without explicit consent violates user expectations.

```javascript
function savePrefs() {
  if (document.getElementById('adm-remember')?.checked) {
    localStorage.setItem(LS_KEY_API, apiKey);
  } else {
    localStorage.removeItem(LS_KEY_API);  // clear if unchecked
  }
  // Other prefs always saved
  localStorage.setItem(LS_KEY_PROV, apiProvider);
  localStorage.setItem(LS_KEY_CURR, currency);
  localStorage.setItem(LS_KEY_MODE, appMode);
}
```

### Loading on startup

`loadPrefs()` is called in `DOMContentLoaded`. If a saved key is found, `aiEnabled` is set to `true` and the AI toggle is checked automatically.

### localStorage availability

localStorage can be blocked in private/incognito mode in some browsers, and in certain iframe contexts. The implementation wraps all calls in `try/catch` — if localStorage is unavailable, the tool still works, keys just won't persist.

---


## 11. History System

### localStorage schema

All history is stored under a single key `csp_history` as a JSON array of assessment record objects, newest first. Maximum 50 records; older records are spliced on save.

```javascript
// Each record shape
{
  id:              string,   // 'asmnt_{timestamp}_{random4}' — unique identifier
  date:            string,   // ISO 8601 — e.g. '2026-06-15T14:32:00.000Z'
  org:             string,   // organisation name
  sector:          string,
  region:          string,
  size:            string,   // 'micro'|'small'|'sme'|'mid'|'large'|'enterprise'
  revenue:         number,
  certTarget:      string,
  assessMode:      string,   // 'quick'|'deep'
  currency:        string,   // 'GBP'|'EUR'|'USD'
  overallCyber:    number,   // 0–100
  overallRisk:     number,   // 0–100
  costOfInaction:  number,   // in GBP regardless of display currency
  scores:          object,   // { iam: 72, network: 54, ... }
  ctx:             object,   // full ctx object snapshot
  answers:         object    // { iam: [3,2,2,1,3], network: [...], ... }
}
```

### Core history functions (line ~1828)

```javascript
getHistory()                        // → array of records from localStorage
setHistory(arr)                     // writes array to localStorage; alerts if full
saveAssessmentToHistory()           // called from calculateAndRender() — auto-saves
restoreAssessment(id)               // restores global state + re-renders results
deleteHistoryRecord(id, e)          // removes one record, re-renders tab
clearAllHistory()                   // removes all, re-renders tab
exportAllHistory()                  // triggers .json download of entire array
exportSingleAssessment(id, e)       // triggers .json download of one record
importHistory(event)                // file input handler — merges, dedupes by id
handleHistoryDrop(e)                // drag-and-drop handler — same logic as import
compareWithPrevious(id, e)          // builds comparison modal DOM, appends to body
renderHistoryTab()                  // renders search, trend chart, delta strip, cards
updateFrameworksSilent()            // re-runs framework matching without updating UI
switchTabById(tab)                  // programmatic tab switch (bypasses event.target)
```

### Deduplication logic

On save, records within 60 seconds from the same org are considered duplicates and the old one is removed before inserting the new one. This prevents double-saves from rapid rerenders (e.g. currency change triggering a re-render chain):

```javascript
const filtered = hist.filter(r =>
  !(r.org === record.org && Math.abs(new Date(r.date) - now) < 60000)
);
```

On import, deduplication is by `id` — records whose `id` already exists in localStorage are skipped entirely.

### Comparison modal

`compareWithPrevious()` builds a modal entirely from DOM string injection and appends it to `document.body`. It closes on backdrop click or the Close button. It does not use `position:fixed` on any inner element — the outer wrapper is fixed and the inner content is a normal-flow div to avoid iframe height collapse issues.

The modal accesses `DOMAINS` (global) to map domain IDs to display names and icons.

### Trend chart

Uses a third Chart.js instance (`trendChart`) alongside `radarChart` and `barChart`. It is destroyed and recreated each time `renderHistoryTab()` is called, using the same destroy-before-recreate pattern. Only renders when 2+ records are present (after search filtering).

The chart uses at most 12 records (`.slice(0,12).reverse()`) to keep the x-axis readable. For orgs with many assessments, the search filter is the natural way to zoom into a subset.

### restoreAssessment() flow

```
restoreAssessment(id)
  ↓ finds record in localStorage
  ↓ assigns to globals: ctx, scores, answers, overallCyber, overallRisk,
                        costOfInaction, assessMode, currency
  ↓ calls updateFrameworksSilent() to rebuild applicableFrameworks
  ↓ calls showScreen('screen-results')
  ↓ calls renderResults() — full re-render of all tabs
  ↓ calls switchTabById('domains') — lands on Domains tab
  ↓ appends purple 'Restored from history' badge to context banner
```

Note: `restoreAssessment()` does NOT call `calculateScores()` — scores are taken directly from the saved record, not recalculated from answers. This ensures what you see matches what was saved at the time, even if the scoring formula has changed.

### Storage size management

Each record is approximately 5–10KB serialised. At 50 records, that is 250–500KB — well within the 5MB localStorage limit. The `setHistory()` function wraps the write in try/catch and alerts the user if localStorage throws a QuotaExceededError.

For environments where localStorage may be unavailable (private mode, sandboxed iframes), all history functions fail silently — `getHistory()` returns `[]`, saves are no-ops, and the History tab shows the empty state.

---


## 12. Toast Notification System

### Architecture (line ~2181)

The toast system is a lightweight, fully self-contained notification engine with no external dependencies. It manages its own DOM (`#toast-container`), animation lifecycle, duplicate prevention, and smart content logic.

```
#toast-container          ← fixed position, bottom-right, z-index 9000
  └── .toast.t-{type}     ← each notification (auto-appended, auto-removed)
      ├── .toast-icon      ← emoji per type
      ├── .toast-body      ← title + message + optional action link
      ├── .toast-close     ← ✕ button
      └── .toast-progress  ← animated bottom bar showing time remaining
```

### Core function — `showToast(opts)`

```javascript
showToast({
  type:     'success',   // 'success' | 'info' | 'warning' | 'danger'
  title:    'Title',     // bold heading (optional)
  msg:      'Message',   // body text
  action:   'Click →',   // underlined action link text (optional)
  actionFn: ()=>{},      // function called on action click (optional)
  duration: 6000,        // ms before auto-dismiss (default 6000)
  id:       'unique-id'  // prevents duplicate toasts with same id (optional)
})
```

### Duplicate prevention

The `_activeToastIds` Set tracks which `id` values have active toasts. `showToast()` returns early if the same `id` is already visible. On dismiss (auto or manual), the id is removed from the Set so the same toast can appear again if re-triggered.

This prevents the save toast from stacking if `saveAssessmentToHistory()` is somehow called twice in quick succession.

### Animation

Two CSS `@keyframes` handle enter and exit:
- `toastIn` — slides in from x=+60px, fades from opacity 0 to 1, with overshoot spring (`cubic-bezier(.34,1.56,.64,1)`)
- `toastOut` — slides out to x=+60px, fades to opacity 0 (300ms, applied by adding `.removing` class)

The `.toast-progress` bar animates from `width:100%` to `width:0%` using a linear keyframe. Duration matches the `duration` option via inline `animation-duration` style.

### Smart save logic — `toastFirstSave()`

Two localStorage flags drive the three-state logic:

```javascript
const LS_KEY_FIRST_SAVE   = 'csp_first_save_done';   // set on first save
const LS_KEY_FIRST_EXPORT = 'csp_first_export_done';  // set on first export
```

| `FIRST_SAVE` | `FIRST_EXPORT` | Toast shown |
|---|---|---|
| not set | — | Full explainer (9s) with History tab action link |
| set | not set | Export nudge (7s) with History tab action link |
| set | set | Brief confirmation (4s) with record count |
| localStorage throws | — | Amber warning + PDF download action (10s) |

The export flag is set inside `toastExportSuccess()`, which is called by both `exportAllHistory()` and `exportSingleAssessment()`. Once either is called, the nudge stops appearing.

### Timing — why 800ms delay on save toast

`toastFirstSave()` is called via `setTimeout(..., 800)` inside `saveAssessmentToHistory()`. This ensures the results screen has finished rendering before the toast appears. Without the delay, the toast would appear during the screen transition animation, which looks jarring.

### Wiring map

| Function | Toast called | When |
|---|---|---|
| `saveAssessmentToHistory()` | `toastFirstSave()` | 800ms after save completes |
| `exportAllHistory()` | `toastExportSuccess()` or `toastExportEmpty()` | Immediately after download triggered |
| `exportSingleAssessment()` | `toastExportSuccess()` | Immediately after download triggered |
| `importHistory()` | `toastImportSuccess()` or `toastImportError()` | After FileReader completes |
| `handleHistoryDrop()` | `toastImportSuccess()` or `toastImportError()` | After FileReader completes |
| `deleteHistoryRecord()` | `toastDeleteRecord()` | After deletion confirmed and re-render |
| `clearAllHistory()` | `toastClearAll()` or inline `showToast()` | After clear confirmed |

### Adding a new toast

Call `showToast()` from anywhere in the app:

```javascript
// Simple notification
showToast({ type:'success', title:'Done', msg:'Your action completed.', duration:5000 });

// With action link
showToast({
  type:'warning',
  title:'Unsaved changes',
  msg:'Your session will expire. Export now to keep your data.',
  action:'Export →',
  actionFn:()=>exportAllHistory(),
  duration:10000,
  id:'session-expiry'  // prevents duplicate if triggered multiple times
});
```

### Extending the system for Phase 2 (Supabase cloud)

When cloud save is added, replace `toastFirstSave()` with a cloud-aware version:
- If cloud save succeeds → green "Saved to cloud" toast (no export nudge needed)
- If cloud save fails → amber "Saved locally only" toast with retry action
- If offline → amber "Saved locally — will sync when online" toast

---


## 13. Five Eyes Framework

### Data structure — `FE_PRINCIPLES` array

Each principle object defines how it maps to domain scores and which AI governance question (if any) boosts its score in Deep Dive mode:

```javascript
{
  id:           'human-oversight',
  name:         'Human Oversight of AI',
  icon:         '👤',
  desc:         'Meaningful human control over AI-driven security decisions',
  source:       'May 2026 Agentic AI guidance — Behavioural risk class',
  domains:      ['governance','detection'],  // domain IDs averaged for base score
  aiQuestionIdx: 2,   // index into governance AI questions array (0–4)
                      // null = no AI question component
  weight:       0.15  // weight in overall Five Eyes score (all weights sum to 1.0)
}
```

### Scoring — `calcFiveEyesScore()`

```javascript
// For each principle:
const domAvg = average(p.domains.map(id => scores[id]));

// If principle has an AI question and assessMode === 'deep':
const aiAnswer = answers['governance'][5 + p.aiQuestionIdx]; // 5 = offset past core questions
const aiScore  = (aiAnswer / 4) * 100;
const combined = aiScore !== null
  ? Math.round(domAvg * 0.7 + aiScore * 0.3)  // 70% domain, 30% AI question
  : Math.round(domAvg);                          // domain only (quick mode)

// Overall Five Eyes score:
const overall = sum(principleScores[i].score * FE_PRINCIPLES[i].weight)
```

The AI questions in governance start at index 5 (after the 5 standard governance questions). In quick mode, `getQuestionsForDomain()` filters out `aiOnly:true` questions, so they are never rendered or answered — `aiQuestionIdx` then returns `undefined` and the scoring falls back to domain-only.

### Five Eyes framework entry in `ALL_FRAMEWORKS`

```javascript
{
  id: 'FIVEYES',
  name: 'Five Eyes AI & Cyber Resilience',
  sub: 'Joint statement 22 Jun 2026 + Agentic AI guidance May 2026',
  tag: 'fiveyes',       // distinct tag — not 'regulatory', 'certification', or 'international'
  regions: 'all',       // global — applies to all organisations
  sectors: 'all',
  sizes: 'all',
  controls: ['iam','network','detection','cloud','data','supplychain','governance','awareness'],
  weight: 1.0,
  fiveEyes: true        // flag used by renderFrameworks() for row styling
}
```

The `fiveEyes: true` flag is used in `renderFrameworks()` to apply `.fw-fe-row` class (purple left border) and inject the NEW badge.

### `renderFiveEyes()` flow

```
renderFiveEyes()
  ↓ checks localStorage for 'csp_fe_alert_dismissed' → hides banner if set
  ↓ removes existing #fe-panel-wrap if re-rendering
  ↓ calls calcFiveEyesScore() → {overall, principleScores[]}
  ↓ calls getFEBand(overall) → {label, color}
  ↓ builds innerHTML for:
     - .fe-panel (score hero + 7 principle bars + source links)
     - .fe-ai-box (AI analysis placeholder or loading state)
  ↓ inserts after the framework table section card
  ↓ if aiEnabled && apiKey → calls generateFEAnalysis() after 1200ms delay
```

### `generateFEAnalysis()` — AI prompt structure

System: CISO briefing expert, direct, two paragraphs, max 140 words.

User prompt includes: org name, sector, region, Five Eyes overall score, weakest principles (below 60%), CyberScore.

Para 1: what the June 22 statement means for this specific sector — includes the "months not years" urgency.
Para 2: top 2 specific actions to improve Five Eyes alignment given their weakest principles.

On success: fires `'fe-ai-ready'` toast pointing user to Frameworks tab.

### Alert banner — `dismissFEAlert()`

The banner is HTML-embedded in the results screen. Dismissal sets `'csp_fe_alert_dismissed'` in localStorage. On subsequent `renderFiveEyes()` calls, if the flag exists, the banner is hidden. The banner auto-hides without clearing the flag on page reload — it only returns if localStorage is cleared.

### Toast triggers added in v1.3

| Trigger | ID | Type | Timing |
|---|---|---|---|
| Results load (always) | `fe-new-statement` | info | +2000ms after render |
| AI enabled on results load | `fe-ai-generating` | info | +1400ms |
| AI analysis complete | `fe-ai-ready` | info | On completion |

### `[Five Eyes]` AI questions — governance domain, indices 5–9

| Index | Question summary | Principle mapped |
|---|---|---|
| 5 | AI security & procurement policy | Secure by Design |
| 6 | AI systems auditable & explainable? | Transparency & Accountability |
| 7 | Human override capability? | Human Oversight of AI |
| 8 | AI agents over-permissioned? | Least Privilege for AI |
| 9 | Tested fallback if AI fails? | Resilience over Reliance |

All five are `aiOnly:true` — filtered out by `getQuestionsForDomain()` in quick mode.

### Adding a new Five Eyes principle

1. Add entry to `FE_PRINCIPLES` array — ensure weights still sum to 1.0
2. If a new AI question is needed, add it to the governance `questions` array with `aiOnly:true`
3. Set `aiQuestionIdx` to the new question's position within the AI question block (0-indexed from position 5)
4. No other changes needed — `calcFiveEyesScore()` and `renderFiveEyes()` iterate `FE_PRINCIPLES` dynamically

### Sources

- https://www.cyber.gov.au/about-us/view-all-content/news/five-eyes-cyber-security-agencies-statement (22 Jun 2026)
- https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services (May 2026)
- https://www.ncsc.gov.uk/collection/secure-by-design (2023/24)

---

## 14. PDF Generation

Uses jsPDF in UMD format loaded from CDN. The PDF is generated entirely client-side — no server round-trip.

```javascript
function downloadPDF() {
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF({ orientation: 'portrait', unit: 'mm', format: 'a4' });
  // ...
  doc.save(`${filename}.pdf`);
}
```

### Coordinate system

jsPDF uses mm coordinates from the top-left corner. A4 = 210mm × 297mm. Left margin (`M`) = 15mm. Content width (`CW`) = 210 - 15×2 = 180mm.

### Adding charts to PDF (v1.1 planned)

Chart.js renders to a `<canvas>` element. To include charts in the PDF:

```javascript
// Get the canvas as a base64 image
const canvas = document.getElementById('radar-chart');
const imgData = canvas.toDataURL('image/png');
doc.addImage(imgData, 'PNG', x, y, width, height);
```

This must be called before `doc.save()` and after the chart has rendered. The chart must be visible (not in a hidden tab) at the time of capture — trigger `switchTab('domains')` before capturing, then `doc.save()`.

---

## 14. Chart Rendering

Uses Chart.js 4.4.1. Two chart instances: `radarChart` and `barChart`.

Both are destroyed before re-rendering to prevent canvas context conflicts:

```javascript
if (radarChart) radarChart.destroy();
if (barChart) barChart.destroy();
```

### Radar chart configuration

```javascript
{
  type: 'radar',
  data: {
    labels: DOMAINS.map(d => d.name.split(' ')[0] + '…'), // truncate for readability
    datasets: [
      { label: 'Your Score',   data: domainScores, ... },
      { label: 'Sector Peer',  data: Array(8).fill(peerScore), borderDash: [4,4], ... }
    ]
  },
  options: {
    scales: {
      r: {
        suggestedMin: 0,
        suggestedMax: 100,
        // dark theme colours for grid/labels
      }
    }
  }
}
```

### Dynamic bar colours

Bar colours in the bar chart are set per-data-point based on score thresholds:

```javascript
backgroundColor: data.map(v =>
  v >= 70 ? 'rgba(16,185,129,0.7)'  // green
: v >= 45 ? 'rgba(245,158,11,0.7)'  // amber
:           'rgba(239,68,68,0.7)'   // red
)
```

---

## 15. Security Model

### Threat model

| Threat | Mitigation |
|---|---|
| API key exposure in source code | Key is runtime-only, never in HTML |
| API key exposure via Git | `.gitignore` excludes `.env` files; key is not in any file |
| API key in browser history | Password input field (`type="password"`) |
| API key in localStorage (if remembered) | Opt-in only; `clearSavedKey()` removes it |
| XSS via AI response | AI responses injected as `innerHTML` — a known risk. Mitigated by trusted AI provider and absence of user-controlled data in prompts |
| Sensitive assessment data leakage | All data in browser memory. No server-side storage. Tab close = data gone |
| CDN supply chain attack | Pin CDN URLs to specific versions (currently done: Chart.js 4.4.1, jsPDF 2.5.1) |

### innerHTML injection

The tool uses `innerHTML` extensively for rendering. This is intentional for performance — `createElement` at this scale would add complexity for minimal gain. The XSS risk is low because:
1. No user-supplied text is injected into innerHTML without processing
2. AI provider responses are the only external text injected — they come from a controlled API, not from other users
3. There is no multi-user session or persistent storage of user input

If embedding this tool in a context where XSS is a higher concern (e.g. an enterprise intranet with multiple users sharing a session), replace innerHTML injection with DOM creation in `renderGapRegister()` and the AI content elements.

### Content Security Policy

If serving from a web server, add these headers:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'unsafe-inline' cdnjs.cloudflare.com;
  style-src 'self' 'unsafe-inline' fonts.googleapis.com;
  font-src fonts.gstatic.com;
  connect-src api.anthropic.com generativelanguage.googleapis.com;
  img-src 'self' data:;
```

Note: `'unsafe-inline'` is required because all JS and CSS is inline in the HTML file. Refactoring to external files would allow removal of this directive.

---

## 16. Performance Considerations

### Initial load time

On a standard broadband connection:
- HTML file: ~130KB — instant
- Chart.js: ~200KB — cached after first load
- jsPDF: ~250KB — cached after first load
- Google Fonts: ~50KB — cached after first load

Total cold load: ~630KB. Subsequent loads (CDN cached): ~130KB.

### Render performance

All `render*()` functions use `innerHTML` assignment on a single container element. This triggers one reflow per function call. At the current data scale (8 domains, 10 gaps, 12 frameworks), this is imperceptible.

If `GAP_DB` grows to 50+ items, consider using `DocumentFragment` or virtual rendering in `renderGapRegister()`.

### Chart rendering

Chart.js canvas rendering is synchronous and takes ~10–30ms per chart. Two charts render on `renderCharts()` — both are destroyed and recreated on `renderResults()`, which is called on currency change. If currency switching causes a perceptible flash, debounce `setCurrency()` with a 200ms delay.

### AI call latency

- Claude Haiku: ~800ms–2s per call
- Gemini 1.5 Flash: ~600ms–1.5s per call

Gap insights are fired individually (one `fetch()` per gap). With 10 gaps, this generates 10 parallel API calls. Most providers rate-limit concurrent requests — if gaps show errors after ~5, implement a sequential queue with 200ms delay between calls.

---

## 17. Testing Strategy

There is no automated test suite in v1.1. Recommended approach for future development:

### Unit tests (recommended: Vitest or Jest)

Key functions to test:

```javascript
// Scoring
calculateScores()        // test with all-zero, all-four, mixed answers
fmtCurr()                // test with each currency + edge cases (0, 1M+)

// Framework matching
updateFrameworks()       // test each region/sector/size combination

// Optimiser
updateOptimiser()        // test all three modes, edge-case budgets (0, 500000)

// FAIR calculation
// inline in calculateScores() — extract to a pure function for testing
```

### Integration tests (recommended: Playwright or Cypress)

Test the full user journey:
1. Welcome → select mode → click Begin
2. Fill context form → click Start Assessment
3. Answer all domains → click See Results
4. Verify three scores are rendered
5. Switch each tab — verify content renders
6. Optimiser sliders — verify before/after updates
7. PDF export — verify file download triggered

### Demo mode smoke test

The fastest regression test: switch to Demo mode, click through the full journey in under 2 minutes. If the results screen renders with three scores and seven populated tabs, the core engine is working.

---

## 18. Extension Patterns

### Adding a new screen

1. Add `<div class="screen" id="screen-newname">` to the HTML
2. Add CSS for the screen if needed (follow existing screen naming patterns)
3. Call `showScreen('screen-newname')` from the appropriate navigation function

### Adding a new results tab

1. Add a `<button class="tab-btn" onclick="switchTab('newtab')">` to `.tab-strip`
2. Add `<div class="tab-panel" id="tab-newtab">` inside `.res-body`
3. Add a render function `renderNewTab()` and call it from `renderResults()`

### Adding a new AI feature

1. Write a new `async function generateX()` following the existing pattern
2. Add a placeholder element in the HTML: `<div id="ai-x-content">...</div>`
3. Call `runAI(system, prompt)` and inject the result
4. Add error handling — catch and display inline
5. Call `generateX()` from `renderResults()` if it should auto-generate, or wire to a button

### Extracting to separate files (if single-file becomes unwieldy)

Recommended split for v2.0:

```
index.html          ← HTML structure + CDN imports only
css/style.css       ← all CSS
js/data.js          ← DOMAINS, ALL_FRAMEWORKS, GAP_DB, DEMO_*
js/scoring.js       ← calculateScores(), FAIR model
js/render.js        ← all render* functions
js/ai.js            ← runAI(), generateAISummary(), etc.
js/pdf.js           ← downloadPDF()
js/app.js           ← state, navigation, admin bar, localStorage, init
```

---

## 19. Build & Deployment

### No build required (current)

```bash
# To "build": just open the file
open index.html

# To deploy to GitHub Pages:
git init
git add index.html README.md HANDOVER.md USER_GUIDE.md QUICK_REFERENCE.md TECHNICAL_GUIDE.md .gitignore
git commit -m "feat: CyberScore Pro v1.1"
git remote add origin https://github.com/username/repo.git
git push -u origin main
# Then enable Pages in repo Settings → Pages → Deploy from branch → main → / (root)
```

### Git tagging convention

```bash
git tag -a v1.1 -m "Initial frozen release"
git push origin v1.1
```

### Netlify deployment (recommended for production)

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy from repo root
netlify deploy --prod --dir .
```

Or drag the folder to app.netlify.com/drop for a one-click deploy.

### Environment-specific API key proxy (production option)

For enterprise deployments where you do not want end-users to supply their own keys, create a Netlify Function as a proxy:

```javascript
// netlify/functions/ai-proxy.js
exports.handler = async (event) => {
  const { system, user, provider } = JSON.parse(event.body);
  const apiKey = process.env.AI_API_KEY; // set in Netlify environment variables

  // Call the appropriate AI provider
  // Return the response
};
```

Update `runAI()` in index.html to call `/.netlify/functions/ai-proxy` instead of the provider directly. The key never leaves the server.

---

## 20. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Charts don't render | Chart.js CDN failed to load | Check network; download Chart.js locally and reference `./chart.min.js` |
| PDF download fails | jsPDF CDN failed | Same as above for jsPDF |
| Fonts show as system default | Google Fonts CDN blocked | Add `@font-face` declarations with locally hosted font files |
| AI errors: "No API key" | Key not saved | Admin bar → Live AI → paste key → Save |
| AI errors: 401 Unauthorized | Wrong key or expired key | Regenerate key at provider console |
| AI errors: 429 Too Many Requests | Rate limit hit | Wait 60 seconds; consider upgrading API tier |
| AI errors: CORS | Browser blocking direct API call | Ensure `anthropic-dangerous-allow-browser: true` header is set for Claude |
| Scores show as 0 | Demo mode with unanswered questions | Ensure `DEMO_ANSWERS` covers all domains with correct format |
| localStorage not persisting | Private/incognito mode | Expected behaviour — keys won't persist in private mode |
| Results flash on currency change | Charts destroy/recreate | Debounce `setCurrency()` with 200ms delay |
| Tab content empty | `switchTab()` called before `renderResults()` | Ensure navigation order: `calculateAndRender()` → `showScreen('screen-results')` → tab works |
| Toast not appearing | localStorage blocked in private mode | Expected — save toast falls back to "not saved" amber warning automatically. |
| Toast appears multiple times | `id` not set on `showToast()` call | Add a unique `id` string to prevent duplicates. |
| Five Eyes panel missing | `renderFiveEyes()` not called | Check it is called inside `renderResults()` after `renderCharts()`. |
| Five Eyes score seems wrong | AI questions not answered (quick mode) | Expected — AI questions only available in Deep Dive. Score uses domain scores only in quick mode. |
| Alert banner reappears after dismiss | localStorage cleared | Expected — clearing browser storage resets the dismiss flag. |
| Five Eyes AI analysis blank | AI toggle off or no key | Enable AI in admin bar. Analysis auto-fires 1200ms after `renderFiveEyes()`. |
| Export nudge keeps appearing | First export not registered | Ensure `toastExportSuccess()` is called after every export — it sets the `csp_first_export_done` flag. |
| History tab empty | localStorage blocked (private mode) | Expected — history requires localStorage. Export/import still works via file. |
| History not saving | `saveAssessmentToHistory()` guard clause | Function skips if `ctx.org` is empty AND `overallCyber===0`. Ensure context screen is filled. |
| Import silently fails | File is not valid JSON or missing `id` field | Check file was exported by CyberScore Pro. Records without `id` are skipped. |
| Trend chart missing | Fewer than 2 records after search filter | Remove search filter or complete more assessments. |
| Compare button missing | Record is the oldest in history | Comparison requires a previous record to compare against. |
| Risk matrix dots missing | Score threshold edge case | Check `scenarios.find()` logic — `lh` and `imp` must match exactly |

---

*CyberScore Pro v1.3 — Technical Guide*  
*Built June 2026 · Single-file vanilla JS SPA · No build step required*
