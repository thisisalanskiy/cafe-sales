# data_import.py
import pandas as pd

# Making sure we will be able to see all columns in the head printout
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)  # Prevent truncation of column values
pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping

class data_import:

  def __init__(self, file):
        """
        Initializes the data import class that loads data from a CSV file.
        :param file_path: str, path to the CSV file
        """
        self.file = file
        self.data_raw = None  # Placeholder for raw data
        self.delimiters = [',', ';', '\t', '|']  # Since we don't know what delimiters there might be

  def try_different_separators(self):
        """Try loading the file with different delimiters until one works."""
        for sep in self.delimiters:
            try:
                df = pd.read_csv(self.file, sep=sep, encoding='utf-8')
                if not df.empty: # Ensure it parsed correctly
                    print(f"Successfully loaded data using separator: '{sep}'")
                    return df 
            except Exception as e:
                print(f"Failed with separator '{sep}': {e}")
        print("Could not parse the file with the given separators.\nPlease check the source data file and start again.")
    
  def load_data(self):
    """Main function to load data with checks."""
    try:
        print("Attempting to load data...")  # Debugging step
        self.data_raw = self.try_different_separators()

        if self.data_raw is None:
            print("Error: No data loaded.")  # Debugging step
            return None  # Explicitly return None if no data
        
        print("Data loaded successfully! \nPreview:")
        print(self.data_raw.head())  # Show first rows
        return self.data_raw  # Return the DataFrame
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # Handle failures gracefully
    
# Example usage
# from data_import import data_import
# importer = data_import(raw_data)
# importer.load_data() <-- will check if the file exists, find the best delimeter for the file and load it into a Pandas DataFrame