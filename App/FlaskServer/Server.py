from flask import Flask, request, render_template, json, jsonify, redirect

app = Flask(__name__)


# TODO: Create server methods for later interface
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
