import pandas as pd

def load_data(file_path):
    """
    Load movie data from CSV file.

    Args:
        file_path (str): Path to the CSV file containing movie data.

    Returns:
        pd.DataFrame: DataFrame containing movie data.
    """
    try:
        movie_data = pd.read_csv(file_path, low_memory=False)
        return movie_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading data: {str(e)}")
        return None