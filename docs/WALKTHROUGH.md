# CyberScore Pro — Step-by-Step Walkthrough

**Version 1.3** · Complete guided tour from first open to board report  
*Follow this end-to-end to see every feature of the tool*

---

## Before You Start

Download `index.html` and open it in Chrome, Firefox, Edge, or Safari. You should see a dark navy welcome screen with "Your *CyberScore* Health Check" as the heading and the admin bar pinned to the bottom of the screen.

**This walkthrough uses Demo mode** — no API key or real company data required. Everything is pre-filled so you can see the full tool in under 10 minutes.

---

## Part 1 — Welcome Screen

### What you see
The welcome screen shows four capability chips (CyberScore, Risk Score, Cost of Inaction, Optimised Roadmap), stats (8 domains, 12+ frameworks, 45 min, All Industries), and two assessment mode cards.

### Step 1 — Inspect the admin bar

Look at the bottom of your screen. The admin bar is always visible. You will see:
- **Demo** and **Live AI** buttons — Demo is active (highlighted in cyan)
- **AI Narrative** toggle — currently off
- **£ GBP** currency selector

The status text reads "Demo mode — demo data". This means the tool will use pre-filled answers from a realistic UK Financial Services example.

### Step 2 — Choose assessment mode

Click the **Deep Dive 🔬** card. It highlights with a cyan border. Notice the mode description changes to "48 questions with full control-level granularity".

For this walkthrough, click back to **Quick Check ⚡** — it's faster and shows the same results structure. Both modes use identical scoring logic.

### Step 3 — Start

Click **Begin Assessment →**. The screen transitions to the Context screen.

---

## Part 2 — Context Screen

### What you see
A form asking for organisation profile, currency, frameworks, and risk preferences. Because you are in Demo mode, it is **pre-filled automatically** with a UK Financial Services mid-market company.

### Step 4 — Review the pre-filled profile

Scroll down and notice these fields are populated:
- **Organisation name:** Acme Financial Ltd
- **Sector:** Financial Services
- **Region:** United Kingdom
- **Size:** Mid-market (251–1,000)
- **Annual revenue:** 25,000,000

These values drive everything — the risk model, peer benchmarks, framework selection, and cost figures all depend on them.

### Step 5 — Inspect the framework auto-selection

Look at the **Applicable frameworks** card. Because sector is "Financial Services" and region is "UK", the tool has automatically selected:
- Cyber Essentials (certification)
- Cyber Essentials Plus (certification)
- ISO 27001:2022 (certification)
- NIST CSF 2.0 (standard)
- FCA SYSC / PS21/3 (regulatory — mandatory for UK FinServ)
- CIS Controls v8 (standard)
- IASME Cyber Assurance (certification)

Change the sector to "Healthcare & Life Sciences" and watch the framework list update — HIPAA appears for US Healthcare. Change region to "EU" and DORA and NIS2 appear. Set it back to Financial Services / UK when done.

### Step 6 — Note the risk preferences

At the bottom of the context screen:
- **Security budget:** £80,000 — pre-populates the Optimiser slider
- **Risk appetite:** Medium
- **Priority certification:** ISO 27001:2022 — the roadmap and optimiser will target this
- **Optimisation objective:** Reduce risk fastest

### Step 7 — Start the quiz

Click **Start Assessment →**. The quiz screen loads.

---

## Part 3 — The Quiz

### What you see
A sticky header with a progress bar and domain badge. The first domain — "Identity & Access" — is shown with its questions and five-option buttons.

### Step 8 — Observe the pre-filled answers

Because you are in Demo mode, answers are loaded automatically. Each domain has one or more options already selected (highlighted with a cyan border and filled circle number).

Look at the answer pattern for Identity & Access — options 3 and 4 are selected (strong but not perfect). This reflects a business with good MFA but some PAM gaps.

### Step 9 — Click through domains

Click **Next Domain →** seven times to move through all eight domains. Notice:
- Each domain has a distinct colour accent and icon
- The progress bar fills as you advance
- Detection & Response has lower answers selected (option 1–2) — this will show as a critical gap in results
- Supply Chain has very low answers — this will be the weakest domain

### Step 10 — See Results

On the final domain (Awareness & Culture), click **See Results →**.

---

## Part 4 — Results Overview

### What you see
The results screen loads with three headline score cards at the top, the context banner confirming "Acme Financial Ltd · Financial Services · UK · mid", and an eight-tab navigation strip.

