# Where have you been (iphone)
Simplify version of Facebook tagging
img = PIL.Image.open("image direction")
exif_data = img._getexif()
exif_data

# you will see the detail of the picture in a python dictionary type
{271: 'Apple',          # this is my cellphone type
 272: 'iPhone 6s',
 274: 1,
 282: (72, 1),
 283: (72, 1),
 296: 2,
 305: '9.3.4',
 306: '2016:09:10 16:45:51',  # Date and time
 531: 1,
 33434: (1, 1083),
 33437: (11, 5),
 34665: 204,
 34850: 2,
 34853: {1: 'N',                              # in the key [34853], it contain the coordination information.
  2: ((21, 1), (54, 1), (678, 100)),          # the formate is (degree, minutes, seconds) N:21;54;6.78 E:120;8.01
  3: 'E',                                     # transformation formular = degree + (minutes)/60 + (seconds)/3600
  4: ((120, 1), (51, 1), (801, 100)),
  5: b'\x00',
  6: (14747, 418),
  7: ((8, 1), (45, 1), (5100, 100)),
  12: 'K',
  13: (0, 1),
  16: 'T',
  17: (60189, 179),
  23: 'T',
  24: (60189, 179),
  29: '2016:09:10',
  31: (5, 1)},
 34855: 25,
