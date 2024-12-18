import openai

# set OpenAI API key
openai.api_key = ""

def generate_lyrics_model(keywords):
    prompt = f"{', '.join(keywords)}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes lyrics based on given keywords."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200  
    )

    content = response['choices'][0]['message']['content']
    paragraphs = content.split("\n\n")
    paragraphs = [p.split("\n") for p in paragraphs]
    new_paragraphs = []
    for i in range (len(paragraphs)):
        for j in range (len(paragraphs[i])):
            new_paragraphs.append(paragraphs[i][j])
        new_paragraphs.append("\n")
    paragraphs = new_paragraphs
    return paragraphs

keywords = ["rain", "night", "alone"]
lyrics = generate_lyrics_model(keywords)
print(lyrics)