### Step 11 — Read the three scores

**CyberScore™** — should show approximately 61/100 with the band "🟡 Established". The bar is filled to 61% in cyan.

**Risk Score** — should show approximately 74/100 in red. Note this is higher than the CyberScore inverse (39) because the Financial Services sector multiplier of 1.4× applies — FinServ firms face higher risk for the same control gaps.

**Cost of Inaction** — should show approximately £2.4M/yr in amber. This is the annualised expected loss at current posture using the FAIR methodology.

> **Key insight to understand:** A 61 CyberScore in Financial Services creates more risk exposure than a 61 in Retail, because attackers target financial data more aggressively. The Risk Score captures this sector adjustment.

---

## Part 5 — Domain Scores Tab

### Step 12 — Read the radar chart

The radar chart shows your eight domain scores (blue line) against the Financial Services sector average of 72 (amber dashed line). Notice:
- Most domains are below the peer benchmark
- Detection & Response is the shortest spoke — most critical gap
- Identity & Access and Governance are closest to or above average

### Step 13 — Read the bar chart

The bar chart shows the same data as a horizontal comparison. Green bars (70+) = good, Amber (45–69) = needs work, Red (<45) = priority concern.

### Step 14 — Read the domain breakdown table

Below the charts, each domain shows its score, a coloured progress bar, the numeric score, and the delta vs peer (e.g. "−18 vs peer" in red). Negative deltas in red immediately show where you are underperforming your sector peers.

### Step 15 — Read the benchmark strip

Four cards show: Your score (61), Sector average (72), Top quartile (82), and Gap to top quartile (+21 pts). This frames the improvement journey.

### Step 16 — The AI Summary box

At the bottom of this tab you see the AI Executive Summary box. Currently it shows a key prompt asking you to enter an API key. We will come back to this in Part 9 if you have a key.

---

## Part 6 — Risk Analysis Tab

### Step 17 — Switch to Risk tab

Click the **⚠️ Risk Analysis** tab button.

### Step 18 — Risk breakdown bars

The domain risk bars are the inverse of the CyberScore bars — low CyberScore = high risk bar. Detection & Response shows the highest risk bar (red, ~80). Identity & Access shows the lowest (green, ~20).

### Step 19 — Risk matrix

The risk matrix plots six threat scenarios on a likelihood × impact grid:
- Red dots = Critical scenarios (high likelihood AND high impact)
- Look for dot **A** (Ransomware) — in the top-right Critical zone because Detection & Response is weak
- Dot **D** (Cloud misconfiguration) — lower down because Cloud scores are moderate

This is the most visually powerful slide for a board presentation — it shows where the red is without requiring any explanation.

### Step 20 — Qualitative risk dimensions

Six coloured squares scored 1–5 show non-financial risk dimensions: reputational damage, customer churn, board credibility, etc. These complement the financial FAIR model with softer risk signals.

---

## Part 7 — Cost of Inaction Tab

### Step 21 — Switch to Cost tab

Click **💷 Cost of Inaction**.

### Step 22 — Read the ALE formula

The formula box at the top shows the FAIR calculation with actual numbers:
```
ALE = SLE × ARO
SLE = £4,500,000 (revenue × 18% exposure factor)
ARO = 0.52 (sector breach frequency × control gap modifier)
ALE = £2,340,000 per year at current posture
```

This is the number you take to the board. "We are currently accepting £2.3M of annualised expected loss."

### Step 23 — Read the four cost cards

Four cards break the total down:
- **Breach cost** (~£3M) — forensics, notifications, recovery
- **Regulatory exposure** (~£1M max GDPR fine) — FCA SYSC applies too
- **Operational downtime** (~£342k for 5-day incident) — based on daily revenue
- **Insurance & opportunity** (~£550k) — premium uplift + deals lost for lacking certs

### Step 24 — Regulatory fine exposure bars

Below the cards, a bar chart shows maximum fine exposure by regulation. For UK FinServ you'll see GDPR/ICO and FCA bars. FCA fines are unlimited but the bar shows a 2% of revenue estimate.

### Step 25 — Opportunity cost

The bottom section shows revenue at risk from missing certifications:
- "Missing Cyber Essentials — Blocked from public sector contracts — £1.25M"
- "No ISO 27001 — Enterprise sales cycles extended — £2M"

These are the figures that resonate with commercial leaders, not just security teams.

---

