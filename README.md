# 📧 Email/SMS Spam Classifier

This is a deployed **machine learning project** that classifies a given Email or SMS message as **Spam** or **Not Spam** using Natural Language Processing (NLP). It uses a Naive Bayes classifier trained on labeled spam data and is deployed using Flask on Render.

🔗 **Live App**: [https://email-sms-spam-classifier-qfmk.onrender.com](https://email-sms-spam-classifier-qfmk.onrender.com)

---

## 🚀 Features

- Accepts user input (text message) through a web form
- Preprocesses the message using NLP techniques
- Transforms text with a TF-IDF vectorizer
- Predicts whether the message is **Spam** or **Not Spam**
- Clean and minimal user interface with Flask and HTML/CSS
- Deployed on Render with easy access for demonstration

---

## 🧠 Technologies Used

| Tool          | Purpose                              |
|---------------|---------------------------------------|
| Python        | Core programming language             |
| Flask         | Web application framework             |
| Pandas        | Data handling and processing          |
| Scikit-learn  | Machine Learning and vectorization    |
| NLTK          | Text preprocessing (tokenizing, stemming, stopword removal) |
| HTML/CSS      | Frontend design                       |
| Render        | Hosting and deployment                |

---

## 📊 Dataset

The dataset used is the classic SMS Spam Collection Dataset (`spam.csv`), containing labeled messages as `spam` or `ham`.

---

## 🧹 Preprocessing Pipeline

1. Lowercasing
2. Tokenization
3. Removing special characters and punctuation
4. Removing stopwords
5. Stemming
6. TF-IDF vectorization

---

## 🧪 Model Training

- **Model Used**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF
- **Training Steps**:
  - Cleaning and preprocessing
  - Splitting into train/test sets
  - Fitting TF-IDF vectorizer and model
  - Saving the model and vectorizer using `pickle`

---

## 🖥 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Shivampatil412/Email-SMS-Spam-Classifier.git
cd Email-SMS-Spam-Classifier

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# Visit http://localhost:5000 in your browser


⚙️ File Structure
Email-SMS-Spam-Classifier/
│
├── app.py                  # Flask web app
├── model.pkl               # Trained Naive Bayes model
├── vectorizer.pkl          # Trained TF-IDF vectorizer
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend form and display
├── sms_spam_detection.ipynb # Jupyter Notebook with full ML process
└── README.md

🛠 Deployment on Render
The app is deployed on Render, a free and easy-to-use cloud platform for hosting web apps. The deployment includes:
--> Setting up requirements.txt
--> Running app.py as the entry point
--> Auto-deployment from GitHub (if configured)

✍️ Author
Shivam Manohar Patil
Aspiring Data Scientist | Machine Learning Enthusiast
🔗 LinkedIn: https://www.linkedin.com/in/shivam-patil-697b2a143/

📜 License
This project is open-source and available under the MIT License.
