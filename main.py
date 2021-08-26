import os
import time
from flask import Flask, Response

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
    epoch = int(time.time())
    return Response(response=str(epoch), mimetype='text/html')

if __name__=="__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)