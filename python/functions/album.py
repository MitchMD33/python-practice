'''
1.Create a make album function 
2. The function should take two pieces of information 'artist name' and 'album title'.
3. Make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. 
4.Use the none to add an optional parameter to make_album() that allows you to store the number of songs on your album. If the calling line includes a value for the number of songs add that value to the album's dictionary. make at least one new function call that includes the number of songs on an album. 
'''


def make_album(artist_name, album_title, songs=None):
  """Stores the artist's album and songs. """  
  album = {'album': album_title, 'artist': artist_name}
  if songs:
    album['songs'] = songs
  return album

musician = make_album('joe bob', 'redneck album', songs=2)
musician_two = make_album('mj', 'white album', songs=10)
musician_three = make_album('black', 'red album', songs=12)
print(musician,musician_two,musician_three)