import openai

# set OpenAI API key
openai.api_key = "sk-p..."

def generate_lyrics_model(keywords):
    prompt = f"{', '.join(keywords)}"
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",  
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant that writes lyrics based on given keywords."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.7,
    #     max_tokens=200  
    # )

    #return response['choices'][0]['message']['content']
    return "I'm in a field of Dandellions, wishing on everyone that you'll be mine.."

keywords = ["rain", "night", "alone"]
lyrics = generate_lyrics_model(keywords)
print(lyrics)