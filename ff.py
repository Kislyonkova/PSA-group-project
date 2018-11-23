from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/main/')
def main_page():

    return render_template('main_page.html')


@app.route('/<username>/')
def show_userprofile(username):
    #user_n = str(username).lower()
    user_data = db.get_user(username)
    return render_template('playlists.html', user=user_data)





if __name__ == '__main__':
    app.run(debug=True)






