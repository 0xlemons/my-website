import os

os.system("pip3 install flask")
os.system("pip3 install uuid")
from flask import Flask, request, render_template
import uuid

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template('lemons.html')


if __name__ == '__main__':
    app.run(debug=True)
