import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (this allows requests from any domain)
CORS(app)

# Load the model, vectorizer, and label encoder
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open('label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

# API route for predicting genre
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get lyrics from the POST request
        data = request.get_json(force=True)
        lyrics = data['lyrics']

        # Transform lyrics using the vectorizer
        lyrics_tfidf = vectorizer.transform([lyrics])

        # Predict the genre using the trained model
        predicted_label = model.predict(lyrics_tfidf)

        # Decode the predicted label to the genre
        predicted_genre = label_encoder.inverse_transform(predicted_label)

        # Return the predicted genre as a JSON response
        return jsonify({'genre': predicted_genre[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
