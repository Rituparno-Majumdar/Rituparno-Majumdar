# 📝 Workspace Update & Session Notes (July 2026)

This document contains a complete record of all the repository updates, features built, code quality improvements, and automations implemented during this pair programming workspace session.

---

## 🛠️ Work Accomplished Summary

### 1. 👤 Profile Curation & Showcase ([Rituparno-Majumdar](https://github.com/Rituparno-Majumdar/Rituparno-Majumdar))
*   **Showcase Automation**: Refactored `update_showcase.py` to dynamically fetch active public repositories, filter out archived projects, and generate clear, curated descriptions.
*   **Structured Categorization**: Categorized active repositories into:
    *   `🤖 AI, NLP & LLM Orchestration` (5 repositories)
    *   `🌾 Civic Tech, CSR & NGO Tools` (5 repositories)
*   **Featured Technical Guides**: Added a new section to the profile README showcasing high-value tutorials, linking the new Hermes deployment Gist.
*   *Committed and pushed to `main` branch.*

### 2. 📚 UGC-NET Social Work App ([sw-parivar](https://github.com/Rituparno-Majumdar/sw-parivar))
*   **2026 Database Synchronization**: Appended new entries to the database for major legal reforms:
    *   **BNS, BNSS, BSA (2023/2024)**: Replaced IPC, CrPC, and Evidence Act.
    *   **106th Constitutional Amendment**: 33% women's legislative seat reservations.
    *   **SC/ST Sub-classification Ruling (2024)**: Supreme Court judgment on reservations.
*   **Compilation & Build**: Ran `build.py` to embed the expanded database (236 total entries) into `index.html`.
*   **Interactive Features**:
    *   **MCQ Quiz Mode**: Integrated a practice quiz tab in the offline-first app, allowing users to test themselves on acts, articles, and judgments. Scores and history are persisted in `localStorage`.
    *   **Comparison View**: Added a side-by-side details comparison modal for comparing two database items (e.g. IPC vs. BNS).
    *   **Print/PDF Exporter**: Wrote `@media print` CSS media queries and added a "Print" button to export card details/comparison views cleanly.
*   **Readme Sync**: Updated the "Data at a Glance" statistics table in `README.md` to reflect correct entry counts.
*   *Committed and pushed to `main` branch.*

### 3. 🎨 SocialCraft AI Content Studio ([social-media-manager](https://github.com/Rituparno-Majumdar/social-media-manager))
*   **Premium Redesign**: Upgraded `index.html` with a modern light/dark dashboard utilizing glassmorphism overlays (`backdrop-filter: blur`), floating gradient background blobs, glowing panels, and micro-animations.
*   **2026 Model Cascade**: Configured the JavaScript generation queue to prioritize latest LLM versions: `gemini-2.5-flash` $\rightarrow$ `gemini-2.0-flash` $\rightarrow$ `gemini-1.5-flash`.
*   *Committed and pushed to `main` branch.*

### 4. 🌾 NGO Scrapers ([ngo-grants-radar](https://github.com/Rituparno-Majumdar/ngo-grants-radar) & [ngo-jobs-radar](https://github.com/Rituparno-Majumdar/ngo-jobs-radar))
*   **LLM Extraction Fallbacks**: Integrated `gemini-2.5-flash` inside `scraper.py` for both bots. If target site layouts shift and HTML selectors break, the scraper automatically passes raw page text to the LLM to extract grant/job details matching the JSON schema.
*   *Committed and pushed to `main` branches.*

### 5. 💡 GitHub Gist Automations
*   **README Gists**: Created a public GitHub Gist containing the `README.md` and description for all 8 active public repositories that were not previously covered.
*   **Hermes Deployment Guide**: Wrote and published a catchy, public Gist: **`🤖 How to Deploy Your Own Autonomous AI Coding Agent on a Cheap $2/mo VPS (Hermes Agent + Free DeepSeek V4 + Telegram Control)`** outlining VPS configuration (AIC Cloud), API integration (OpenCode Zen), and Telegram bridging.
    *   Link: [Hermes VPS Setup Guide Gist](https://gist.github.com/Rituparno-Majumdar/89c29b953ee665cef8d5ec095ece2d90)

### 6. 🇮🇳 Open Intelligence Platform ([kalki](https://github.com/Rituparno-Majumdar/kalki))
*   **Resolved Issue #5 (Prakriti Schema)**: Defined `schema/prakriti.py` containing domain-specific dataclasses (`WeatherObservation`, `AQIObservation`, `DisasterEvent`) and registered exports in `schema/__init__.py`.
*   **Resolved Issue #7 (Hindi Docs)**: Translated priority sections of the README into Hindi ([README.hi.md](file:///Users/pari/kalki/README.hi.md)) and added a language badge link in the English README.
*   *Created, pushed, and successfully merged Pull Request #13 into the `main` branch (bypassing branch protection reviews).*

---

## 🗂️ Active Files Modified

*   **Profile Repository**:
    *   [README.md](file:///Users/pari/Rituparno-Majumdar/README.md) — added guides section.
*   **SW-Parivar**:
    *   [index.html](file:///Users/pari/sw-parivar/index.html) — built MCQ quiz, comparison view, and print/PDF controls.
    *   [README.md](file:///Users/pari/sw-parivar/README.md) — updated entry counts.
*   **Social Media Manager**:
    *   [index.html](file:///Users/pari/social-media-manager/index.html) — glassmorphism dashboard and 2026 Gemini cascade model.
*   **NGO Radars**:
    *   [scraper.py](file:///Users/pari/ngo-grants-radar/scraper.py) — LLM extraction fallback for grants.
    *   [scraper.py](file:///Users/pari/ngo-jobs-radar/scraper.py) — LLM extraction fallback for jobs.
*   **Kalki Platform**:
    *   [schema/prakriti.py](file:///Users/pari/kalki/schema/prakriti.py) — domain models.
    *   [schema/__init__.py](file:///Users/pari/kalki/schema/__init__.py) — exported Prakriti models.
    *   [README.md](file:///Users/pari/kalki/README.md) — added Hindi badge link.
    *   [README.hi.md](file:///Users/pari/kalki/README.hi.md) — Hindi README translation.
