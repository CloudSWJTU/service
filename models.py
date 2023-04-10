from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:634589YAOyubo@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 定义模型类
class Picture(db.Model):
    __table_name__ = 'service_picture'
    picture_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    picture_name = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    upload_time = db.Column(db.Integer, unique=True)
    status = db.Column(db.String(80), unique=False)


@app.route('/')
def index():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    images_urls = [url_for('static', filename='uploads/' + image) for image in images]
    return render_template('fuwuquzhidao.html', images_urls=images_urls)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        get_picture_name = request.files.get('picture_name')
        the_picture = Picture(picture_name=get_picture_name)
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '上传成功'

    return index()


# 删除表
db.drop_all()
# 创建表
db.create_all()
# 添加数据
u1 = Picture(username='john', picture_name='yishitang')
u2 = Picture(username='susan', picture_name='yifu')
u3 = Picture(username='mary', picture_name='cainiao')
u4 = Picture(username='david', picture_name='shaokao')
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
