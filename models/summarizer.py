from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn"
)

def generate_summary(text, instruction=None, max_length=180, min_length=60):
    if not text or len(text.strip()) < 30:
        return "⚠️ Not enough text to summarize."

    instruction = instruction.strip() if instruction else ""

    if "bullet" in instruction.lower() or "list" in instruction.lower():
        text = f"Summarize the following in bullet points:\n\n{text}"
    elif "tweet" in instruction.lower():
        text = f"Summarize this in tweet-style tone:\n\n{text}"
    elif "casual" in instruction.lower():
        text = f"Summarize in a casual, easy-to-understand tone:\n\n{text}"
    elif "key takeaways" in instruction.lower():
        text = f"List key takeaways:\n\n{text}"
    else:
        text = f"{instruction}\n\n{text}" if instruction else text

    # Default max_length/min_length
    max_length = 300
    min_length = 150

    # Override only if prompt says shorter
    if "100 words" in instruction:
        max_length = 130
        min_length = 90
    elif "70 words" in instruction:
        max_length = 90
        min_length = 60
    elif "short" in instruction.lower():
        max_length = 80
        min_length = 40
    elif "long" in instruction.lower() or "detailed" in instruction.lower():
        max_length = 400
        min_length = 250

    try:
        result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text'].strip()
    except Exception as e:
        return f"⚠️ Summarization error: {str(e)}"
