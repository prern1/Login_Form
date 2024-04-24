from flask import Flask,request
from flaskext.mysql import MySQL
from flask import Flask, render_template

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'Prerana_Patro'
app.config['MYSQL_DATABASE_PASSWORD'] = 'prerna23'
app.config['MYSQL_DATABASE_DB'] = 'Prerana_23'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)
@app.route('/create_user', methods=['POST'])
def create_user():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        username = request.form['username']
        password = request.form['password']
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return 'User created successfully'
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)