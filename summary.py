from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_abstract(text, min_len=50):
    count = len(text.split())
    max_len = max(75, int(count * 0.5))

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return summary[0]['summary_text']
