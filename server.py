from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    return '', 200

if __name__ == '__main__':
    app.run(port=8080)
