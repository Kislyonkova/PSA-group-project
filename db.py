# key - user login
# value - additional data
_users = {
    'katie': {
        'name': 'Katyusha',
        'job': 'Designer'
    },
    'alya': {
        'name': 'Alya',
        'job': 'PM'
    },
    'emil': {
        'name': 'Emil',
        'job': 'Programmer'
    },
    'seva': {
        'name': 'Seva',
        'job': 'Programmer'
    },
    'liza': {
        'name': 'Liza',
        'job': 'Designer'
    },
    'alexei': {
        'name': 'Lekha',
        'job': 'Designer'
    },
    'julia': {
        'name': 'Julia',
        'job': 'PR Manager'
    }

}


_music = {
    'song1': {
        'author': 'Monetochka',
        'title': 'Нет монет',
        'album cover': 'link_will_be_here'
    }

 }


def get_user(username):
    return _users.get(username)


# def get_song(song):
#    return _music.get(song)

_user_list = []
for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)  # add data from the 2nd dct to this one
    _user_list.append(_new_element)

def get_users_by_name(q):
    results = []
    for user in _user_list:
        if q.lower() in user['name'].lower():
            results.append(user)
    return results


_music_list = []
for uid, song_data in _music.items():
    _new_element = {'uid': uid}
    _new_element.update(song_data)
    _music_list.append(_new_element)


def get_song(q):
    results = []
    for song in _music_list:
        if q.lower() in song['author'].lower():
            results.append(song)
    return results
