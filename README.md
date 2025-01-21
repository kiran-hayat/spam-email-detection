# Spam Email Detection

This project implements a spam email detection system using machine learning. The goal is to classify emails as either "spam" or "ham" (non-spam). The system uses Natural Language Processing (NLP) techniques and a Naive Bayes classifier to predict whether an email is spam.

## Features

- **Spam Detection**: Classifies emails into "spam" and "ham".
- **NLP Pipeline**: Uses a CountVectorizer with bigrams to process the email text.
- **Model**: The project uses a Naive Bayes classifier (MultinomialNB) for classification.
- **Web Interface**: A Flask web application is included for easy deployment and user interaction.

## Files and Structure

- `app.py`: The main Flask application that serves the model and provides a web interface for testing.
- `templates/`: Contains the HTML templates for the Flask application.
  - `index.html`: The landing page for the web app.
- `model.pkl`: The trained spam detection model saved in a pickle format.
- `requirements.txt`: A list of dependencies required to run the project.
- `spam-email-detection.ipynb`: Jupyter notebook for data exploration, training the model, and evaluating performance.
- `spam.csv`: The dataset used for training the model.

## Requirements

To run this project, you need to install the following dependencies. You can install them using the `requirements.txt` file.

```bash
pip install -r requirements.txt