## Part 8 — Frameworks, Gaps, Optimiser, Roadmap

### Step 26 — Frameworks tab

Click **📋 Frameworks**. A table shows each applicable framework with:
- Coverage % bar
- Status chip (Ready / Partial / Significant gaps)
- Key gaps column naming which domains are pulling coverage down

Notice ISO 27001 shows ~60% coverage with "Detection, Supply Chain" as key gaps. FCA SYSC shows partial coverage. Cyber Essentials shows higher coverage because it only covers five domains.

### Step 27 — Gap Register tab

Click **🔍 Gap Register**. You see 10 pre-built gaps sorted by severity:
- Two **CRITICAL** gaps at the top (No SIEM, No IR plan)
- Several **HIGH** gaps (MFA gaps, no phishing simulation, no vulnerability management)
- **MEDIUM** gaps below

Click the **Critical** filter button — the list filters to show only critical gaps. Click **All gaps** to restore.

Each gap shows: control reference (e.g. "ISO 27001 A.8.15"), effort, typical cost, risk reduction in points, and which frameworks it affects.

### Step 28 — Optimiser tab

Click **🎯 Optimiser**. This is the most interactive screen.

**Left panel — Controls:**
- The objective mode is set to "📉 Reduce risk fastest" (active)
- Budget slider shows £80,000 (pre-populated from context screen)
- Time horizon: 12 months
- Internal capacity: 5 days/month
- Risk appetite: Medium

**Right panel — Action plan:**
The top 6 actions are ranked. Look at the first one — it should be "No SIEM or centralised security monitoring" with a risk reduction of £500k+/year.

**Before/After projection:**
Three cards at the bottom of the left panel show: if you implement these 6 actions, your CyberScore goes from 61→83, Risk Score from 74→52, and annual loss drops by ~£870k.

### Step 29 — Try a different objective

Click **📋 Reach cert soonest**. The action list reorders — cert-critical gaps for ISO 27001 float to the top. The before/after numbers change.

Click **💰 Best value per spend** — the list reorders again, now showing the highest risk-per-£ actions first. MFA rollout (low cost, high risk reduction) moves to the top.

Switch the budget slider to £20,000 and watch the ROI numbers adjust. Increase to £200,000 and watch higher-effort actions become viable.

### Step 30 — Roadmap tab

Click **🗺 Roadmap**. A timeline shows four phases:
- **0–30 days** — 5 quick wins including MFA, backup testing, phishing simulation
- **1–3 months** — Foundation controls (EDR, SIEM, policies, supplier questionnaires)
- **3–6 months** — Intermediate programme (network segmentation, DLP, vulnerability management)
- **6–18 months** — ISO 27001 gap analysis, ISMS documentation, certification audit

ISO 27001 appears as a certification milestone badge in the final phase — matching the target cert set in the context screen.

---

## Part 9 — History Tab

### Step 31 — Open History tab

Click **📂 History**. Because you are in Demo mode and have just completed your first walkthrough, you should see one saved record — "Acme Financial Ltd" with today's date and the three scores.

> If this is the first time you have opened the tool and run the demo, you will see the empty state with the import drop zone. Run the assessment again to create a second record.

### Step 32 — Explore the history card

The history card shows:
- Organisation name and date/time
- Three score pills (CyberScore, Risk Score, Cost of Inaction)
- Sector, region, size, assessment mode, and cert target
- Four action buttons: Load & View, Compare with previous, Export, Delete

### Step 33 — Export a record

Click **⬇ Export** on the card. A `.json` file is saved to your downloads folder named something like `Acme_Financial_Ltd_2026-06-15.json`. Open it in a text editor to see the complete assessment snapshot.

### Step 34 — Import it back

Click **⬆ Import JSON** at the top of the History tab. Select the file you just exported. The tool reads it and tries to import — since the record already exists (same ID), it shows "0 new records, 1 duplicate skipped." This confirms the deduplication is working.

### Step 35 — Run assessment again to get a second record

Click **← Restart** in the results header. Click **Begin Assessment →**, click through the context screen (demo is still pre-filled), and click **Start Assessment →**. On the quiz screen, change one or two answers — for example, on Detection & Response, select option 3 instead of option 1. Click **See Results →**.

Now go back to the **📂 History** tab. You should see two records. The trend chart appears automatically — a line chart showing CyberScore and Risk Score across your two assessments. The delta strip shows the change: if you improved Detection answers, the CyberScore should be higher and Risk Score lower.

