from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '10.0.1.4'
app.config['MYSQL_USER'] = 'azureuser'
app.config['MYSQL_PASSWORD'] = '1q2w3e4r####'
app.config['MYSQL_DB'] = 'lucys'

mysql = MySQL(app)

@app.route ('/')
def home():
    return 'Hello World!' + '\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) # Debug mode enabled

@app.route ('/reservations')
def reservations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM reservationsTable")
    data = cur.fetchall()
    return str(data) + '\n'
