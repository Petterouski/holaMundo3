import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return '''
        <h1>Hola Mundo desde HEROKU</h1>
        <button onclick="window.location.href='https://front-paas-production.up.railway.app/ '">
            Regresar
        </button>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)