#!/usr/bin/env python
# coding: utf-8

# In[1]:


from geopy.geocoders import Nominatim
import numpy as np
import rasterio
from PIL import Image
import matplotlib.pyplot as plt
import math


# In[2]:


#function to fetch lat and long given city name
def get_location(city):
    arr = {}
    geolocator = Nominatim(user_agent="megh_varta")
    location = geolocator.geocode(city)
    arr['city'], arr['lat'], arr['lon'] = location.raw['display_name'], np.float(location.raw['lat']), np.float(location.raw['lon'])
    return arr

#convert longitude and latitude to corresponding pixels
def cords_to_pixel(lon, lat):
    xs = (height/29.2) * (lon-62.8)
    ys = width-((width/33) * (lat-4.5))
    return (xs, ys)

# def cords_to_pixel(lon, lat):
#     xs, ys= rasterio.transform.rowcol(src.transform,  location['lon'],location['lat'],)
#     return ( ys,xs)
south=math.radians(8.4)
north=math.radians(37.6)
west= math.radians(68.7)
east= math.radians(97.25)

width = 887
height = 971

def mercY(lat):
    return math.log(math.tan(lat/2 + math.pi/4)) 

ymin = mercY(south);
ymax = mercY(north);
xFactor = width/(east - west);
yFactor = height/(ymax - ymin);

print(ymin)
print(ymax)
print(xFactor)
print(yFactor)

def mapProject(lat, lon):# both in radians, use deg2rad if neccessary
    global xFactor, yFactor, west, ymax;
    x = lon;
    y = mercY(lat);
    x = (x - west)*xFactor;
    y = (ymax - y)*yFactor; # y points south
    return (x+10, y-13);


# In[3]:


# geolocator = Nominatim(user_agent="megh_varta1")
# location = geolocator.geocode("Mumbai")
# print(location.address)


# In[41]:


# img = Image.open("india1.png")
# ar = np.array(img)

img2 = Image.open("india1cc.png")
ar1 = np.array(img2)

#city -> location
city_name="nagpur"
location = get_location(city_name)
# print(location)
#lon, lat -> pixels
pixel_cord = mapProject(math.radians(location['lat']), math.radians(location['lon']))
# mask = ar[int(pixel_cord[0]), int(pixel_cord[1])]

# mask_str = ""

# if mask == 0:
#     mask_str = "Clear"
# else:
#     mask_str = "Cloudy"

#display
fig2 = plt.figure(figsize = (20,20))

ax3 = fig2.add_subplot(111)
ax3.axis('off')
# x_label = "8 July 00:00 "", City: "+ location['city'].split(",")[0] + ",  Latt: " +str(round(location['lat'],3)) + ",  Long: " + str(round(location['lon'],3))
# ax3.set_xlabel(x_label, fontsize=40, style="italic")

# Turn off tick labels
ax3.set_yticklabels([])
ax3.set_xticklabels([])
ax3.imshow(ar1[:,:])
# ax3.imshow(ar, cmap='gray',alpha=0.5)
ax3.annotate(" ", xy=pixel_cord, xycoords='data',
             backgroundcolor='black',fontsize=1)
# ax3.set_title(" " + mask_str,fontsize=35, fontweight="bold")
ax3.set_title(" ",fontsize=35, fontweight="bold")
plt.savefig("cords.jpg",bbox_inches='tight')
plt.show()


# In[ ]:




