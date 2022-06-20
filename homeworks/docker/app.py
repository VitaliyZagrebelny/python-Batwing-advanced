from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Welcome!'

@app.route('/name')
def name():
    return "Vitalii Zahrebelniy"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)