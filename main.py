def replace(string, dictionary):
    for (k, v) in dictionary.items():
        string = string.replace(f"$({k})", v)
    return string

def get_skills_html(skills):
    base_url = "https://go-skill-icons.vercel.app/api/icons?i="
    skills_str = ",".join(sorted(skills))
    img_url = f"{base_url}{skills_str}&perline=8"

    return f"""
<p align="center">
    <a href="https://github.com/LelouchFR/skill-icons">
        <img src="{img_url}" />
    </a>
</p>
    """

with open("template.md", encoding="utf-8") as r:
    template = r.read()

replacements = {
    "skills": get_skills_html(["assembly", "arch", "bash", "c", "css", "element", "github", "html", "hyprland", "linux", "python", "rust", "vim", "vscode", "virtualbox", "tmux"])
}

template = replace(template, replacements)

with open("README.md", "w", encoding="utf-8") as w:
    w.write(template)
