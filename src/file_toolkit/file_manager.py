import csv
import logging


logging.basicConfig(filename='logs/toolkit.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#identify the file type in string 
def catch_file_type(file_path: str) -> str | None:
    file_path =file_path.lower()
    
    if file_path.endswith('.txt'):
        return "txt_file"
    elif file_path.endswith(".csv"):
        return "csv_file"
    else:
        return None
    
#Reads the .txt file and return value as string 
def read_txt_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            txt_data = file.read()
            logging.info(f"Text file opened successfully:{file_path}")
            return txt_data  
    except Exception as e:
        logging.error(f"Error reading text file:{file_path}: {e}")
        raise 
        
    
#Reads the .csv file and return value as list 
def read_csv_file(file_path: str):
   try:
        with open(file_path, 'r') as csv_file:
            csv_data = []
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                csv_data.append(row)
                
        logging.info(f"CSV file loaded successfully:{file_path}")     
        return csv_data
   except Exception as e:
            logging.error(f"Error reading CSV file:{file_path}: {e}")
            raise 
    

            
   
    