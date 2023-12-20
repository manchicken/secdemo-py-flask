# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# ************************************************
# * I cannot say this enough. This is demo code. *
# * Please do not use this code for anything     *
# * other than education on what not to do.      *
# * I am using this code to test security tools  *
# * which scan code for vulnerabilities.         *
# ************************************************


from flask import Flask
import json
import pymysql

DB_HOST = "localhost"
DB_USER = "appuser"
DB_PASSWORD = "apppassword"
DB_NAME = "appdb"

app = Flask(__name__)


def db_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        database=DB_NAME,
    )


@app.route('/')
def index():
    return 'OK'


@app.route('/key/<id>')
def keyLookupById(id):
    db = db_conn()
    curs = db.cursor()
    curs.execute(f"SELECT * FROM keys_and_values WHERE id={id}")
    rows = curs.fetchall()
    return json.dumps(rows)
