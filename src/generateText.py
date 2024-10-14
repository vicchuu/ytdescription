# for generating text using keywords ot phrase
# ip -> key word op -> long phrase

# src/generate.py
from transformers import pipeline

# Load the text generation model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')


def generate_description(input_text):
    #prompt = f"Keywords: {''.join(keywords)}.\n Write a detailed description based on these keywords:"
    #result = generator(keywords, max_length=100, do_sample=True, temperature=0.7,truncation=True)
    result = generator(
        input_text,
        max_length=250,               # Increase the length to generate more tokens
        num_return_sequences=1,        # Return only one sequence
        no_repeat_ngram_size=3,        # Avoid repetition of 3-grams
        temperature=0.7,               # Adjust temperature for creativity
        top_p=0.9,                     # Nucleus sampling for diversity
        do_sample=True,                # Enable sampling instead of greedy decoding
        eos_token_id=50256             # Use the end-of-sentence token to avoid incomplete sentences
    )
    generated_text = result[0]['generated_text']
    print(f"printed text : {generated_text}")
    # Remove the prompt from the generated text
    #description = generated_text[len(prompt):].strip()
    #print(f"Desc:{description}")
    return generated_text
