from flask import Flask, render_template, request
from preprocessing import predict_mail_body

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        input_value = request.form['emailBody']
        result = predict_mail_body(input_value)
    return render_template('index.html', result=result)

@app.route('/about_model')
def about():
    return render_template('info.html')    

if __name__ == '__main__':
    app.run(host="0.0.0.0" , debug=True, port=5000)
