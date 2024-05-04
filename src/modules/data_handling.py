import pandas as pd

def load_data(file_path):
    """
    Load movie data from CSV file.

    Args:
        file_path (str): Path to the CSV file containing movie data.

    Returns:
        pd.DataFrame: DataFrame containing movie data.
    """
    movie_data = pd.read_csv(file_path)
    return movie_data