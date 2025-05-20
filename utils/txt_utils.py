def save_summary_as_txt(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def extract_text_from_txt(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()
