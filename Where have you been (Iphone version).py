
# coding: utf-8

# # import module
# ### module PIL.Image is for extract GPS information from pictures
# ### module os is for setting directory

# In[11]:

import PIL.Image
import os


# ### Setting the picture destination

# In[20]:

my_dir = r'C:\Users\User\Desktop\photo'
os.chdir = r'C:\Users\User\Desktop\photo'
pictures =os.listdir(my_dir)
img_list = os.listdir( r'C:\Users\User\Desktop\photo')
direct =  my_dir +'\\'+str(img_list[0])


# In[24]:

latitudes = []
longitudes = []


# ## Function of extracting coordination 

# In[26]:

def extract_coorditation(direct):
    img = PIL.Image.open(direct)
    exif_data = img._getexif()
    exif_data
    coordination = exif_data[34853]
    horiz = coordination[2]
    verti = coordination[4]
    lati = round ((horiz[0][0] + horiz[1][0]/60+horiz[2][0]/(horiz[2][1]*3600)),3 )
    longi = round ((verti[0][0] + verti[1][0]/60+verti[2][0]/(verti[2][1]*3600) ),3)
    latitudes.append(lati)
    longitudes.append(longi)


# In[27]:

for picture in pictures:
    direct =  my_dir +'\\'+picture
    extract_coorditation (direct)


# In[28]:

print (latitudes)
#[35.696, 52.271, 24.148, 24.969, 21.902, 23.219, 34.667, 34.839, 35.124, 25.08, 24.182, 33.167, 33.267, 32.885, 37.89]
print (longitudes)
#[139.57, 4.547, 120.665, 121.588, 120.852, 121.308, 135.431, 134.694, 135.764, 121.237, 120.616, 130.415, 131.369, 131.054, 126.739]

# ### gmplot is an API for offline google map
# refer this page for detail https://pypi.python.org/pypi/gmplot/1.0.5
# 

# In[29]:

import gmplot
gmap = gmplot.GoogleMapPlotter(23.5, 121, 5)
#gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
gmap.scatter(latitudes, longitudes, '#FF0000', size=10000, marker=False)
gmap.draw("mymap.html")


# In[19]:

import webbrowser
webbrowser.open(r'C:\Users\User\Desktop\mymap.html')


# In[ ]:

#Description (說明)
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

