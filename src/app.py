from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/reader")
def main():
    return "Hello, Dear Reader!"
    
if __name__ == "__main__":
   app.run()
