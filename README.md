# Movie Recommender Web App

This is a web application built with Streamlit that recommends similar movies based on user input. It employs a movie recommendation system trained on movie data and similarity scores.

## Overview

The application allows users to select a movie from a dropdown menu and click the "Recommend" button to receive a list of similar movies. Each recommendation includes the movie's title, poster image, and a link to its IMDb page.

## Features

- **Movie Selection**: Users can choose a movie from a dropdown menu populated with a list of available movies.
- **Recommendation**: Upon selecting a movie and clicking the "Recommend" button, the system retrieves and displays a list of similar movies.
- **Poster Display**: The recommended movies are presented alongside their poster images obtained from [The Movie Database (TMDb)](https://www.themoviedb.org/).
- **IMDb Link**: Each recommended movie includes a link to its corresponding IMDb page for further information.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Streamlit
- Requests
- zstandard

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## API Key

To fetch movie data and posters, the application requires an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/). Follow these steps to obtain your API key:

1. Sign up or log in to your TMDb account.
2. Navigate to your account settings and select the "API" option from the dropdown menu.
3. Create a new API application and follow the instructions to generate your API key.
4. Once you have your API key, open the `app.py` file in the project directory.
5. Locate the `API_KEY` variable at the top of the file and replace `"YOUR_API_KEY"` with your actual API key.

```python
API_KEY = "YOUR_API_KEY"
```

By following these steps, you'll be able to use the application with your own API key.

## File Structure

- `app.py`: Main Python script containing the Streamlit web application.
- `src/`: Directory containing additional resources used by the application.
  - `data/pkl_data/`: Directory containing compressed pickle files of movie data and similarity scores.
  - `data/image/no-poster.png`: Default image displayed when no poster is available for a movie.

## Usage

1. Clone the repository or download the source code files.
2. Navigate to the project directory in your terminal.
3. Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

4. Once the app is running, open your web browser and navigate to the provided URL.
5. Select a movie from the dropdown menu and click the "Recommend" button to view similar movies.

## Acknowledgments

- This project utilizes data from [The Movie Database (TMDb)](https://www.themoviedb.org/) and [IMDb](https://www.imdb.com/).
- The movie recommendation system is based on collaborative filtering techniques.
- Streamlit library is used for building interactive web applications with Python.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
