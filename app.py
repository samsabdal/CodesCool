from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    print('-------------------------Hello Coding-------------------------------')
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    if not name or not email:
        return redirect(url_for('index'))
    return render_template('submit.html', name=name, email=email)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)