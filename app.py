from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    variable = 10
    cars = {
      "Agam": "Maruti 800",
      "Yash": "Mercedes", 
      "Boss": "Jisme ladkiyan ho"
    }
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 