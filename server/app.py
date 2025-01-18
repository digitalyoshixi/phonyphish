from flask import Flask 

app = Flask(__name__) # designates this script as the root apth

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__": # if running this file directly
    app.run(debug=True) # run the app
