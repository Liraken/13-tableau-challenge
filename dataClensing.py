import pandas as pd

# List of filenames
filenames = ['202307-citibike-tripdata', '202312-citibike-tripdata']

# Directory where the files are located
directory = 'Resources/'

# Loop through each file
for filename in filenames:
    # Construct the full path to the file
    file_path = f'{directory}{filename}.csv'
    
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Count the occurrences of each 'start_station_id'
    station_counts = df['start_station_id'].value_counts()

    filtered_df = df[df['start_station_id'].map(station_counts) >= 50]

    # Drop rows with any empty cells
    filtered_df = df.dropna()
    
    # Drop the specified columns
    columns_to_drop = ['rideable_type', 'end_station_name', 'end_station_id', 'end_lat', 'end_lng']
    filtered_df = filtered_df.drop(columns=columns_to_drop)


    # Construct the path for the cleaned file (could also overwrite the original file if desired)
    cleaned_file_path = f'{directory}{filename}.csv'

    # Save the cleaned dataframe to a new CSV file
    filtered_df.to_csv(cleaned_file_path, index=False)
    
    print(f'Rows with empty cells have been dropped and the cleaned data for {filename} is saved.')