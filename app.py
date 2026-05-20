import os
from datetime import datetime
from flask import Flask, render_template  # Obavezno uvezi render_template

app = Flask(__name__)

# 1. POČETNA STRANICA (tvojsajt.com/)
@app.route('/')
def home():
    trenutno_vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Prosleđujemo vreme u index.html
    return render_template('index.html', vreme=trenutno_vreme)


# 2. NOVA STRANICA (tvojsajt.com/o-nama)
@app.route('/filmovi')
def o_nama():
    # Ova funkcija samo uzima o-nama.html iz templates foldera i prikazuje ga
    return render_template('filmovi.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
