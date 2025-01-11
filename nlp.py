from transformers import pipeline

# Initialize the text generation pipeline with GPT-2
nlp_pipeline = pipeline('text-generation', model='gpt-2')

def process_user_input(user_input):
    # Use GPT-2 to generate a response based on user input
    response = nlp_pipeline(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']
