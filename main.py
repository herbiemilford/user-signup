from flask import Flask, request, redirect, render_template



app = Flask(__name__)
app.config['DEBUG'] = True
form = '''<form action="/signup" method="POST">
   <label for ="username">Username
          <input type="text" name="username" value="{{username}}" />
          <p>{{username_error}}</p>
</label>

<label for="password">Password
          <input type="password" name="password" value="{{password}}" />
          <p>{{password_error}}</p>
<label for = "verify>Verify Password
          <input type="password" name="verify" value="{{verify}}" />
          <p>{{verify_error}}</p>
</label>
<label for="email">Email
          <input type="text" name="email" value="{{email}}" />
          <p>{{email_error}}</p>
<label>
          <input type="submit" name="submit" value="Submit">
</label>
        </form>


'''
@app.route("/")
def index():
    return form

app.run()