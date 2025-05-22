model = None
tokenizer = None

def generate_summary(text, instruction=None):
    global model, tokenizer

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
    elif instruction:
        text = f"{instruction}\n\n{text}"

    # Default max/min length
    max_length = 300
    min_length = 150

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
        if model is None or tokenizer is None:
            from transformers import BartTokenizer, BartForConditionalGeneration
            import torch
            tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
            model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

        inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()
    except Exception as e:
        return f"⚠️ Summarization error: {str(e)}"
