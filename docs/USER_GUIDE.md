# CyberScore Pro — User Guide

**Version 1.3** · For business users, security leads, and consultants  
*No technical knowledge required*

---

## Table of Contents

1. [What is CyberScore Pro?](#1-what-is-cyberscore-pro)
2. [Before You Begin](#2-before-you-begin)
3. [Step 1 — Welcome Screen](#3-step-1--welcome-screen)
4. [Step 2 — Context & Profile](#4-step-2--context--profile)
5. [Step 3 — The Assessment Quiz](#5-step-3--the-assessment-quiz)
6. [Step 4 — Understanding Your Results](#6-step-4--understanding-your-results)
7. [The Eight Result Tabs Explained](#7-the-seven-result-tabs-explained)
8. [Using the Optimiser](#8-using-the-optimiser)
9. [AI-Powered Features](#9-ai-powered-features)
10. [Exporting & Sharing Results](#10-exporting--sharing-results)
11. [History — Saving & Comparing Assessments](#11-history--saving--comparing-assessments)
12. [Running a Demo](#12-running-a-demo)
13. [Five Eyes AI & Cyber Resilience Framework](#13-five-eyes-ai--cyber-resilience-framework)
14. [Frequently Asked Questions](#14-frequently-asked-questions)

---

## 1. What is CyberScore Pro?

CyberScore Pro is a cyber security assessment tool that helps any business — regardless of size or technical sophistication — understand three things:

**How secure are you?**
Your **CyberScore™** (0–100) measures your security maturity across eight control domains, from identity management to staff awareness. A score of 75+ means you have a mature, measurable programme. A score below 40 means you have critical gaps that need immediate attention.

**How exposed is your business?**
Your **Risk Score** (0–100, lower is better) translates your security gaps into business risk exposure, adjusted for your specific sector. A Financial Services firm has different risk exposure than a small retailer, even with identical security controls.

**What does doing nothing cost you?**
Your **Cost of Inaction** puts a number on your current exposure in pounds, euros, or dollars — calculated using the FAIR risk methodology used by insurers and risk professionals. This is the annualised expected loss if you make no improvements.

The tool then produces a **gap register**, a **framework adherence matrix**, an **optimisation engine**, and a **certification roadmap** — all tailored to your sector, region, and company size.

---

## 2. Before You Begin

### What you need

- A modern web browser (Chrome, Firefox, Edge, or Safari — any version from 2022 onwards)
- The `index.html` file (open it directly from your desktop, or visit the hosted URL)
- Approximately 15 minutes for Quick Check, or 45 minutes for Deep Dive
- Basic knowledge of your organisation's current IT and security arrangements

### What you don't need

- Any software installation
- A login or account
- An internet connection (after the page has loaded)
- Any technical or cyber security expertise to complete the questionnaire

### Who should do the assessment?

The assessment works best when completed by someone with a good overview of the business — typically a CEO, COO, IT Manager, Finance Director, or a consultant working with the organisation. For the most accurate results, involve your IT lead for the technical questions.

### A note on honest answers

The tool is only as useful as the honesty of the answers. There is no right or wrong answer — and no one is judging the results. The purpose is to get an accurate picture of where you are today so you can build a realistic plan to improve.

---

## 3. Step 1 — Welcome Screen

When you open the tool, you will see the welcome screen with the CyberScore Pro branding and two options for how deep you want to go.

### Choose your assessment mode

**⚡ Quick Check (~15 minutes)**
Covers all 8 security domains with 2 questions each — 16 questions total. Ideal for:
- A first-pass overview before a board meeting
- A client-facing demonstration
- A senior leadership briefing where time is limited
- An initial baseline when starting a security programme

**🔬 Deep Dive (~45 minutes)**
Covers all 8 domains with 5 questions each — 40 questions total. Produces a much more granular gap analysis and is required for:
- Certification gap analysis (Cyber Essentials, ISO 27001)
- Board-level risk reporting
- A formal security improvement programme
- When engaging a cyber security consultancy

Both modes use the same scoring model. The Deep Dive gives more precise results because it captures more nuance — a domain can look stronger or weaker depending on which specific controls are in place.

Click **Begin Assessment →** once you have chosen your mode.

---

## 4. Step 2 — Context & Profile

This screen captures information about your organisation. It is used to:
- Select the most relevant security frameworks for your profile
- Calibrate the risk model with sector-specific threat data
- Set peer benchmark scores for your industry
- Calculate cost of inaction figures based on your revenue

### Organisation Profile fields

**Organisation name** — Your company or trading name. Used in the PDF report header.

**Contact name** — The person completing the assessment. Used in report outputs.

**Industry sector** — Choose the sector that best describes your primary business. This is the most important field — it determines which regulatory frameworks apply and how your risk score is calculated. If you span multiple sectors, choose the one that carries the highest regulatory obligation (e.g. if you are a tech company that processes payments, choose Financial Services or Retail & E-commerce).

**Region / Jurisdiction** — Where your business is primarily regulated. UK, EU, US, or Global. This determines which mandatory regulations apply (e.g. DORA applies to EU financial firms; FCA SYSC applies to UK financial firms).

**Company size** — Based on employee headcount. This affects which frameworks are applicable — some (like IASME) are designed specifically for smaller businesses, while others (like DORA) only apply above certain thresholds.

**Annual revenue** — Used to calculate the cost of inaction figures. Enter in the currency you have selected. Pre-set buttons (£500k, £2M, £10M, £50M, £250M) are provided for speed. If you leave this blank, a default of £5M is used.

### Currency

Select your preferred currency using the three buttons: **£ GBP**, **€ EUR**, or **$ USD**. All financial figures throughout the tool — including the optimiser budget slider and PDF report — will use this currency. You can change it at any time using the dropdown in the admin bar at the bottom of the screen.

### Auto-selected frameworks

As you fill in sector and region, a preview panel will appear showing which frameworks have been automatically selected for your profile. These are the frameworks your results will be measured against. They are split into:

- **Mandatory** (red) — regulatory requirements you must comply with
- **Recommended** (blue) — internationally recognised standards that are strongly advisable
- **Certification** (purple) — certifications you can pursue to demonstrate compliance

You do not need to change these — they are chosen based on published guidance and regulatory scope.

### Risk & Optimisation Preferences

**Security budget** — Your approximate annual spend on cyber security (tools, staff, consultancy). This pre-populates the optimiser's budget slider. You can adjust it at any time in the results.

**Risk appetite** — How much residual risk your organisation is comfortable accepting after implementing controls. Low = minimise all risk (common in regulated sectors). Medium = balance risk and cost. High = accept more risk to keep spend low.

**Priority certification target** — If you have a specific certification in mind (Cyber Essentials for UK public sector tendering, ISO 27001 for enterprise clients), select it here. The optimiser and roadmap will prioritise actions that close the gaps needed for that specific certification.

**Optimisation objective** — The primary goal for the optimiser's action ranking. You can change this at any time in the Optimiser tab.

Click **Start Assessment →** when ready.

---

## 5. Step 3 — The Assessment Quiz

The quiz takes you through each of the 8 security domains one at a time. A progress bar at the top shows how far through the assessment you are.

### The 8 domains

| Domain | What it covers |
|---|---|
| 🔐 Identity & Access | Who can access what, and how — MFA, admin accounts, passwords, vendor access |
| 🛡️ Network Security | How your network is protected — firewalls, remote access, monitoring, Wi-Fi |
| 🔍 Detection & Response | How quickly you spot and respond to incidents — EDR, SIEM, IR planning |
| ☁️ Cloud & Asset Management | What you have and how it is secured — asset inventory, cloud security, patching |
| 📦 Data Protection | How sensitive data is handled — encryption, backups, DLP, privacy compliance |
| 🔗 Supply Chain & 3rd Party | How you manage vendor and supplier security risk |
| 🧑‍💼 Governance & Policy | Security leadership, policies, risk management, and board accountability |
| 🎓 Awareness & Culture | Training, phishing simulations, and security culture |

### Answering questions

Each question has five options, ranging from no control in place (score 0) to best practice fully implemented (score 4). Read each option carefully and select the one that most accurately describes your current situation.

**Tips for answering:**
- Choose the option that reflects reality today, not your aspirations or plans
- If you are genuinely unsure, choose the option one level below what you think — the tool is designed to prompt improvement, and over-claiming leads to a misleadingly high score
- "Some" and "partial" are valid answers — most organisations are not at either extreme
- If a question is not relevant to your business (e.g. a water treatment question for a media company), choose the lowest option and note it

Click **Next Domain →** when you have answered all questions in that section. You can go back using the **← Previous** button.

On the final domain, the button becomes **See Results →**.

---

## 6. Step 4 — Understanding Your Results

After completing the quiz, you are taken to the results screen. At the top you will see a context banner confirming your organisation, sector, region, and size — check these are correct.

### The three headline scores

**🛡 CyberScore™**
Your overall security maturity score. Calculated as a weighted average of your eight domain scores. Higher is better.

- 90–100 ⭐ Leading — industry benchmark, ready for advanced certifications
- 75–89 🟢 Advanced — mature programme, ISO 27001 achievable
- 60–74 🟡 Established — structured programme, Cyber Essentials Plus achievable
- 40–59 🟠 Developing — basic controls, common in growing businesses
- 0–39 🔴 Critical — significant gaps, immediate action required

**⚠️ Risk Score**
Your business risk exposure. This is not the same as CyberScore — it factors in your specific sector's threat landscape. A Financial Services firm with a CyberScore of 60 has higher risk exposure than a media company with the same score, because attackers target financial data more aggressively.

Lower is better. A score above 70 indicates critical exposure.

**💷 Cost of Inaction**
The annualised expected financial loss if you make no changes. This is calculated using the FAIR (Factor Analysis of Information Risk) methodology:

- It combines the likely financial impact of a breach with the probability of one occurring given your current controls
- It includes regulatory fine exposure, operational downtime, incident response costs, and insurance premium uplift
- It is a planning estimate, not a guarantee — actual costs vary significantly

Use this number in board conversations to frame cyber security as a financial risk management question, not just a technical one.

---

## 7. The Eight Result Tabs Explained

### 🛡 Domain Scores tab

Shows your score for each of the 8 domains, displayed as:
- A **radar chart** showing your profile vs sector peer average
- A **bar chart** comparing each domain to the sector peer
- A **domain bar list** showing your score, peer benchmark, and the gap between them (Δ)
- A **benchmark strip** showing your score vs sector average, top quartile, and the gap to best in class

Green bars (70+) = good. Amber (45–69) = needs work. Red (below 45) = priority concern.

The AI Executive Summary box at the bottom of this tab will generate a personalised narrative if you have connected an API key.

### ⚠️ Risk Analysis tab

Three sections:

**Risk breakdown by domain** — shows risk exposure per domain (inverse of your score, adjusted). High bars here are the domains where your gaps create the most business risk.

**Risk matrix** — a likelihood × impact grid showing your top 6 risk scenarios (ransomware, phishing, insider theft, supply chain attack, data breach, cloud misconfiguration) positioned based on your answers. Dots represent your identified scenarios — hover over them to see the scenario name.

**Qualitative risk dimensions** — six non-financial impact dimensions scored 1–5: reputational damage, customer churn risk, board credibility impact, supplier trust loss, talent retention risk, and media exposure risk. These complement the financial cost model.

### 💷 Cost of Inaction tab

Four sections:

**ALE formula** — shows the FAIR calculation behind your headline cost figure.

**Cost breakdown cards** — four cards covering:
- Direct breach cost (forensics, notifications, recovery)
- Regulatory fine exposure (GDPR, ICO, FCA, DORA, NIS2 — whichever apply to your profile)
- Operational downtime cost (based on a 5-day incident scenario)
- Insurance and opportunity cost (premium uplift + deals at risk for lacking certifications)

**Regulatory fine exposure** — bar chart of maximum fine amounts under each applicable regulation. This is worst-case exposure, not a prediction.

**Opportunity cost** — revenue and contracts at risk because of missing certifications or poor cyber posture (public sector tendering, enterprise sales, M&A readiness).

### 📋 Frameworks tab

A table showing each framework applicable to your profile, with:
- **Coverage %** — how much of this framework's requirements you currently meet
- **Status** — Ready (70%+), Partial (45–69%), or Significant gaps (below 45%)
- **Key gaps** — which domains are pulling your coverage down

Use this table to answer the question: "which certification could I achieve fastest?"

### 🔍 Gap Register tab

A prioritised list of the specific security controls you are missing or have only partially implemented. Each gap shows:
- **Severity** — Critical, High, or Medium
- **Control reference** — the specific ISO 27001, NIST, or other framework control this addresses
- **Why it matters** — a plain-English explanation of the business risk
- **Effort** — Low, Medium, or High implementation effort
- **Typical cost** — indicative budget range
- **Risk reduction** — how many points this would remove from your Risk Score
- **Frameworks** — which certifications this gap affects

Use the filter buttons at the top to view Critical gaps only, High gaps only, or all gaps.

If AI is enabled, each gap also shows a one-sentence contextual insight specific to your sector and region.

### 🎯 Optimiser tab

The optimiser is the most powerful feature in the tool. It takes your gaps and ranks them into an action plan based on your specific constraints. See Section 8 for a full walkthrough.

### 🗺 Roadmap tab

A phased 18-month implementation roadmap divided into four stages:
- **0–30 days** — Quick wins: low effort, high impact actions you can start immediately
- **1–3 months** — Foundation controls: the core security baseline
- **3–6 months** — Intermediate programme: deeper structural improvements
- **6–18 months** — Maturity and certification: the path to your target certification

Each stage includes specific actions with effort indicators. Certification milestones are shown where they fall in the sequence.

The AI Board Report button at the bottom of this tab generates a one-page, board-ready summary if you have an API key connected.

---

## 8. Using the Optimiser

The Optimiser tab answers the question: **"Given my budget, time, and capacity — what should I fix first?"**

### Step 1 — Choose your objective

Select one of three modes:

**📉 Reduce risk fastest** — ranks actions by how much they reduce your Risk Score and Cost of Inaction. Use this if you have had a near-miss incident, are under board pressure, or your risk score is in the Critical band.

**💰 Best value per spend** — ranks actions by risk-reduction-per-£. More cost-efficient than the risk-first mode. Use this when budget is tight and you need to demonstrate value.

**📋 Reach cert soonest** — prioritises the controls needed to achieve your target certification. Use this when you have a tender deadline, a client contract requiring Cyber Essentials or ISO 27001, or an M&A process approaching.

### Step 2 — Set your constraints

Use the four sliders to reflect your real situation:

**Annual budget** — drag to your approximate security budget. The optimiser ranks actions that fit within this envelope and flags anything that exceeds it.

**Time horizon** — how many months you are planning for. Shorter horizons push quick-win actions to the top. Longer horizons allow structural improvements to be included.

**Internal capacity** — how many days per month your internal team can dedicate to security improvement work. Actions requiring high internal effort are ranked lower if capacity is constrained.

**Risk appetite** — Low means the optimiser requires you to close more gaps. High means it accepts more residual risk and focuses only on the most critical items.

### Step 3 — Read the outputs

**Before/After projection** — three cards showing your projected CyberScore, Risk Score, and annual loss after implementing the top recommended actions.

**Prioritised action plan** — the top 6 actions, ranked by your chosen objective. Each shows:
- Rank number
- Action name and description
- Effort level and typical cost
- Which frameworks it covers
- **Risk £ removed per year** — the annualised loss reduction you can expect from this single action

The **Risk £ removed** figure is the most powerful number in the tool. It lets you answer the CFO's question: "If we spend £12,000 on MFA rollout, what do we get back?" The answer is shown directly in the action card.

---

## 9. AI-Powered Features

CyberScore Pro can connect to Claude (Anthropic) or Gemini (Google) to generate personalised AI narratives. These features are entirely optional.

### Setting up AI

1. In the admin bar at the bottom of the screen, click **Live AI**
2. Select your provider: **Claude (Anthropic)** or **Gemini (Google)**
3. Paste your API key into the field
4. Tick **Remember in browser** if you want the key to persist between sessions
5. Click **Save**
6. Toggle **AI Narrative** to ON

Your key is stored only in your browser's local storage. It is never written to the HTML file, never sent to GitHub, and the only outbound connection is directly to your chosen AI provider.

### Getting an API key

**Anthropic Claude** — create an account at console.anthropic.com, go to API Keys, and create a new key. Cost is approximately £0.002–£0.003 per assessment (using Claude Haiku). You need to add a payment method but the cost per use is very low.

**Google Gemini** — create an account at aistudio.google.com, click "Get API Key". The Gemini 1.5 Flash model has a generous free tier — you can run many assessments at no cost.

### What the AI generates

**Executive Summary** (Domains tab) — a three-paragraph narrative covering your overall posture, your top two risks with business impact, and your immediate priority actions. Generated automatically when you load results.

**Gap Insights** (Gaps tab) — a single sentence of contextual, sector-specific insight for each gap in your register. For example, for a UK Financial Services firm, the gap insight for "No SIEM" will reference FCA expectations and typical breach dwell times in the sector.

**Board Report** (Roadmap tab) — a one-page, board-ready summary covering current posture, top risks, cost of inaction, recommended investments, and next review date. Click the **Generate Board Report** button to trigger this. Copy and paste it into a Word document or PowerPoint slide for your board pack.

---

## 10. Exporting & Sharing Results

### PDF Report

Click **⬇ PDF Report** in the results header. The PDF is generated entirely in your browser — nothing is uploaded anywhere. It includes:

- A header with your organisation name, sector, region, and date
- The three headline scores
- Domain scores vs peer benchmark
- Top 5 gaps with severity and cost
- Cost of inaction summary
- A footer disclaimer

The filename is automatically set to `[OrgName]_CyberScore_Report_[Date].pdf`.

### Sharing the tool itself

The entire tool is a single HTML file. To share it:
- Email the `index.html` file directly
- Share the GitHub Pages URL (e.g. `https://username.github.io/cyber/`)
- Save it to a shared drive

Recipients open it in their browser and run their own assessment. Each person's results are independent — nothing is shared between users.

### Sharing results

Results are not automatically saved. To preserve them:
- Download the PDF before closing the browser
- Screenshot the results tabs you want to keep
- Copy the AI board report text before navigating away

---


## 11. History — Saving & Comparing Assessments

Every time you reach the results screen, CyberScore Pro automatically saves the assessment to your browser's local storage. You don't need to do anything — it happens in the background. The History tab is the eighth tab in the results screen.

### What is saved

Each saved record captures:
- Organisation name, sector, region, size, and revenue
- Assessment mode (Quick Check or Deep Dive)
- All domain scores and the complete answer set
- CyberScore, Risk Score, and Cost of Inaction
- Date and time of the assessment
- Currency setting at the time

Records are stored in your browser only — nothing leaves your device. Up to 50 assessments are kept, with the newest at the top.

### The History tab

Open the History tab in the results screen at any time. If you have two or more saved assessments, a trend chart appears at the top showing your CyberScore and Risk Score over time. Below the chart, three delta cards show the change in scores since the previous assessment.

### Loading a past assessment

Click anywhere on a history card to load that assessment and view its full results — all seven tabs restore to the state they were in when the assessment was completed. A purple "📂 Restored from history" badge appears in the context banner so you know you are viewing a historic record.

To return to your current assessment, click **← Restart** and complete a new one.

### Comparing two assessments

On any history card (except the oldest), click **📊 Compare with previous**. A comparison modal appears showing:
- The date and profile of each assessment side by side
- Score changes for CyberScore, Risk Score, and Cost of Inaction with directional arrows
- A domain-by-domain breakdown showing which areas improved and which declined

This is particularly useful for demonstrating progress to a board or client — the comparison view shows the value of the security improvements made between assessments.

### Exporting history

**Export a single assessment** — click **⬇ Export** on any history card. A `.json` file is saved to your downloads folder containing the complete record for that assessment.

**Export all history** — click **⬇ Export all (JSON)** at the top of the History tab. All saved records are bundled into a single `.json` file. Use this to:
- Back up before clearing browser storage
- Transfer history to another device
- Share assessments with a colleague
- Archive a client's records at the end of an engagement

### Importing history

To restore a backup or import assessments from another device:
1. Click **⬆ Import JSON** at the top of the History tab, or drag a `.json` file onto the drop zone
2. The tool reads the file and adds any new records to your history
3. Duplicate records (same ID) are skipped automatically
4. Both single-record exports and full-history exports are supported

### Searching history

Type any organisation name or sector into the search box to filter the history list. The trend chart updates to reflect only the filtered records.

### Deleting records

**Delete one** — click **🗑 Delete** on any history card and confirm. This cannot be undone.

**Clear all** — click **🗑 Clear all** to remove every saved assessment. Always export first if you want to keep a backup.


### Notification toasts — what to do when they appear

CyberScore Pro shows small notification toasts in the bottom-right corner of the screen to keep you informed about what is happening with your data. They auto-dismiss after a few seconds, or you can click ✕ to close them immediately. Where a toast has an action link, click it to go directly to the relevant part of the tool.

**Save notifications** appear automatically about 0.8 seconds after your results load, giving the screen time to render first:

- **First time ever** — a green "Assessment saved to this browser" toast with a full explanation and a link to the History tab. This only appears once.
- **Saved before but never exported** — a blue info toast reminding you to export. This continues to appear until you export at least once.
- **Returning user** — a brief green confirmation showing how many records are now stored.
- **If storage is unavailable** (private/incognito mode) — an amber warning that the assessment was not saved, with a direct link to download the PDF instead. In this situation, downloading the PDF is the only way to preserve your results.

**Export notifications** confirm that a file was downloaded and remind you to store it safely. Once you have exported at least once, the repeated export-nudge in the save toast will stop appearing.

**Import notifications** tell you how many records were added and how many were skipped as duplicates.

**Delete and clear notifications** confirm the action and remind you how to restore from a backup.

### Storage limits

Browser localStorage has a 5MB limit per site. Each assessment record takes approximately 5–10KB, meaning you can store 500–1,000 assessments before approaching the limit. The tool keeps the newest 50 records automatically — if you need more, export and reimport as needed.

---

## 12. Running a Demo

For presentations, client meetings, or training sessions, use **Demo mode**.

1. Click **Demo** in the admin bar at the bottom of the screen
2. Click **Begin Assessment** — the context screen will be pre-filled with a UK Financial Services mid-market company profile
3. Click **Start Assessment →** — the quiz will be pre-answered
4. Click **See Results →** on any domain to jump straight to results

The demo data is designed to show a realistic but imperfect profile — strong governance and identity controls, weak detection and supply chain scores — so the gap register and optimiser show meaningful recommendations.

To return to a real assessment, click **← Restart** and then click **Demo** again to switch back to Demo mode off, or simply refresh the page.

---


## 13. Five Eyes AI & Cyber Resilience Framework

CyberScore Pro now includes a dedicated Five Eyes alignment score, informed by two landmark documents published in 2026 by the intelligence and cyber security agencies of the United Kingdom, United States, Australia, Canada, and New Zealand.

### What is the Five Eyes?

The Five Eyes is an intelligence-sharing alliance between the UK (NCSC), USA (CISA and NSA), Australia (ASD/ACSC), Canada (CCCS), and New Zealand (NCSC-NZ). When all five nations publish a joint statement, it carries significant weight — it reflects coordinated intelligence assessments, not just policy preferences.

### The two source documents

**Five Eyes Joint Leadership Statement — 22 June 2026**

Issued by the heads of all five agencies simultaneously. The central warning: frontier AI models are anticipated to transform offensive cyber capabilities not in years, but in months. The statement calls for: understanding and assessing risk and accountability; prioritising foundational cyber controls; empowering cyber leaders with authority and resources; and treating cyber resilience as a board-level business issue — not a technical one.

The statement explicitly declares: *"Secure-by-design and secure-by-default must become standard practice — not an aspiration."*

**Careful Adoption of Agentic AI Services — May 2026**

A 30-page joint guidance document covering autonomous AI systems (agents that can plan, decide, and act without human review at each step). It identifies five risk classes: privilege (over-permissioned agents), design and configuration (poor setup), behavioural (unexpected agent actions), structural (cascading failures across interconnected agents), and accountability (no audit trail or human oversight). It opens with: *"Until security practices, evaluation methods and standards mature, organisations should assume that agentic AI systems may behave unexpectedly."*

### The 7 principles and what they mean for your business

**🏗️ Secure by Design** — Security must be considered from the very start of any system design or technology procurement decision, not added on afterwards. In practice: security requirements in every project brief, security review gates in every project lifecycle.

**🔒 Secure by Default** — Technology should ship with the most secure settings enabled. Vendors who ship insecure defaults are transferring risk to their customers. In practice: check default configurations of every tool you use; never assume defaults are safe.

**🛡️ Defence in Depth** — No single control, technology, or AI tool should be relied upon as a complete defence. Layered controls mean that when one fails — and it will — others catch what falls through. The statement warns explicitly against single-tool reliance.

**🔍 Transparency & Accountability** — AI systems used in security decisions must be auditable and explainable. Your board should be able to understand what your AI security tools are doing and why. This is the accountability risk class from the May 2026 guidance.

**👤 Human Oversight of AI** — There must be meaningful human control over AI-driven security decisions. This does not mean humans must approve every alert, but it does mean humans must be able to override, halt, or interrogate AI actions — especially for autonomous agents. This is the behavioural risk class.

**🔑 Least Privilege for AI** — AI agents must operate with the minimum permissions necessary. The May 2026 guidance found 78% of compromised AI agents were over-permissioned. An AI agent with broad write access — if prompted adversarially — can delete firewall logs, exfiltrate data, or modify configurations autonomously. This is the privilege risk class.

**⚡ Resilience over Reliance** — You must have tested fallback procedures for when AI tools fail or behave unexpectedly. Over-reliance on AI without fallback is itself a risk. This is the structural risk class.

### What appears in the tool

**Alert banner** — when you load your results, a prominent purple banner at the top of the results screen summarises the June 22 statement with links to the official guidance documents. It can be dismissed once read.

**Toast notification** — two seconds after results load, a blue info toast appears pointing you to the Frameworks tab to view your Five Eyes score.

**Frameworks tab** — the Five Eyes framework appears as a highlighted row (purple left border, NEW badge) in the framework table. Below the table, a full alignment panel shows your score for each of the 7 principles with coloured progress bars. If AI is enabled, an AI analysis box auto-generates a personalised assessment of what the June 22 statement means specifically for your sector.

**Gap register** — three new gaps tagged `[Five Eyes]` appear in the gap register: no AI governance policy (Critical), AI agents potentially over-permissioned (High), and no human override procedure (High).

**Deep Dive assessment mode** — five additional questions prefixed `[Five Eyes]` appear in the Governance domain. These directly assess your AI security governance and are used to sharpen the principle scores for Transparency, Human Oversight, Least Privilege for AI, and Resilience. They do not appear in Quick Check mode.

### Five Eyes Alignment Score

The score (0–100) is calculated for each principle by averaging the domain scores most relevant to that principle. In Deep Dive mode, the five AI-specific questions each contribute 30% of the score for their relevant principle, with domain scores making up the remaining 70%. The overall Five Eyes score is the weighted average across all 7 principles.

A score of 70+ means your organisation is broadly aligned with Five Eyes guidance. Below 50 indicates significant gaps in AI security governance that need addressing — particularly given the May 2026 finding that the timeline for AI-enabled threats is months, not years.

---

## 14. Frequently Asked Questions

**Is this an official certification or audit?**
No. CyberScore Pro is a self-reported maturity assessment — a structured questionnaire that produces a scored output. It is a starting point, not an end point. To achieve formal certifications (Cyber Essentials, ISO 27001, SOC 2), you need to engage an accredited certification body. To get a professional security assessment, engage a qualified penetration testing firm or CISO consultancy.

**How accurate are the scores?**
The scores are as accurate as the answers. The tool is calibrated against IBM Cost of a Data Breach 2024, Verizon DBIR 2024, and NCSC guidance. The cost figures are planning estimates based on industry averages — actual breach costs vary significantly by organisation.

**Can I save my results?**
Yes — results are saved automatically to browser localStorage every time you reach the results screen. Open the History tab to see all saved assessments. To back up across devices, use the Export function in the History tab.

**Can I do multiple assessments for different sites or business units?**
Yes — complete each assessment separately. All are saved to History automatically. Use the "Compare with previous" feature to compare any two consecutive records, or export all as JSON to do your own analysis. A dedicated multi-site mode is planned for v1.2.

**My sector isn't listed — what should I choose?**
Choose the closest match, or select **Other**. The tool will use general industry benchmarks and apply the most universal frameworks. You can always add sector-specific context in the AI board report prompt.

**The framework I need isn't shown — why?**
The tool automatically selects frameworks based on your sector, region, and size. If you believe a framework should apply and is not showing, check that your sector and region are set correctly. You can also manually reference any framework in your PDF report or board report.

**Is my API key safe?**
Yes, if used correctly. Your key is entered at runtime and stored only in your browser's local storage if you tick "Remember in browser". It is never written to the HTML file, never transmitted to any server other than your chosen AI provider, and never stored on GitHub. To remove it, click **Clear** in the admin bar.

**Can I customise the tool with my own branding?**
Not in v1.0 — this is planned for v1.2 as a white-label mode. In the meantime, the PDF report can be opened in a PDF editor (e.g. Adobe Acrobat) and a logo added manually.

**What browsers are supported?**
Chrome, Firefox, Edge, and Safari — any version from 2022 onwards. Internet Explorer is not supported.

**How do I report a bug or request a feature?**
Raise a GitHub Issue in the repository. Include your browser, operating system, and a description of what happened vs what you expected.

---

*CyberScore Pro v1.3 — Self-reported cyber security maturity assessment*  
*Not a substitute for professional cyber security audit, penetration testing, or formal certification*
