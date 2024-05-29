from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_model')
def about():
    return render_template('info.html')    

if __name__ == '__main__':
    app.run(host="0.0.0.0" , debug=True, port=5000)
