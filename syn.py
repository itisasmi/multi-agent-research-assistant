from transformers import pipeline

synthesizer = pipeline("summarization", model="facebook/bart-large-cnn")

def synthesize_review(summaries):
    joined = "\n\n".join(summaries)
    limit = 1024
    tokens = joined.split()
    if len(tokens) > limit:
        joined = " ".join(tokens[:limit])

    result = synthesizer(
        joined,
        max_length=220,
        min_length=120,
        do_sample=False
    )

    return result[0]['summary_text']
