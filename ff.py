from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
    def show_userprofile():
        return 'Hello, %s' % username

@app.route('/user/<username>/<int:playlist_id>')
    def show_userplaylist(username, playlistid):
        return 'Users playlist'

@app.route('/user/<username>/recomendations')
    def show_userrecomendations(username):
        return 'Users recomendations'

@app.route('/playlist/<int:playlist_id>')
    def show_playlist(playlist_id):
        return 'Playlist'

@app.route('/song/<int:song_id>')
    def song(song_id):
        return 'Song page'


if __name__ == '__main__':
    app.run()






