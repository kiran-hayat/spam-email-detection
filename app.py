from flask import Flask, request, render_template
from joblib import load

# Initialize Flask app
app = Flask(__name__)

# Load the trained pipeline (includes both vectorizer and model)
pipeline = load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the email content from the form
        email_content = request.form['email']
        
        # Use the pipeline to predict the result
        prediction = pipeline.predict([email_content])
        
        # Convert prediction to a readable format
        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        
        return render_template('index.html', email=email_content, result=result)

if __name__ == '__main__':
    app.run(debug=True)
