from flask import Flask
import config
from models import Picture, db

app = Flask(__name__)

# 配置文件绑定
app.config.from_object('config')

db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
