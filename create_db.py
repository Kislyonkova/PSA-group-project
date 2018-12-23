import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''
CREATE TABLE users_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    name TEXT,
    password TEXT,
    email TEXT,
    photo TEXT
)
''')
conn.commit()

c.execute('''
    INSERT INTO users_data (name, password, email)
    VALUES ('Katie', 'test1', 'test2')
''')
conn.commit()

# changed the table structure
# added column 'login' & committed changes
c.execute('''
    ALTER TABLE users_data
    ADD COLUMN login TEXT
''')
conn.commit()

# updated tha table and change login to smth
c.execute('''
    UPDATE users_data
    SET login='katie'
    WHERE name='Katie'
''')
conn.commit()

#
c.execute('''
   ALTER TABLE users_data
   ADD COLUMN photo TEXT
''')
conn.commit()

# convert data and insert to table
users_data = [
    {'login': 'alya',
     'name': 'Alya',
     'password': '123',
     'email': 'abc@gmail.com',
     'photo': 'link'},

    {'login': 'katyusha',
     'name': 'Katie',
     'password': '1234',
     'email': 'gg@gmail.com',
     'photo': 'link'},

    {'login': 'julia',
     'name': 'Julia',
     'password': 'lovecleaningup',
     'email': 'cleaner@gmail.com',
     'photo': 'link'},

    {'login': 'kirill',
     'name': 'Kirill',
     'password': 'clevertop',
     'email': 'kkk00@gmail.com',
     'photo': 'link'},

    {'login': 'alexei',
     'name': 'Lekha',
     'password': '3435u435y47535',
     'email': 'alexei@gmail.com',
     'photo': 'link'},

    {'login': 'liza',
     'name': 'Liza',
     'password': 'plane',
     'email': 'loveplanes@gmail.com',
     'photo': 'link'},

    {'login': 'seva',
     'name': 'Seva',
     'password': '13242424343',
     'email': 'seva@gmail.com',
     'photo': 'link'}
]

for user in users_data:
    c.execute("INSERT INTO users_data"
              "(login, name, password, email, photo)"
              "VALUES "
              "('{login}', '{name}', '{password}', '{email}', '{photo}')".format(**user))
    conn.commit()

# USER PLAYLISTS
c.execute('''
CREATE TABLE user_playlists (
    user_user INTEGER,
    user_id INTEGER,
    playlist_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users_data(user_id),
    FOREIGN KEY(playlist_id) REFERENCES playlist_info(playlist_id)
)
''')
conn.commit()

# NOT EXECUTED YET
c.execute("SELECT u.* "
          "FROM users_playlists up"
          "JOIN users_data u ON (u.id = up.user_id "
          "WHERE ue.event_id=1")

# PLAYLISTS content
c.execute('''
CREATE TABLE playlists_info (
    playlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    playlist_title TEXT,
    description TEXT,
    hashtags TEXT,
    author_login INTEGER,
    photo TEXT 
)
''')
conn.commit()

playlists = [
    {'playlist_id': '1',
     'playlist_title': 'November Sadness',
     'description': 'desc',
     'hashtags': '#pop, #electronic #sad',
     'author_login': 'liza',
     'photo': 'https://raw.githubusercontent.com/Kislyonkova/PSA-group-project/master/images/songs_playlists/-7YRDIiKTjA.jpg'},

    {'playlist_id': '2',
     'playlist_title': 'Morning inspiration',
     'description': 'desc2',
     'hashtags': '#pop #happy #morning #hits ',
     'author_login': 'alya',
     'photo': 'https://raw.githubusercontent.com/Kislyonkova/PSA-group-project/master/images/songs_playlists/morning.jpg'}
]
for playlist in playlists:
    c.execute("INSERT INTO playlists_info"
              "(playlist_id, playlist_title, description, hashtags, author_login, photo)"
              "VALUES "
              "('{playlist_id}', '{playlist_title}', '{description}', "
              "'{hashtags}', '{author_login}', '{photo}')".format(**playlist))
    conn.commit()

# SONGS
c.execute('''
CREATE TABLE songs_db (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist TEXT,
    title TEXT,
    genre TEXT,
    photo TEXT)
''')
conn.commit()

songs = [
    {'song_id': '1',
     'artist': 'Son Lux',
     'title': 'Lost It to Trying',
     'genre': 'test_genre',
     'photo': 'https://raw.githubusercontent.com/Kislyonkova/PSA-group-project/master/images/songs_playlists/sonlux.jpg'},

    {'song_id': '2',
     'artist': 'Монеточка',
     'title': 'Нет монет',
     'genre': 'test_genre_2',
     'photo': 'https://raw.githubusercontent.com/Kislyonkova/PSA-group-project/master/images/songs_playlists/monetochka.jpg'}
]

for song in songs:
    c.execute("INSERT INTO songs_db"
              "(song_id, artist, title, genre, photo)"
              "VALUES "
              "('{song_id}', '{artist}', '{title}', '{genre}', '{photo}')".format(**song))
    conn.commit()

# PLAYLISTS & SONGS
c.execute('''
CREATE TABLE playlists (
    playlist_song_id INTEGER,
    playlist_id INTEGER,
    song_id INTEGER,
    FOREIGN KEY(playlist_id) REFERENCES playlists_info(playlist_id),
    FOREIGN KEY(song_id) REFERENCES songs_db(song_id)
)
''')
conn.commit()

# FIX THAT
playlist_content = [
    {'playlist_song_id': '12',
     'playlist_id': '1',
     'song_id': '2'},

    {'playlist_song_id': '123',
     'playlist_id': '2',
     'song_id': '2'}
]
