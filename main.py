from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True #displays runtime errors in the browser, too


page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sign Up</title>
    </head>
    <body>
        <h1>Signup</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new users
add_form = """
    <form action="/add" method="post">
        <label>
            <input type="text" name="username"/>
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""



@app.route('/')
def index():
    return form

