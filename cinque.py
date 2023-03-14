from flask import Flask,render_template
app = Flask(__name__)

import datetime

@app.route('/', methods=['GET'])
def home():
    return render_template('tour5.html')

@app.route('/persona', methods=['GET'])
def persona():
    return render_template('persona.html', costo = 10)
    
@app.route('/gruppo', methods=['GET'])
def gruppo():
    return render_template('gruppo.html',costo = 8)

@app.route('/guida', methods=['GET'])
def guida():
    return render_template('gruppoGuida.html',costo = 12)

@app.route('/paginacosti', methods=['GET'])
def guida():
    return render_template('gruppoGuida.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)