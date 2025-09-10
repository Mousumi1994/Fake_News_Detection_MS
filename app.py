from flask import Flask, request, render_template
from model import news_classifier  # Import your model
import os

app = Flask(__name__)


@app.route('/')
def home():
     return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    # Use your model here
    if request.method == 'POST':
        news_text = request.form['news_text']

    result = news_classifier(news_text)

    if result[0]['label'] == 'LABEL_0':
        prediction = 'FAKE'
    else:
        prediction = 'REAL'

    result_text = f"The news is likely: {prediction}"
    return render_template('index.html', prediction_text=result_text, original_text=news_text)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
