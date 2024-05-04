from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(movie_data):
    """
    Calculate similarity between movies based on genres.

    Args:
        movie_data (pd.DataFrame): DataFrame containing movie data.

    Returns:
        np.array: Array of cosine similarity scores between movies.
    """
    # Extract genre information from movie_data and encode it
    genres = movie_data["genre"].str.get_dummies(sep=',')
    
    # Calculate cosine similarity between movies based on genres
    similarity_matrix = cosine_similarity(genres, genres)
    
    return similarity_matrix

def get_recommendations(user_preferences, movie_data, similarity_matrix, num_recommendations=5):
    """
    Generate movie recommendations based on user preferences.

    Args:
        user_preferences (dict): User preferences containing favorite genres.
        movie_data (pd.DataFrame): DataFrame containing movie data.
        similarity_matrix (np.array): Array of cosine similarity scores between movies.
        num_recommendations (int): Number of recommendations to generate.

    Returns:
        list: List of recommended movies.
    """
    # Extract genre information from movie_data and encode it
    genres = movie_data["genre"].str.get_dummies(sep=',')
    
    # Create a preference vector based on user preferences
    preference_vector = np.zeros(len(genres.columns))
    for genre in user_preferences:
        if genre in genres.columns:
            preference_vector += user_preferences[genre] * genres[genre]
    
    # Calculate similarity between user preferences and movies
    similarity_scores = cosine_similarity([preference_vector], genres)[0]
    
    # Get indices of movies with highest similarity scores
    movie_indices = np.argsort(similarity_scores)[::-1][:num_recommendations]
    
    # Get recommended movies based on indices
    recommended_movies = movie_data.iloc[movie_indices]
    
    return recommended_movies