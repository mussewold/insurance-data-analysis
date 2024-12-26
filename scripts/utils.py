import pandas as pd
import os



def load_data(file_path):

    input_file = file_path  
    output_file = "../data/MachineLearningRating_v3.csv"  
     # Ensure the directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = pd.read_csv(input_file, delimiter='|') # Delimeter


    data.to_csv(output_file, index=False)

    print(f"File successfully converted and saved as {output_file}")
    return data

