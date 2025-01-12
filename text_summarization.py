from transformers import pipeline

# Initialize summarization pipeline with a pre-trained model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Summarize the input text
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Example usage
text = """
Artificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.
"""
summary = summarize_text(text)
print("Summary:", summary)
