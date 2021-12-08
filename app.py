from flask import Flask, jsonify, request
import requests


app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"msg" : "Pong!"})


@app.route('/translate', methods=['POST'])
def translate():
    req = request.json
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20211208T150414Z.e25f96f16efc7a4f.c6a8021be5fa064a7b6b06add108f6eb6c30c6c3"
    response = requests.get(url+"&text="+req['text']+"&lang="+req['lang'])

    return jsonify({"response" : response.json()})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
