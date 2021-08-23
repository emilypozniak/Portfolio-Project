import numpy as np
import pandas as pd



artists = pd.read_csv("/Users/emilypozniak/Desktop/artists.csv")


#First, I want to drop any duplicate rows in the data

artists = artists.drop_duplicates()


#Next, I want to drop any rows where it's the same artist and different spellings using the ambiguous_artist column

artists[artists['ambiguous_artist']== True]



#As you can see, there are some artists that are obviously the same, like Chris Brown and Christopher Brown.
#I'm assuming that if the number in the listeners_lastfm column are the same, then it is the same artist. 

artists = artists.drop_duplicates(
    subset = ['artist_lastfm', 'listeners_lastfm'],
    keep = 'first').reset_index(drop = True)


#This fixes the problem 

artists[artists['ambiguous_artist']== True]


#Now I am able to drop the ambiguous artist column and the artist_mb column
#I am also going to drop the country_mb column because they seem to be giving the same information

to_drop = ['artist_mb', 'ambiguous_artist', 'country_mb']
artists.drop(to_drop, inplace = True, axis = 1)



#Next, I want to reset the index to use the mbid column

artists['mbid'].is_unique


artists = artists.set_index('mbid')


#Next, I want to combine the tags columns into a singular column called Tags

artists['Tags'] = artists['tags_lastfm'] + artists['tags_mb']


#Now, I'll drop the tags_lastfm and tags_mb columns

to_drop = ['tags_lastfm', 'tags_mb']
artists.drop(to_drop, inplace = True, axis = 1)



#Finally, I want to rename the columns in the data frame

new_names =  {'mbid': 'ID', 'artist_lastfm': 'Artist', 
              'country_lastfm': 'Country', 'listeners_lastfm': 'Listeners', 
              'scrobbles_lastfm': 'Scrobbles'}



artists.rename(columns=new_names, inplace=True)



#The data frame is much easier to work with now.

artists.head()

