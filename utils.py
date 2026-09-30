from pathlib import Path

def check_project_structure():
    required = [
        Path("dataset/legitimate"),
        Path("dataset/phishing"),
        Path("models"),
        Path("results"),
        Path("src"),
    ]

    missing = [str(p) for p in required if not p.exists()]

    if missing:
        print("Missing folders:")
        for item in missing:
            print(" -", item)
        return False

    print("Project structure check: PASSED")
    return True
