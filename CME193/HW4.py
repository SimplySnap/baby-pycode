import numpy as np
import pandas as pd
import time

#Import data
data = pd.read_csv("Spotify Most Streamed Songs.csv")
df = pd.DataFrame(data)

def questionOne(df):
    print(df.head())
    time.sleep(4)
    print(df.tail())
    time.sleep(2)
    print(df.shape)
    time.sleep(2)
    print(df.dtypes)
    time.sleep(1)
    print(df.columns.tolist)
    time.sleep(1)
    print(f"Empty values in each column \n: {df.isnull().sum()}")

#questionOne(df)

def questionTwo(df):
    #songs_2023 new data frame of songs released in 2023
    songs_2023 = df.loc[df['released_year'] == 2023]
    print(f"Songs released in 2023:\n{songs_2023}")

    #Sort dataset in stream column in descending order
    songs_2023.sort_values(by='streams', ascending=False)

    sorted_songs_2023 = songs_2023.loc[(df['danceability_%'] > 70) & (df['energy_%'] > 80)]
    print(sorted_songs_2023)
#questionTwo(df)

def questionThree(df):
    newset = df.groupby('artist(s)_name')['streams'].sum() #Groups dataset by artist and calcs total # of streams
    print(newset)

    artist_track_counts = df.groupby('artist(s)_name').size()  # Counts the number of tracks for each artist
    # Find the artist with the maximum number of tracks
    most_tracks_artist = artist_track_counts.idxmax()
    print(most_tracks_artist)

    analytics = df.groupby('released_year').agg({
        'danceability_%': 'mean',
        'valence_%': 'mean',
        'energy_%': 'mean'
    })
    print(analytics)
#questionThree(df)

def questionFour(df):
    df['total_playlists'] = df['in_spotify_playlists'] + df['in_apple_playlists']

    #Normalize the streams column
    df['normalized_streams'] = (df['streams'] - df['streams'].min()) / (df['streams'].max() - df['streams'].min())

    # 3. Convert released year, month, and day into a single release date column
    df['release_date'] = df['released_year'].astype(str) + '-' + df['released_month'].astype(str) + '-' + df['released_day'].astype(str)

    print(df[['total_playlists', 'normalized_streams', 'release_date']].head())
#questionFour(df)

def questionFive(df):
    danceabilityStats = {
        'mean': df['danceability_%'].mean(),
        'median': df['danceability_%'].median(),
        'std': df['danceability_%'].std()
    }

    streamsStats = {
        'mean': df['streams'].mean(),
        'median': df['streams'].median(),
        'std': df['streams'].std()
    }

    energyStats = {
        'mean': df['energy_%'].mean(),
        'median': df['energy_%'].median(),
        'std': df['energy_%'].std()
    }
    print(f"Mean, median and standard deviation for streams, danceability and energy are: {danceabilityStats,streamsStats,energyStats}")

    highest_valence_song = df.loc[df['valence_percent'].idxmax()]
    lowest_valence_song = df.loc[df['valence_percent'].idxmin()]

    print(f"The song with highest and lowest valence respectively are: {highest_valence_song, lowest_valence_song}")
#questionFive(df)

def questionSix(df):
    sel_cols = df[['track_name', 'artist(s)_name', 'streams']]

    print(f"First 10 rows using .loc:\n{sel_cols.loc[:9]}")
    print(f"First 10 rows using .iloc:\n{sel_cols.iloc[:10]}")
questionSix(df)
