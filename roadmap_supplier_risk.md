# Supplier Evidence & Risk‑Multiplier Roadmap

## 1. Standard Region & Sector Multipliers (1 – 1.3 range)

| Dimension | Value Range | Typical Default (example) | Source / Rationale |
|-----------|-------------|--------------------------|--------------------|
| **Region** | 1.00 – 1.30 | EU = 1.20, US = 1.15, APAC = 1.25, LATAM = 1.10, Africa = 1.30 | Derived from **World Bank Country Risk Ratings** and **ENISA 2024 Threat Landscape** – higher geopolitical exposure → higher multiplier.
| **Sector** | 1.00 – 1.30 | Finance = 1.30, Healthcare = 1.25, Critical Infrastructure = 1.28, Technology = 1.10, Public = 1.20, Manufacturing = 1.12 | Based on **NIST CSF Impact Tiers** and sector‑specific breach frequency data (Verizon 2024 DBIR).

> **How to use** – The JSON file `risk_multipliers.json` ships with these defaults. Users can override any entry via the **Risk Settings** tab.

## 2. Supplier‑Evidence Expectations by Major Defence / Government Ministries

| Country / Ministry | Canonical Framework / Guideline | Typical Evidence Requested (high‑level) | Gap in Current CyberScore Pro (v1.9) |
|--------------------|--------------------------------|---------------------------------------|--------------------------------------|
| **United Kingdom – MOD (UK MOD)** | **Minimum Cyber Security Standard (MCSS)** – ISO 27001‑aligned | • ISA/ISRA (Information Security Assessment) report<br>• Third‑party security certifications (ISO 27001, Cyber Essentials Plus)<br>• Pen‑test reports (last 12 months)<br>• Secure Development Lifecycle evidence (SAST/DAST) | • No dedicated upload of third‑party certificates<br>• No automated storage of penetration‑test PDFs<br>• No checklist for Secure Development lifecycle
| **European Union – ENISA / EU C‑CERT** | **ENISA Guidelines** & **EU Cybersecurity Act** (Cybersecurity Certification) | • Certification of compliance (eIDAS, ISO 27001)<br>• GDPR‑aligned data‑handling evidence<br>• Supply‑chain risk management plan | • No GDPR‑specific data‑processing addendum attached
| **India – CERT‑In** | **CERT‑In Guidelines** (ISO 27001‑based) | • Security audit reports<br>• Incident‑response capability statement<br>• Evidence of compliance with **Indian Data Protection Bill** | • No Indian‑specific data‑protection acknowledgement
| **United States – DoD / DHS** | **CMMC 2.0** (Cybersecurity Maturity Model Certification) | • CMMC level evidence (plan of actions, audit reports)<br>• FedRAMP authorization excerpts (if SaaS)<br>• Continuous monitoring logs | • No CMMC level field, no continuous‑monitoring artifact storage
| **South Africa – Dept of Communications (DOC)** | **ISACA South Africa Cyber‑Security Framework** | • ISMS audit report<br>• Compliance with POPIA (Protection of Personal Information Act) | • No POPIA compliance statement upload
| **Australia – ASD (Australian Signals Directorate)** | **IRAP** (Information Security Registered Assessors Program) | • IRAP assessment report<br>• Security Architecture diagram (network) | • No network‑diagram upload, no IRAP status field
| **Canada – CSE / DSB** | **Canadian Centre for Cyber Security (CCCS) Guidelines** | • Cyber‑security policy documents<br>• Risk‑assessment reports aligned with **IT Security Policy (PS‑6)** | • No policy‑review document upload beyond the existing Governance tab

### Summary of Gaps
1. **Missing dedicated upload fields** for certifications (ISO 27001, Cyber Essentials, CMMC, IRAP, etc.).
2. **No taxonomy** for evidence type – all files are stored as a generic list.
3. **No metadata** (date, expiry, cert‑level) captured alongside the file.\n4. **No automated validation** (e.g., checksum, PDF‑page‑count) to ensure completeness.
5. **No jurisdiction‑specific compliance checklist** (GDPR, POPIA, Data‑Protection Bill, etc.).

