# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PBUAnVmc7oY43IykXd6gP5atr12xUmwf
"""

# Import required libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
songs_data = pd.read_csv('/content/songs_data.csv')

# Convert genre to numerical format for clustering
songs_data['genre'] = songs_data['genre'].astype('category').cat.codes

# Select features for clustering
X = songs_data[['tempo', 'popularity', 'loudness', 'genre']]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize and fit KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
songs_data['cluster'] = kmeans.fit_predict(X_scaled)

# Visualize clusters using a pairplot
sns.pairplot(songs_data, hue='cluster', vars=['tempo', 'popularity', 'loudness'])
plt.show()

# Print centroids of each cluster
print("Cluster Centers (centroids):")
print(kmeans.cluster_centers_)

# Recommendation Function
def recommend_songs(song_id, n_recommendations=5):
    # Find the cluster of the given song_id
    song_cluster = songs_data.loc[songs_data['song_id'] == song_id, 'cluster'].values[0]

    # Recommend songs from the same cluster
    recommended_songs = songs_data[songs_data['cluster'] == song_cluster].sample(n_recommendations)

    print(f"Recommendations based on Song ID {song_id}:")
    print(recommended_songs[['song_id', 'tempo', 'popularity', 'loudness', 'genre']])

# Example: Get recommendations for song_id 10
recommend_songs(10)