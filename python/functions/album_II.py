def make_album(artist_name, album_title):
  """Stores the artist's album and songs. """  
  album = {'album': album_title, 'artist': artist_name}
  return album

while True:
  print(f"\nWhat is your artist's name")
  print("(enter 'q' at any time to quit)")
  
  a_name = input("enter artist name:")
  if a_name == 'q':
    break
  
  alb_name = input("enter album name:")
  if alb_name == 'q':
    break
  
  album_info = make_album(a_name, alb_name)
  print(f"Here is your album info:{album_info}")
  
