from flask import Flask
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '10.0.1.4'
app.config['MYSQL_USER'] = 'azureuser'
app.config['MYSQL_PASSWORD'] = '1q2w3e4r####'
app.config['MYSQL_DB'] = 'lucys'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) # Debug mode enabled

@app.route ('/')
def home():
    return 'Hello World!' + '\n'

# All Reservation history inquiry
@app.route ('/reservations')
def reservations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM reservations_table")
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return str(data) + '\n'

# Reserve
@app.route ('/reserve', methods=['POST'])
def reserve():
    try:
        request_data = request.get_json()
        name = request_data['name']
        email = request_data['email']
        phone = request_data['phone']
        seats = request_data['seats']
        seat_info = request_data['seat_info']
        datetime = request_data['datetime']
        status = '확정'

        # Check if the seat is already reserved
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM reservations_table WHERE datetime = %s AND seat_info = %s", (datetime, seat_info))
        if cur.fetchone():
            return 'Seat already reserved for this date and time.\n', 400
        
        # Insert new reservation
        cur.execute("INSERT INTO reservations_table (name, email, phone, seats, seat_info, datetime, status) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, email, phone, seats, seat_info, datetime, status))
        mysql.connection.commit()
        cur.close()
        return 'Reservation created successfully!\n', 201

    except Exception as e:
        print(e)
        return 'Error in reservations\n', 400

# Reservation history inquiry with Email
@app.route('/reservations/email', methods=['GET'])
def get_reservations():
    try:
        email = request.args.get('email')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM reservations_table WHERE email = %s", [email])
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()

        return str(data) + '\n', 200 # Check point. reservations()
    
    except Exception as e:
        print(e)
        return 'Error in retrieving reservations' + '\n', 400