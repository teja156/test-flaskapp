from flask import Flask
host_name = "127.0.0.1"
portno = 80
app = Flask(__name__)

@app.route("/")
def runapp():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True,host=host_name,port=portno)