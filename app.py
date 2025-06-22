from flask import Flask, request, render_template
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load NLTK assets
# nltk.download('punkt')
# nltk.download('stopwords')
import nltk
nltk.data.path.append("./nltk_data")  

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    transformed_message = transform_text(message)
    vector_input = tfidf.transform([transformed_message])
    result = model.predict(vector_input)[0]
    
    prediction = "Spam" if result == 1 else "Not Spam"
    
    return render_template('index.html', prediction_text=f'Prediction: {prediction}')

if __name__ == "__main__":
    app.run(debug=True)
