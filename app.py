from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route('/')
def main_for_now():
    return render_template('index.html')


@app.route('/search/')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    #songs = db.get_song(q)
    return render_template('search_results.html', q=q, users=users)



@app.route('/<username>/')
def show_userprofile(username):
    # user_n = str(username).lower()
    user_data = db.get_user(username)
    return render_template('playlists.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
