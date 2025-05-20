import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(path):
    lines = reader.readtext(path, detail=0)
    return ' '.join(lines).strip()