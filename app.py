from flask import Flask, render_template
from api import Crypto
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

# Creating a connection cursor


# Executing SQL Statements
#cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
#cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
#cursor.execute(''' DELETE FROM table_name WHERE condition ''')

# Saving the Actions performed on the DB
#mysql.connection.commit()

# Closing the cursor
#cursor.close()



crypto = Crypto()


@app.route("/")
def hello_world():
    results = crypto.get_top_10()

    cursor = mysql.connection.cursor()
    cursor.execute('TRUNCATE david')

    for obj in results:
        name = obj.get('name')
        symbol = obj.get('symbol')
        slug = obj.get('slug')
        price = obj['quote']['USD']['price']
        last_updated = obj.get('last_updated')
        cursor.execute(f"INSERT INTO david (crypto_name,symbol,slug,price,last_updated) VALUES ('{name}','{symbol}','{slug}', {price}, '{last_updated}')")
    mysql.connection.commit()
    cursor.close()
    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run(debug=True)
