# based on 8-7.py, add a while loop


# make an album
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


active = 1
while active:
    singer = input("Enter singer name: ")
    if singer == 'quit':
        active = 0
    else:
        album = input("Enter album name: ")
        if album == 'quit':
            active = 0
        else:
            number = input("Enter number of songs: ")
            if number == 'quit':
                active = 0
            elif number == '':
                info = make_album(singer, album)
                print(info)
            elif number != '':
                info = make_album(singer, album, number)
                print(info)
