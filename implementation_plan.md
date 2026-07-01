# Quick Action Items Implementation Plan (Updated per user input)

## Goal Description

Implement the five high‑impact, low‑effort enhancements identified in the CyberAsk 0107 feedback **and** incorporate the user‑specified refinements:
1. Provide **default risk‑multiplier values** (region & sector) with UI fields that allow manual override.
2. Present the risk‑multiplier settings in a **separate "Risk Settings" tab** (if implementation remains simple).
3. Enhance the **Supplier Evidence** upload component with a **thumbnail preview** (for images/PDF) and **download** option.
4. Add an **App Quick‑Reference Guide** accessible from the main UI.
5. Fix the Demo button, externalise framework list, and add the Policy Review domain (as previously scoped).

## User Review Required

> [!IMPORTANT]
> Please confirm the following decisions before work begins:
> - **Risk multiplier defaults**: We will ship a `risk_multipliers.json` file containing suggested values (e.g., EU = 1.2, US = 1.1, APAC = 1.3; sector factors similarly). The UI will show these defaults in the **Risk Settings** tab and allow the user to edit them.
> - **Separate Risk Settings tab**: We will create a new tab called **Risk Settings** that houses the region/sector selectors and override inputs. If you later prefer merging into the existing Settings panel, we can adjust.
> - **Supplier evidence preview**: Thumbnails will be generated for image files and the first page of PDFs (using the browser’s `FileReader` and `PDF.js`‑lite). Each uploaded file will have a **Download** button.
> - **Quick Reference Guide**: A modal dialog will display the content of `QUICK_REFERENCE.md` rendered as HTML, opened via a **Help** icon in the top‑right corner.
>
> > [!CAUTION]
> > Changing `index.html` directly will affect the live demo. Ensure a backup commit before applying.

## Open Questions

- Do you have a preferred source for the **latest suggested multiplier values** (e.g., a URL, internal guideline) or should we use the static example set described above?
- Should the **Risk Settings** tab be placed before the questionnaire tabs in the navigation bar, or after the *Framework* tab?
- For PDF thumbnail generation, do you want a simple first‑page image or a generic PDF icon? (We can use `PDF.js` to render the first page.)
- Would you like the Quick Reference guide to include a **search** field for fast lookup?

## Proposed Changes

---
### index.html (main UI & scoring logic)
- **Demo button fix** – add `onclick="skipToDemo()"` to the Demo button element.
- **Risk multiplier constants** – load from `risk_multipliers.json` into `REGION_RISK` and `SECTOR_RISK` objects.
- **UI addition – Risk Settings tab**:
  - New `<div id="risk-settings" class="tabcontent">` with dropdowns for region & sector, numeric input fields pre‑filled with defaults, and a **Save** button.
  - Hook the inputs to global variables `userRegionFactor` and `userSectorFactor` that override the defaults in `calculateScores()`.
- **modify `calculateScores()`** to apply:
  ```js
  const regionFactor = userRegionFactor || REGION_RISK[selectedRegion];
  const sectorFactor = userSectorFactor || SECTOR_RISK[selectedSector];
  finalScore = baseScore * regionFactor * sectorFactor;
  ```
- **Policy Review domain** – add three new question objects to `DOMAINS` (as previously planned).
- **Supplier Evidence UI** – file input (`<input type="file" multiple accept="image/*,application/pdf" />`), JS handler that:
  1. Stores file objects in `answers.supplierEvidence` (as Base64 strings).
  2. Generates a thumbnail using `URL.createObjectURL` for images; for PDFs, uses a lightweight `pdfjsLib.getDocument` to render page 1 to a canvas and convert to data URL.
  3. Displays each thumbnail with **Download** (`<a download>`). 
- **Quick Reference Guide** – add a **Help** icon (`<button id="help-btn">?`), on click opens a modal containing the HTML rendering of `QUICK_REFERENCE.md` (converted via a simple Markdown‑to‑HTML function).

---
### risk_multipliers.json (new file)
```json
{
  "region": {
    "EU": 1.2,
    "US": 1.1,
    "APAC": 1.3,
    "LATAM": 1.15,
    "AFRICA": 1.25
  },
  "sector": {
    "Finance": 1.3,
    "Healthcare": 1.2,
    "Manufacturing": 1.1,
    "Technology": 1.05,
    "Public": 1.25
  }
}
```
*These values are placeholders and can be edited by the user via the Risk Settings tab.*

---
### frameworks.json (unchanged from previous plan) – remains the source of framework definitions.

---
### QUICK_REFERENCE.md (existing) – no changes needed; it will be loaded into the modal.

---
### README.md (documentation update)
- Add a **Quick Reference** section with a screenshot of the Help modal.
- Document the new **Risk Settings** tab and how users can override defaults.
- Explain the **Supplier Evidence** upload workflow (preview → download).

---
### branding.css (optional – for future branding variables) – unchanged.

## Verification Plan

### Automated Tests
- **Playwright script** will now also:
  1. Open the **Risk Settings** tab, verify default values are displayed.
  2. Change a region factor, submit a questionnaire, and assert the final score changes accordingly.
  3. Upload an image and a PDF, verify thumbnails appear and download links work.
  4. Open the **Help** modal and confirm the quick‑reference content is visible.

### Manual Verification
- Load the app locally in Chrome/Edge.
- Click **Demo** → confirm demo flow.
- Navigate to **Risk Settings**, adjust a factor, run a short quiz, and observe score change.
- Upload a sample PNG and a sample PDF, check thumbnail preview and that clicking **Download** saves the original file.
- Click the **Help** icon, ensure the quick‑reference guide displays correctly.

Once you approve the plan (and optionally provide the source for the latest multiplier values), I will generate a `task.md` checklist and start implementing the changes.
