import urllib.request
import json
import re
import os

# Curated data for existing repositories
CURATED_PROJECTS = {
    "obsidian-llm-wiki-kit": {
        "name": "obsidian-llm-wiki-kit",
        "emoji": "🧠",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "A prompt-engineering starter kit for building a self-growing personal knowledge base in Obsidian, implementing Andrej Karpathy's LLM Wiki pattern."
    },
    "opencode-research-agents": {
        "name": "opencode-research-agents",
        "emoji": "🤖",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "A multi-agent research orchestration system running inside OpenCode, using epistemic parallelism to save synthesized findings to Obsidian."
    },
    "social-media-manager": {
        "name": "social-media-manager",
        "emoji": "🎨",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "**SocialCraft AI**: Zero-install client-side AI tool generating platform-optimized posts in 13 Indian regional languages using the Gemini API."
    },
    "bengali-annotation-job-alert": {
        "name": "bengali-annotation-job-alert",
        "emoji": "🗣️",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "Automated job monitor scraping LinkedIn, Remotive & RSS for Bengali AI data annotation and NLP roles, with Telegram alerts via GitHub Actions."
    },
    "bengali-annotation-quality": {
        "name": "bengali-annotation-quality",
        "emoji": "🧪",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "Annotation quality assessment pipeline calibrating Bengali sentiment datasets with Cohen's Kappa, disagreement analysis, and bias evaluation."
    },
    "kalki": {
        "name": "kalki",
        "emoji": "🇮🇳",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "**Kalki**: India's Open Intelligence Platform — open-source early-warning signals from public data to foresee climate, health, and economic crises."
    },
    "ngo-grants-radar": {
        "name": "ngo-grants-radar",
        "emoji": "🌾",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Automated grant call monitoring for NGOs — tracks open funding opportunities from institutional donors and delivers Telegram alerts via GitHub Actions."
    },
    "ngo-jobs-radar": {
        "name": "ngo-jobs-radar",
        "emoji": "💼",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Automated NGO and social sector job alert pipeline — monitors 6 platforms and delivers real-time Telegram notifications via GitHub Actions."
    },
    "ngo-mis-toolkit": {
        "name": "ngo-mis-toolkit",
        "emoji": "📊",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "CLI toolkit for NGO reporting, logframe management & CSR compliance tracking in India. Generate donor-ready Word reports and validate LFA indicators."
    },
    "sw-parivar": {
        "name": "sw-parivar",
        "emoji": "📚",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Indian Social Work Knowledge Base — offline-first reference vault of laws, schemes, judgments, and UGC-NET frameworks for field practitioners."
    },
    "forest-rights-claim": {
        "name": "forest-rights-claim",
        "emoji": "🌿",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Offline-first FRA 2006 land claim mapping tool for tribal communities — trace GPS boundaries on Leaflet and generate official Schedule I Form A PDFs."
    },
    "bail-draft-builder": {
        "name": "bail-draft-builder",
        "emoji": "⚖️",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Interactive BNSS Section 479 under-trial bail eligibility calculator — computes detention threshold and generates formal, court-ready bail petitions."
    },
    "pds-audit-portal": {
        "name": "pds-audit-portal",
        "emoji": "📦",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Automated audit engine for India's Public Distribution System — detects duplicate ration cards, allocation shortfalls, and suspicious cancellation hotspots."
    },
    "voice-reporting-companion": {
        "name": "voice-reporting-companion",
        "emoji": "🎙️",
        "category": "🌾 Civic Tech, CSR & NGO Tools",
        "description": "Offline-first voice-to-JSON health reporting tool for ASHA and Anganwadi workers — auto-parses speech into NHM child health forms and stores in IndexedDB."
    },
    "kappabench": {
        "name": "kappabench",
        "emoji": "📊",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "Agreement and consensus benchmarking framework for LLM-as-a-judge classifiers — calculates Cohen's Kappa, Fleiss' Kappa, and Krippendorff's Alpha."
    },
    "markdownmind": {
        "name": "markdownmind",
        "emoji": "🧠",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "Autonomous knowledge graph synthesizer for Markdown vaults — structures links, clusters topics, detects orphan files, and generates summaries."
    },
    "promptshield": {
        "name": "promptshield",
        "emoji": "🛡️",
        "category": "🤖 AI, NLP & LLM Orchestration",
        "description": "Defensive LLM structured extraction validation middleware — guards against prompt injections and repairs truncated JSON responses."
    }
}

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github.v3+json"}
    )
    # Use GITHUB_TOKEN if available to avoid rate limits in GitHub Actions
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"token {token}")
        
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching repositories: {e}")
        return []

