import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Hola Mundo desde HEROKU :3</title>
            
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    color: #2c3e50;
                }
                button {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 15px 25px;
                    font-size: 16px;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                button:hover {
                    background-color: #2980b9;
                }
            </style>
        </head>
        <body>
            <h1>🌎 Hola Mundo desde HEROKU</h1>
            <button onclick="window.location.href='https://front-paas-production.up.railway.app/ '">
                Regresar
            </button>
        </body>
        </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)