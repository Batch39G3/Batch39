from flask import Flask, redirect, url_for, request, render_template
# Define a flask app
from flask import jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

