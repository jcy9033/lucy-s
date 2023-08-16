@app.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        email = request.args.get('email')  # 이메일로 예약을 찾아
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM reservations_table WHERE email = %s", [email])
        reservations = cur.fetchall()
        cur.close()

        # 이제 reservations 변수에는 해당 이메일로 예약된 모든 이력이 들어있어.
        # 이걸 적절하게 포맷팅해서 반환해주면 되겠지.

        return str(reservations) + '\n', 200

    except Exception as e:
        print(e)
        return 'Error in retrieving reservations\n', 400