from transformers import GPT2LMHeadModel, GPT2Tokenizer

class Chatbot:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def chat(self, user_input):
        # Encode the input and generate a response
        inputs = self.tokenizer.encode(user_input, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
        
        # Decode the output and return the result
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Example usage
chatbot = Chatbot()
response = chatbot.chat("Hello, how are you?")
