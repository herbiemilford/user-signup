from flask import Flask, request, redirect, render_template



app = Flask(__name__)
app.config['DEBUG'] = True
form = '''<form action="/signup" method="POST">
   <label for ="username">Username
          <input type="text" name="username" value=" " />
          <p></p>
</label>

<label for="password">Password
          <input type="password" name="password" value="" />
          <p></p>
<label for = "verify">Verify Password
          <input type="password" name="verify" value="" />
          <p></p>
</label>
<label for="email">Email
          <input type="text" name="email" value=" " />
          <p></p>
<label>
          <input type="submit" name="submit" value="Submit">
</label>
        </form>


'''
@app.route("/")
def index():
    return render_template('index.html', title = "Sign UP")
 

@app.route("/signup", methods = ['POST'])
def signup():

    username = request.form ["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "": #validate username
        username_error = "Enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters in length."
        username = ""
    elif " " in username:
        username_error = "Username cannot contain spaces."
        username = ""


    if password == "":  #validate password
        password_error = "Enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters in length."
    elif " " in password:
        password_error = "Password cannot contain spaces."

    if verify == "" or verify != password: #verify password
        verify_error = "Passwords do not match. Try again."
app.run()