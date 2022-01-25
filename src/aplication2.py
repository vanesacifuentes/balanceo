from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running aplication2!'

    
if __name__ == '__main__':
    app.run(debug=True,  port=3001)