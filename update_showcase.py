import urllib.request
import json
import re
import os

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

def generate_markdown_table(repos, username):
    # Filter out forks, the profile repository itself
    filtered_repos = []
    for r in repos:
        if r.get("fork"):
            continue
        name = r.get("name")
        if name.lower() == username.lower():
            continue
        filtered_repos.append(r)
        
    # Sort by stars, and then by last updated to highlight best projects first
    filtered_repos.sort(key=lambda x: (x.get("stargazers_count", 0), x.get("updated_at", "")), reverse=True)
    
    # Take top 6 core projects
    top_repos = filtered_repos[:6]
    
    table_lines = [
        "| 📁 Project Showcase | 📝 Description | 🛠️ Language | 📊 Stats |",
        "| :--- | :--- | :---: | :---: |"
    ]
    
    # Emoji mapping for different project themes based on keywords
    theme_emojis = {
        "readfluence": "🎯",
        "social-craft-ai": "📱",
        "ngo": "🌾",
        "bengali": "🗣️",
        "nlp": "🔬",
        "annotation": "🧪",
        "wiki": "🧠",
        "agent": "🤖",
        "kalki": "🇮🇳"
    }
    
    for r in top_repos:
        name = r.get("name")
        html_url = r.get("html_url")
        desc = r.get("description") or "No description provided."
        lang = r.get("language") or "Mixed"
        stars = r.get("stargazers_count", 0)
        forks = r.get("forks_count", 0)
        
        # Pick emoji based on keywords
        emoji = "🛠️"
        for kw, em in theme_emojis.items():
            if kw in name.lower() or kw in desc.lower():
                emoji = em
                break
                
        # Clean up description to prevent breaking GFM pipes
        desc = desc.replace("|", "\\|")
        
        table_lines.append(
            f"| {emoji} [**{name}**]({html_url}) | {desc} | `{lang}` | ⭐ {stars} &middot; 🍴 {forks} |"
        )
        
    return "\n".join(table_lines)

def update_readme():
    username = "Rituparno-Majumdar"
    repos = fetch_repos(username)
    if not repos:
        print("No repositories found or rate limit hit. Aborting update.")
        return
        
    table_md = generate_markdown_table(repos, username)
    
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        readme_path = "/Users/pari/Documents/GITPROJECTS/Rituparno-Majumdar/README.md"
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace content between placeholders
    pattern = r"<!-- START_SHOWCASE -->.*?<!-- END_SHOWCASE -->"
    replacement = f"<!-- START_SHOWCASE -->\n{table_md}\n<!-- END_SHOWCASE -->"
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Showcase table updated successfully in README.md.")
    else:
        print("Showcase placeholders not found in README.md.")

if __name__ == "__main__":
    update_readme()
