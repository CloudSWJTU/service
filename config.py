SECRET_KEY = '634589YAOyubo111'
# MySQL所在的主机名
HOSTNAME = '127.0.0.1'
# MySQL监听的端口号，默认3306
PORT = '3306'
# 连接MySQL的用户名，读者用自己设置的
USERNAME = "root"
# 连接MySQL的密码，读者用自己的
PASSWORD = "634589YAOyubo"
# MySQL上创建的数据库名称
DATABASE = "test"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
