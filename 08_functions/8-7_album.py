def make_album(singer, album, number_of_songs=''):
    if number_of_songs:
        album_info = {
            'singer': singer,
            'album': album,
            'number_of_songs': number_of_songs,
        }
    else:
        album_info = {
            'singer': singer,
            'album': album,
        }
    return album_info


info = make_album("The Beatles", "Yesterday")
print(info)

info = make_album("The Carpenters", "Yesterday once more")
print(info)

info = make_album("The Cranberries", "Dying in the sun", 9)
print(info)
