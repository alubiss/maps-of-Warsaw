#!/usr/bin/env python
# coding: utf-8

# In[2]:


import esda
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
import libpysal as lps
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point
import matplotlib.pyplot as plt
import osmnx as ox


# In[2]:


import folium


# In[4]:


city = ox.gdf_from_place('Warsaw, Poland')
ox.plot_shape(ox.project_gdf(city))


# In[5]:


G = ox.graph_from_place('Warsaw, Poland', network_type='drive')
ox.plot_graph(G)


# In[6]:


dane = pd.read_excel(io="dane.xlsx")


# In[9]:


dane["adres stacji"][142]


# In[10]:


C = ox.graph_from_address(dane["adres stacji"][143], network_type='drive')
ox.plot_graph(C)


# In[11]:


fig, ax = ox.plot_graph(C, show=False, close=False)
ax.scatter(52,21, c='red')
plt.show()


# In[22]:


G = ox.graph_from_address('Arkuszowa 22, Warsaw, Poland')
fig, ax = ox.plot_graph(G, show=False, close=False)
ax.scatter(20.9080351,52.2842445,c="#%02X0000" % 100)
plt.show()


# In[13]:


dane = pd.read_excel(io="dane2.xls")


# In[43]:


x = dane["wielkosc ruchu"][8]*5
x= int(x)
x


# In[53]:


#G = ox.graph_from_place('Warsaw, Poland')
fig, ax = ox.plot_graph(G, show=False, close=False)
#ax.scatter(20.9080351,52.2842445,c='red',zorder=2)
for m in range(len(dane["x"])):
    x = dane["wielkosc ruchu"][m]/100
    x= int(x)
    ax.scatter(dane["x"][m],dane["y"][m],s=dane["wielkosc ruchu"][m]/100 ,c="#%2X0000" % x ,zorder=2)
fig.set_size_inches(18.5, 10.5)
plt.show()


# In[ ]:




