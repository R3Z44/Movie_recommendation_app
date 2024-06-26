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
movies_df = decompress_with_zstd('src/data/pkl_data/movies_df.zstd')
similarity = decompress_with_zstd('src/data/pkl_data/similarity.zstd')

# Your API key
API_KEY = "YOUR_API_KEY"


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
    
# Recommend similar movies
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]
    
    recommended_movies = []
    recommended_movies_poster = []
    for movie in movies_list:
        id = movies_df.iloc[movie[0]].movie_id
        recommended_movies.append(movies_df.iloc[movie[0]].title)
        # Fetch poster from API
        poster_url = fetch_poster(id)
        if poster_url:
            imdb_id = fetch_imdb_id(id)
            recommended_movies_poster.append({'poster_url': poster_url, 'imdb_id': imdb_id})
        else:
            recommended_movies_poster.append({'poster_url': "src/data/image/no-poster.png", 'imdb_id': None})  # Default image
    return recommended_movies, recommended_movies_poster

# Web App
def main():
    # Streamlit Config
    st.set_page_config(page_title="Movie Recommender", page_icon=":movie_camera:", layout="wide")
    
    # Web Components
    st.title('Movie Recommendation System')
    selected_movie = st.selectbox(
        label="Select a movie",
        options=movies_df['title'],
        placeholder="Choose a movie",
        index=None)

    if st.button('Recommend'): 
        # No movies selected 
        if selected_movie == None:
            st.error("No movie selected.")
            return
        
        try:    
            names, posters = recommend(selected_movie)
            num_cols = 5
            num_movies = len(names)
            num_rows = num_movies // num_cols + (num_movies % num_cols > 0)

            for i in range(num_rows):
                cols = st.columns(num_cols)
                for j in range(num_cols):
                    index = i * num_cols + j
                    if index < num_movies:
                        with cols[j]:
                            st.text(names[index])
                            st.image(posters[index]['poster_url'])
                            st.markdown(f"[IMDb](https://www.imdb.com/title/{posters[index]['imdb_id']}/)")
        except IndexError:
            st.error("Currently we don't have any information about this movie.")

if __name__ == "__main__": 
    main()
