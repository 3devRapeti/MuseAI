from flask import Flask, request, jsonify
import generator

app = Flask(__name__)

@app.route('/process', methods=['POST'])

def process():
    keyword = request.get_json().get('input')
    lyrics = generator.generate_lyrics(keyword) 
    return jsonify({'lyrics': lyrics})

if __name__ == '__main__':
    app.run(debug=True)