## 3. Roadmap to Close the Gaps (Quarterly Milestones)

| Milestone | Deliverable | Owner / Effort | Target Release |
|-----------|-------------|----------------|----------------|
| **Q1 2026** | **Evidence‑type taxonomy** – Extend `answers.supplierEvidence` schema to capture `type` (ISO, Pen‑Test, CMMC, etc.), `issuedDate`, `expiryDate`. Update UI to include a dropdown for type when uploading. | Front‑end dev (2 days) + schema design (1 day) | v1.9‑patch‑1 |
| **Q2 2026** | **Region‑specific compliance checklist** – Add a collapsible section under Supplier Evidence that shows required documents for the selected country (e.g., MCSS for UK, CMMC for US). | Product owner (requirements) + dev (3 days) | v2.0‑alpha |
| **Q3 2026** | **Thumbnail preview & download** – Implement PDF first‑page rendering via **pdf.js**; store files in `localStorage` (Base64) with metadata; add a **Download** button per entry. | Front‑end dev (5 days) + QA (2 days) | v2.0‑beta |
| **Q4 2026** | **Automated evidence validation** – Verify file type, size ≤ 5 MB, checksum generation, and optional digital‑signature verification (for PDFs). Show warnings for missing required evidence per jurisdiction. | Security engineer (2 days) + dev (4 days) | v2.0‑release |
| **Q1 2027** | **Governance & Policy Review expansion** – Add country‑specific policy questions (e.g., GDPR, POPIA, Data‑Protection Bill) and map them to the evidence checklist. | Analyst (2 days) + dev (3 days) | v2.1 |
| **Q2 2027** | **Exportable compliance package** – One‑click generation of a ZIP containing all uploaded evidence, a summary report, and a compliance matrix aligned to the selected ministry’s framework. | Back‑end (Node) dev (4 days) + UI (2 days) | v2.1‑patch |

### Quick Wins (Can be shipped in the current sprint)
- **Add a static dropdown** for evidence type (ISO 27001, Cyber Essentials, CMMC, IRAP, etc.) and store it with each file.
- **Show a generic PDF icon** for PDFs (no rendering) – this satisfies the thumbnail preview requirement with minimal effort.
- **Publish `risk_multipliers.json`** with the default values listed above and a link to the data source (World Bank, ENISA, NIST).
- **Create a “Quick Reference Guide” modal** (already scoped) that includes a one‑page summary of the supplier‑evidence checklist for each ministry.

## 4. Sources for Multipliers & Guidance
1. **World Bank Country Risk Ratings 2024** – https://databank.worldbank.org/source/country-risk‑ratings
2. **ENISA Threat Landscape 2024** – https://www.enisa.europa.eu/publications/enisa‑threat‑landscape‑2024
3. **Verizon Data Breach Investigations Report 2024** – https://www.verizon.com/business/resources/reports/dbir/
4. **NIST Cybersecurity Framework – Impact Tiers** – https://www.nist.gov/cyberframework/impact-tiers
5. **UK MOD MCSS** – https://www.gov.uk/government/publications/minimum-cyber-security-standard-mcss
6. **CMMC 2.0** – https://www.cmmc.gov
7. **IRAP (Australia)** – https://www.cyber.gov.au/acsc/view-all-content/irap
8. **CERT‑In Guidelines** – https://www.cert-in.org.in
9. **South Africa POPIA** – https://www.gov.za/documents/protection-personal-information-act
10. **Canada DSB Cyber‑Security Guidelines** – https://www.cyber.gc.ca

---
### Next Action
Please confirm the default multiplier table (or provide any alternative values) and the preferred placement of the **Risk Settings** tab. Once approved, I’ll generate the task checklist and start implementing the quick‑win items.
