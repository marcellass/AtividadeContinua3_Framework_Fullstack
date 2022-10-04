import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('ac_volei.html')

@app.route('/api/volei', methods=['POST'])
def jogo_volei():

    json = request.get_json()
    primeiro_nome = json['primeiro'].upper()
    ultimo_nome = json['ultimo'].upper()
    time_nome = json['time'].upper()
    combo = json['combo'].upper()
    return jsonify(primeiro=primeiro_nome, ultimo=ultimo_nome, time=time_nome, combo=combo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host='0.0.0.0', port=port)