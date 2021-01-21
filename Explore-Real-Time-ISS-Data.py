#!/usr/bin/env python
# coding: utf-8


from pytrends.request import TrendReq
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from IPython.display import Image

# Who is in the space currently?
import requests
r=requests.get(url='http://api.open-notify.org/astros.json')
r.json()

# http://www.satsig.net/lat_long.htm
Image(filename='satsig_explanation.gif', width='60%')


# Where is the space currently located?

r = requests.get(url='http://api.open-notify.org/iss-now.json')
space_station_location = (r.json())
print(space_station_location)


# Get specific value in json dictionary
float(space_station_location ['iss_position']['longitude'])


import os
os.environ['PROJ_LIB'] = r'C:\Users\HP\Anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'

# Let's plot the ISS current location
# You will need to pip install Basemap
from mpl_toolkits.basemap import Basemap

# Set the dimension of the figure
plt.figure(figsize=(16, 8))

# Make the background
m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")

import requests
r=requests.get(url='http://api.open-notify.org/astros.json')
r.json()
r = requests.get(url='http://api.open-notify.org/iss-now.json')
space_station_location = (r.json())

m.scatter(space_station_location['iss_position']['latitude'],
          space_station_location['iss_position']['longitude'],
          s=500, alpha=0.4,color='blue')
