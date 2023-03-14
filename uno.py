from flask import Flask,render_template
app = Flask(__name__)

import datetime

@app.route('/', methods=['GET'])
def home():
    return render_template('tour.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)