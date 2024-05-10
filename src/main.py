import streamlit as st
import pickle
import requests
import zstandard as zstd

# Load Data and Decompress
def decompress_with_zstd(file_path):
    with open(file_path, 'rb') as f:
        compressed_data = f.read()
    # Decompress using Zstandard
    dc = zstd.ZstdDecompressor()
    decompressed_data = dc.decompress(compressed_data)
    # Load the model from the decompressed data
    loaded_model = pickle.loads(decompressed_data)
    return loaded_model

# Load movie data and similarity scores
movies_df = decompress_with_zstd('data/pkl_data/movies_df.zstd')
similarity = decompress_with_zstd('data/pkl_data/similarity.zstd')

# Your API key
API_KEY = "#YOUR_API_KEY"


# Fetch movie poster from TMDb API
def fetch_poster(movie_id):
    try:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US")
        data = response.json()
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/original" + data['poster_path']
        else:
            return None  # No poster available
    except:
        return None  # Error occurred

# Fetch IMDB ID from TMDb API
def fetch_imdb_id(movie_id):
    try:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids?api_key={API_KEY}")
        data = response.json()
        if data.get('imdb_id'):
            return data['imdb_id']
        else:
            return None  # No IMDB ID available
    except:
        return None  # Error occurred