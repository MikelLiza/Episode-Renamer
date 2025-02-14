import os
import requests
import re

def sanitize_filename(title):
    """
    Sanitizes the filename by removing or replacing illegal characters.
    """
    illegal_chars = r'[\\/:*?"<>|]'
    sanitized_title = re.sub(illegal_chars, '-', title)
    return sanitized_title

def get_show_id(show_name, year=None):
    """
    Searches for a TV show by name and optionally filters by year.
    Returns the show ID of the first matching result.
    """
    url = f"http://api.tvmaze.com/search/shows?q={show_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        results = response.json()
        for result in results:
            show = result['show']
            # Check if the year matches (if provided)
            if year and show['premiered']:
                show_year = show['premiered'].split('-')[0]
                if show_year == str(year):
                    return show['id']
            # If no year is provided, return the first result
            elif not year:
                return show['id']
        print(f"No matching show found for '{show_name}' (year: {year})")
        return None
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

def get_episode_titles(show_id):
    """
    Fetches episode titles for a TV show using its ID.
    Returns a dictionary where the key is (season, episode) and the value is the episode title.
    """
    url = f"http://api.tvmaze.com/shows/{show_id}/episodes"
    response = requests.get(url)
    
    if response.status_code == 200:
        episodes = response.json()
        
        # Create a dictionary of episode titles
        episode_dict = {}
        for episode in episodes:
            season = episode['season']
            episode_num = episode['number']
            title = episode['name']
            episode_dict[(season, episode_num)] = title
        
        return episode_dict
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

def rename_files_in_season_folder(season_folder, season_number, episode_dict):
    """
    Renames files in a season folder to the format "n-x title of the episode".
    """
    files = os.listdir(season_folder)
    
    # Sort files alphabetically (assuming they are in the correct order)
    files.sort()
    
    for index, filename in enumerate(files, start=1):
        # Find the corresponding episode title
        if (season_number, index) in episode_dict:
            title = episode_dict[(season_number, index)]
            # Sanitize the title to remove illegal characters
            sanitized_title = sanitize_filename(title)
            # Create the new filename
            new_filename = f"{season_number}-{index} {sanitized_title}{os.path.splitext(filename)[1]}"
            new_filepath = os.path.join(season_folder, new_filename)
            
            # Rename the file
            old_filepath = os.path.join(season_folder, filename)
            try:
                os.rename(old_filepath, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")
        else:
            print(f"No title found for Season {season_number}, Episode {index}")

def process_season_folders(base_folder, episode_dict):
    """
    Processes each season folder in the base folder.
    """
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        
        # Check if it's a directory and matches the "Season X" format
        if os.path.isdir(folder_path) and folder_name.lower().startswith("season"):
            try:
                # Extract the season number from the folder name
                season_number = int(folder_name.split()[1])
                print(f"Processing {folder_name}...")
                
                # Rename files in the season folder
                rename_files_in_season_folder(folder_path, season_number, episode_dict)
            except (IndexError, ValueError):
                print(f"Skipping folder '{folder_name}' (invalid format)")

# Example usage
show_name = "Avatar: The Last Airbender"  # Replace with your TV show name
#show_year = "2005"  # Replace with the year the show premiered
base_folder = "d:\Shows\Avatar the Last Airbender"  # Replace with your base folder containing season folders

# Get the correct show ID
show_id = get_show_id(show_name, show_year)

if show_id:
    # Fetch episode titles
    episode_dict = get_episode_titles(show_id)
    
    if episode_dict:
        # Process each season folder
        process_season_folders(base_folder, episode_dict)