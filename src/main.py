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