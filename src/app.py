import streamlit as st
from modules import data_handling, recommendation, ui_design

def main():
    st.title("Movie Recommendation App")

    # Load movie data
    movie_data = data_handling.load_data("src/data/movies.csv")

    if movie_data is not None:
        # Sidebar for user input
        user_input = ui_design.get_user_input(movie_data)

        if user_input:
            # Generate movie recommendations
            recommended_movies = recommendation.get_recommendations(user_input, movie_data)

            # Display recommendations
            ui_design.display_recommendations(recommended_movies)

if __name__ == "__main__":
    main()