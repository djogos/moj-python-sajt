import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

# Glavna stranica
@app.route('/')
def home():
    trenutno_vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html lang="sr">
    <head>
        <meta charset="UTF-8">
        <title>Moj Prvi Python Sajt</title>
        <style>
            body {{ font-family: sans-serif; text-align: center; margin-top: 50px; background: #eef2f7; color: #333; }}
            .container {{ background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #3776AB; }} /* Python plava boja */
            p {{ font-size: 18px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Čestitamo! 🐍</h1>
            <p>Tvoj Python + Flask sajt uspešno radi na Renderu!</p>
            <small>Trenutno vreme na serveru: {trenutno_vreme}</small>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Render zahteva da uzmemo PORT iz okruženja (environment varijable)
    port = int(os.environ.get("PORT", 5000))
    # Na tvom računaru će raditi na portu 5000, a na Renderu na portu koji oni odrede
    app.run(host="0.0.0.0", port=port)