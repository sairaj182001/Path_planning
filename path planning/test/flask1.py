import random
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    print(request.remote_addr)
    rand = random.randint(1,100000)
    return f"<h1>hello {request.remote_addr}</h1><img src = 'https://picsum.photos/seed/{rand}/200/300'/>"

if __name__ == "__main__":
    app.run()