def get_repo_metadata(repo):
    name = repo.get("name")
    desc = repo.get("description") or ""
    
    # Check if we have curated data for this repo
    if name in CURATED_PROJECTS:
        return CURATED_PROJECTS[name]
        
    # Auto-detect category & emoji for any new repos added in the future
    text = (name + " " + desc).lower()
    
    if "ngo" in text or "grant" in text or "civic" in text or "kalki" in text or "social-work" in text or "csr" in text or "compliance" in text:
        category = "🌾 Civic Tech, CSR & NGO Tools"
        emoji = "🌾"
    elif "agent" in text or "wiki" in text or "llm" in text or "bengali" in text or "nlp" in text or "ai" in text or "prompt" in text or "model" in text or "mcp" in text or "skill" in text:
        category = "🤖 AI, NLP & LLM Orchestration"
        emoji = "🤖"
    elif "annotation" in text or "label" in text or "coco" in text or "yolo" in text or "dataset" in text or "augment" in text or "synthetic" in text:
        category = "🏷️ Data Annotation & Labeling"
        emoji = "🏷️"
    elif "document" in text or "pdf" in text or "rag" in text or "chunk" in text or "converter" in text or "extract" in text:
        category = "📄 Document Processing & RAG"
        emoji = "📄"
    elif "cli" in text or "terminal" in text or "productivity" in text or "workflow" in text or "automation" in text or "monitor" in text:
        category = "🛠️ CLI Tools & Productivity"
        emoji = "🛠️"
    elif "code-quality" in text or "security" in text or "lint" in text or "over-engineering" in text or "yagni" in text or "code-review" in text or "dependency" in text:
        category = "✅ Code Quality & Security"
        emoji = "✅"
    else:
        category = "Other Projects"
        emoji = "🛠️"
        
    return {
        "name": name,
        "emoji": emoji,
        "category": category,
        "description": desc or "No description provided."
    }

def generate_showcase(repos, username):
    # Filter out forks, archived repos, and the profile repository itself
    active_repos = []
    for r in repos:
        if r.get("fork"):
            continue
        if r.get("archived"):
            continue
        name = r.get("name")
        if name.lower() == username.lower():
            continue
        active_repos.append(r)
        
    # Sort repos by stars (descending), then updated_at (descending)
    active_repos.sort(key=lambda x: (x.get("stargazers_count", 0), x.get("updated_at", "")), reverse=True)
    
    # Group repositories by category
    grouped_repos = {}
    for r in active_repos:
        meta = get_repo_metadata(r)
        category = meta["category"]
        if category not in grouped_repos:
            grouped_repos[category] = []
        
        # Keep original language & url from api
        meta["html_url"] = r.get("html_url")
        meta["language"] = r.get("language") or "Mixed"
        grouped_repos[category].append(meta)
        
    # Define desired category ordering
    category_order = [
        "🤖 AI, NLP & LLM Orchestration",
        "🏷️ Data Annotation & Labeling",
        "📄 Document Processing & RAG",
        "🛠️ CLI Tools & Productivity",
        "✅ Code Quality & Security",
        "🌾 Civic Tech, CSR & NGO Tools",
        "Other Projects"
    ]
    
    showcase_md = []
    
    for cat in category_order:
        if cat not in grouped_repos or not grouped_repos[cat]:
            continue
            
        showcase_md.append(f"### {cat}\n")
        showcase_md.append("| Project | Description | Language |")
        showcase_md.append("| :--- | :--- | :---: |")
        
        for p in grouped_repos[cat]:
            name = p["name"]
            html_url = p["html_url"]
            emoji = p["emoji"]
            desc = p["description"].replace("|", "\\|")
            lang = p["language"]
            
            showcase_md.append(f"| {emoji} [**{name}**]({html_url}) | {desc} | `{lang}` |")
            
        showcase_md.append("") # empty line after table
        
    return "\n".join(showcase_md).strip()

def update_readme():
    username = "Rituparno-Majumdar"
    repos = fetch_repos(username)
    if not repos:
        print("No repositories found or rate limit hit. Aborting update.")
        return
        
    showcase_md = generate_showcase(repos, username)
    
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        readme_path = "/Users/pari/Rituparno-Majumdar/README.md"
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace content between placeholders
    pattern = r"<!-- START_SHOWCASE -->.*?<!-- END_SHOWCASE -->"
    replacement = f"<!-- START_SHOWCASE -->\n{showcase_md}\n<!-- END_SHOWCASE -->"
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Showcase table updated successfully in README.md.")
    else:
        print("Showcase placeholders not found in README.md.")

if __name__ == "__main__":
    update_readme()
