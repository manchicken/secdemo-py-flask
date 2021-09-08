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
app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'

