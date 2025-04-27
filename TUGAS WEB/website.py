from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page1.html')

@app.route('/about')
def about():
    return render_template('page2.html')

@app.route('/contact')
def contact():
    return render_template('page3.html')

@app.route('/riwayat')
def riwayat():
    return render_template('page4.html')

if __name__ == '__main__':
    app.run(debug=True)