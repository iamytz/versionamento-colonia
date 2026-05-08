from flask import Flask,render_template
import pyodbc



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("repositorio.html")









if __name__ == "__main__":
    app.run(debug=True)