### Step 36 — Compare two assessments

Click **📊 Compare with previous** on the newer record. A modal appears showing:
- Side-by-side headers for the two assessments
- Score comparison table with directional arrows (▲ = increase, ▼ = decrease)
- Domain-by-domain bar comparison

Notice Detection & Response shows an improvement if you changed those answers. Close the modal with the ✕ or Close button.

### Step 37 — Export all history

Click **⬇ Export all (JSON)**. A file named `CyberScore_History_2026-06-15.json` downloads containing both records. This is your portable backup — drag it onto the History tab drop zone on any device to restore.

---

## Part 10 — AI Features (Optional — requires API key)

*Skip this section if you don't have an API key. The tool works fully without AI.*

### Step 38 — Switch to Live AI mode

In the admin bar, click **Live AI**. The API key fields appear.

### Step 39 — Select your provider and enter key

Select **Claude (Anthropic)** or **Gemini (Google)** from the dropdown.

Paste your API key into the field. Tick **Remember in browser** if you want it to persist. Click **Save**.

The status changes to "✅ Key saved & remembered in browser — AI ready".

### Step 40 — Enable AI Narrative

Click the **AI Narrative** toggle to ON. The toggle turns cyan.

### Step 41 — Generate AI content

Go to the **🛡 Domain Scores** tab. The AI Executive Summary box now shows a loading spinner. After 1–2 seconds, a three-paragraph narrative appears covering:
1. Your overall security posture and what the CyberScore means for a FinServ firm
2. Your top two risks and their business impact
3. Immediate priority actions and expected outcomes

Go to the **🔍 Gap Register** tab. Each gap now shows a purple "AI Insight" box with a one-sentence contextual comment specific to UK Financial Services.

### Step 42 — Generate the board report

Go to the **🗺 Roadmap** tab. Click **Generate Board Report**. After 2–3 seconds, a board-ready one-page narrative appears covering: current posture, top risks, cost of inaction, recommended investments, and a suggested next review date.

Copy the text — paste it into a Word document or PowerPoint slide for your board pack.

---

## Part 11 — PDF Export

### Step 43 — Download PDF

In the results header bar, click **⬇ PDF Report**. Your browser downloads a file named `Acme_Financial_Ltd_CyberScore_Report_2026-06-15.pdf`.

Open it. You will see:
- A dark header with three headline scores
- Domain scores vs peer benchmark with coloured progress bars
- Top 5 gaps with severity chips, explanations, and cost estimates
- Cost of inaction summary (ALE formula + key figures)
- Footer disclaimer

The PDF is generated entirely in your browser — nothing was uploaded anywhere.

---

## Part 12 — Currency Switch

### Step 44 — Change currency

In the admin bar, click **€ EUR** in the currency dropdown. Every financial figure on the results screen updates instantly — the Cost of Inaction, all cost cards, the Optimiser ROI figures, and the regulatory fine amounts now show in euros using an approximate GBP→EUR conversion rate.

Switch to **$ USD** and then back to **£ GBP**. Notice the PDF would also use the currently selected currency if you exported now.

---


---

## Part 13 — Toast Notifications

*This part explains what each notification means and what to do when you see one.*

### Step 45 — First save toast

When you complete an assessment for the very first time, a green toast slides in from the bottom-right about 0.8 seconds after the results appear:

> **✅ Assessment saved to this browser**  
> Your results are stored in this browser only — they stay private on your device. To keep a permanent backup or share with a colleague, export from the History tab.  
> *Open History tab →*

Click the action link to jump directly to the History tab. This toast only appears once — on every subsequent save you get a shorter confirmation instead.

**What to do:** Click "Open History tab →" and export your first assessment.

### Step 46 — Export nudge toast

If you have saved before but never exported, subsequent saves show a blue info toast:

> **💡 Assessment saved**  
> Tip: you haven't exported yet. Use the History tab to export a .json backup you can restore on any device.  
> *Go to History →*

This nudge disappears permanently once you export at least one assessment (in either single or all-history format).

**What to do:** Export when convenient. Your data is safe in the browser until then.

### Step 47 — Returning user save toast

Once you have exported at least once, saves show a brief green toast:

> **✅ Assessment saved**  
> Added to your History. 3 record(s) stored in this browser.

No action needed — this is purely informational.

### Step 48 — Private/incognito mode warning

Open the tool in a private browser window and complete an assessment. The save toast will be amber:

