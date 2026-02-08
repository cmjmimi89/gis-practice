from pathlib import Path

# ===============================
# 새 프로젝트 만들 때 여기만 수정
PROJECT_ROOT = Path(r"E:\gis-projects\gis-practice-new")
# ===============================

FOLDERS = [
    "project",
    "project/notebooks",
    "project/scripts",

    "data",
    "data/raw",
    "data/processed",

    "output",
    "output/maps",
    "output/tables",

    "env",
    "docs"
]

FILES = {
    ".gitignore": """# data & output
data/
output/

# python
__pycache__/
.ipynb_checkpoints/
.env
*.log
""",
    "README.md": "# GIS Project\n\nAuto-generated project structure."
}


def create_scaffold():
    for folder in FOLDERS:
        (PROJECT_ROOT / folder).mkdir(parents=True, exist_ok=True)

    for filename, content in FILES.items():
        path = PROJECT_ROOT / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print("✅ Project scaffold created:", PROJECT_ROOT)


if __name__ == "__main__":
    create_scaffold()
