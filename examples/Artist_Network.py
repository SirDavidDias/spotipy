#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:57:55 2018

@author: daviddias
"""

#Load libraries for handle the Spotify API data (Spotipy)

import pandas as pd

#########################################################################################################
#Libraries for Spotify API (Spotipy)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials()

#To get access to all Spotipy functions
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#########################################################################################################


def related_groups_photo(name):
    results = sp.search(q='artist:' + name, type='artist')
    resultsrelated = sp.artist_related_artists(results['artists']['items'][0]['id'])
    tablaresultsrelated = pd.DataFrame(columns=['Artist', 'Artist_related', 'Artist_photo', 'Artist_related_photo'], index=None)
    #List of artists based on seed artist
    for i in range(0,len(resultsrelated['artists'])):
            tabla1 = pd.DataFrame(data={'Artist': results['artists']['items'][0]['name'],
                                      'Artist_related': resultsrelated['artists'][i]['name'],
                                        'Artist_photo': results['artists']['items'][0]['images'][1]['url'],
                                        'Artist_related_photo': resultsrelated['artists'][i]['images'][0]['url']}, index=[i])
            tablaresultsrelated = tablaresultsrelated.append(tabla1, ignore_index=True)
            
    #This loop repeat the step above for each artist
    for i in range(0,len(resultsrelated['artists'])):
     resultsrelated1 = sp.artist_related_artists(resultsrelated['artists'][i]['id'])
     for e in range(0, len(resultsrelated1['artists'])):
                 tabla2 = pd.DataFrame(data={'Artist': resultsrelated['artists'][i]['name'],
                                      'Artist_related': resultsrelated1['artists'][e]['name'],
                                        'Artist_photo': resultsrelated['artists'][i]['images'][0]['url'],
                                        'Artist_related_photo': resultsrelated1['artists'][e]['images'][0]['url']}, index=[i])
                 tablaresultsrelated = tablaresultsrelated.append(tabla2, ignore_index=True)
                 
                 tablaresultsrelated.to_csv('/path.csv', sep=',', index=None,header=True)
        
    return tablaresultsrelated


#This allow you to get a network based on an artist you like.