> **⚠️ Assessment not saved**  
> Your browser storage is unavailable (private/incognito mode?). Download the PDF now to keep a record of your results.  
> *Download PDF →*

**What to do:** Click "Download PDF →" immediately. In private mode, your results will be lost when you close the tab.

### Step 49 — Export toasts

Click **⬇ Export all (JSON)** in the History tab. After the file downloads, a green toast confirms:

> **✅ Export complete**  
> "CyberScore_History_2026-06-15.json" saved to your downloads. Store it safely — it contains 2 assessment records and can be re-imported on any device.

Click **⬇ Export** on a single card. The toast names that specific file instead.

If you click Export when history is empty, an amber toast explains there is nothing to export.

### Step 50 — Import toasts

Drag a `.json` file onto the History tab drop zone. After import:

> **✅ 2 records imported**  
> All records imported successfully. Your history has been updated.

If some records were already in your history:

> **✅ 1 record imported**  
> 1 duplicate skipped (already in your history).

If the file is invalid, a red error toast explains the problem.

### Step 51 — Delete and clear toasts

Click **🗑 Delete** on a history card and confirm. A blue toast confirms:

> **💡 Record deleted**  
> The assessment has been removed from your history. If you need it back, re-import from an exported .json file.

Click **🗑 Clear all** and confirm. A red toast confirms with the count:

> **🗑️ 3 records cleared**  
> All history has been removed from this browser. Import a .json backup to restore, or complete a new assessment to start fresh.

Note: the "Clear all" confirm dialog now tells you how many records will be deleted and reminds you to export first — this is a stronger warning than a plain "Are you sure?".


---

## Part 14 — Five Eyes AI & Cyber Resilience

*This part covers the new Five Eyes framework added in v1.3, triggered by the joint statement issued today, 22 June 2026.*

### Step 52 — The alert banner

When you load results (or if you already have results open from this walkthrough), look at the top of the results body — above the three score cards. You will see a prominent purple banner with a pulsing red "NEW TODAY" badge:

> 🛡️ **Five Eyes Joint Statement — AI Cyber Threat Warning** NEW TODAY · 22 Jun 2026
>
> *"Frontier AI models are anticipated to exceed current industry expectations, fundamentally transforming both offensive and defensive cyber capabilities. The timeline is not years, it is months."*

The banner shows all five agency flags (🇬🇧 🇺🇸 🇦🇺 🇨🇦 🇳🇿) and three links: the joint statement, the May 2026 agentic AI guidance, and a direct link to your Five Eyes score. Click the ✕ to dismiss it — it will not return (stored in your browser). Click "View your Five Eyes score →" to jump straight to the Frameworks tab.

### Step 53 — The Five Eyes toast

About 2 seconds after results load, a blue info toast appears bottom-right:

> **💡 Five Eyes statement issued today**  
> The five national cyber agencies issued a joint warning today: AI threats are months away, not years. Your Five Eyes Alignment Score is now in the Frameworks tab.  
> *View Five Eyes score →*

Click the action link. If AI is enabled, you may also see a second toast: "Generating Five Eyes AI analysis…"

### Step 54 — Frameworks tab — Five Eyes row

Click the **📋 Frameworks** tab. Scroll down the framework table. You will see a highlighted row with a purple left border:

> 🛡️ **Five Eyes AI & Cyber Resilience** NEW  
> Joint statement 22 Jun 2026 + Agentic AI guidance May 2026

The row shows coverage %, a status chip, and key gaps just like other frameworks. It appears for all organisations regardless of sector or region — the Five Eyes principles apply globally.

### Step 55 — Five Eyes alignment panel

Below the framework table, a full alignment panel appears with:

**Score hero** — a large number (e.g. 48/100) coloured by band, labelled "Five Eyes Alignment Score", with all five nation flags.

**7 principle bars** — each principle shows its icon, name, description, a coloured progress bar, and percentage. Principles with a `+ AI Q` tag are boosted by your AI question answers (Deep Dive only).

For the demo data (UK Financial Services, Quick Check mode), you should see:
- Secure by Design: ~65% (established governance)
- Defence in Depth: ~45% (weak detection)
- Human Oversight of AI: ~35% (no AI questions answered in quick mode)
- Least Privilege for AI: ~30% (IAM gaps + no AI question)
- Resilience over Reliance: ~25% (weak detection + no AI question)

The overall score for demo/quick should be around 42–50 — showing the tool correctly identifies AI governance as a key gap.

### Step 56 — Switch to Deep Dive and answer AI questions

Go back: click **← Restart** → **Begin Assessment** → select **Deep Dive 🔬** → **Begin Assessment →** → complete context → **Start Assessment →**

Navigate to the **Governance & Policy** domain. After the 5 standard questions, you will see 5 additional questions prefixed `[Five Eyes]`:

1. *[Five Eyes] Do you have a formal AI security and procurement policy?*
2. *[Five Eyes] Are AI systems used in your security stack auditable and explainable?*
3. *[Five Eyes] Do you maintain human override capability for AI-driven security decisions?*
4. *[Five Eyes] Have you assessed whether AI agents or tools in use are over-permissioned?*
5. *[Five Eyes] Do you have tested fallback procedures if an AI security tool fails?*

Select "option 3" or higher for each (for demonstration purposes). Proceed to results. Now return to the Frameworks tab — the `+ AI Q` tagged principles should show noticeably higher scores, and the overall Five Eyes alignment score should improve.

### Step 57 — Three new [Five Eyes] gaps

Click the **🔍 Gap Register** tab. Scroll down and look for gaps tagged `[Five Eyes]`:

- **[Five Eyes] No AI governance or procurement policy** — CRITICAL — references "Five Eyes Accountability Risk Class / May 2026 Agentic AI Guidance"
- **[Five Eyes] AI agents potentially over-permissioned** — HIGH — references "Five Eyes Privilege Risk Class"
- **[Five Eyes] No human override procedure for AI security decisions** — HIGH — references "Five Eyes Human Oversight Principle"

Each has a control reference linking to the specific Five Eyes risk class and guidance document.

### Step 58 — AI-powered Five Eyes analysis (if key enabled)

If you have AI enabled, scroll to the purple AI box below the Five Eyes alignment panel in the Frameworks tab. It will contain a two-paragraph analysis:
- Para 1: what the June 22 joint statement means specifically for your sector and region
- Para 2: your top 2 specific actions to improve Five Eyes alignment

This is the most timely AI output in the tool — it directly references today's statement and is specific to your organisation's profile.

## What You've Covered

| Feature | ✅ |
|---|---|
| Welcome screen + mode selection | ✅ |
| Context profiler with framework auto-selection | ✅ |
| Quiz navigation across 8 domains | ✅ |
| Three headline scores (CyberScore, Risk, Cost) | ✅ |
| Domain Scores tab — radar, bar chart, benchmark strip | ✅ |
| Risk Analysis — domain bars, risk matrix, qualitative dimensions | ✅ |
| Cost of Inaction — FAIR model, regulatory fines, opportunity cost | ✅ |
| Framework adherence matrix | ✅ |
| Gap register with severity filtering | ✅ |
| Optimiser — three modes, five controls, before/after projection | ✅ |
| Certification roadmap | ✅ |
| History tab — auto-save, export, import, trend chart, comparison modal | ✅ |
| Toast notifications — smart save alerts, export/import/delete confirmations | ✅ |
| Five Eyes alert banner, alignment panel, 7 principles, AI analysis | ✅ |
| Three new [Five Eyes] gaps in gap register | ✅ |
| Five Eyes AI questions in Deep Dive Governance domain | ✅ |
| AI features (Executive Summary, Gap Insights, Board Report) | ✅ if key available |
| PDF export | ✅ |
| Currency switching | ✅ |
| Admin bar — Demo/Live toggle, API key persistence | ✅ |

---

## Next Steps

**For a real assessment:**
1. Click **← Restart** → switch off Demo mode in admin bar (click Live AI or just leave on Demo and answer questions yourself)
2. Fill in your real organisation details on the Context screen
3. Answer the quiz honestly — lower is fine, the tool is designed to surface gaps
4. Download the PDF and share with your board or security team
5. Use the Optimiser to build a prioritised action plan within your real budget

**For clients (consultancy use):**
1. Run the assessment with the client in the room — walk through each domain question together
2. Export the JSON at the end (History tab → Export) to archive the client record
3. Use the Compare feature on follow-up engagements to show progress
4. Generate the AI Board Report and use it as the first draft of your deliverable

**For demos:**
1. Keep Demo mode on
2. Go straight to results and walk through the tabs
3. The demo data is calibrated to show a realistic but imperfect profile — all eight tabs have meaningful content

---

*CyberScore Pro v1.3 · Walkthrough complete*
