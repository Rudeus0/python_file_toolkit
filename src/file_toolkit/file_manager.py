import csv
#identify the file type in string 
def catch_file_type(file_path: str) -> str | None:
    file_path =file_path.lower()
    
    if file_path.endswith('.txt'):
        return "txt_file"
    elif file_path.endswith(".csv"):
        return "csv_file"
    else:
        return None
    
#
def read_txt_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)  
    except (FileNotFoundError, PermissionError) as e:
        print(f'Error reading file {e}')
    
    
        
def read_csv_file(file_path: str):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                print(row)
    except (FileNotFoundError, PermissionError)  as e:
        print(f'Error reading file{e}')
    