import easyocr

reader = None

def extract_text_from_image(path):
    global reader
    if reader is None:
        print("🧠 Loading EasyOCR model once...")
        reader = easyocr.Reader(['en'], gpu=False)

    lines = reader.readtext(path)

    # Sort top to bottom
    lines_sorted = sorted(lines, key=lambda x: x[0][0][1])
    texts = [line[1] for line in lines_sorted]

    # Keywords we consider as garbage
    blacklist_keywords = [
        "cnn.com", "cnn.org", "@cnn", "visit", "twitter", "instagram", "more information", "blog", ".com", ".org"
    ]

    cleaned = [
        t for t in texts
        if not any(kw.lower() in t.lower() for kw in blacklist_keywords)
    ]

    return ' '.join(cleaned).strip()
