
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
print (longitudes)


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



