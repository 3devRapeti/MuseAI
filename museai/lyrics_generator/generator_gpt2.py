from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import os
import ast

def generate_lyrics_model(keywords):

    keywords = ast.literal_eval(keywords)
    prompt = ""

    for keyword in keywords:
        prompt += keyword
        prompt += ","

    keywords = prompt
     
    current_folder = os.path.dirname(__file__)
    model_path = os.path.join(current_folder, "model.pt")

    #Load the model to use it
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    model.load_state_dict(torch.load(model_path, weights_only=True, map_location='cpu'))
    model.eval()

    input_ids = tokenizer(keywords, return_tensors='pt').input_ids

    output = model.generate(input_ids, max_length=100, no_repeat_ngram_size=2, num_return_sequences=5, 
                            do_sample=True, temperature=0.9, pad_token_id=tokenizer.eos_token_id)

    lyrics = []
    for i in range(len(output)):
        lyrics.append(tokenizer.decode(output[i], skip_special_tokens=True))
    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].split("\n")    
    
    new_lyrics = []

    for i in range(len(lyrics)):
        new_lyrics += lyrics[i]

    return new_lyrics
