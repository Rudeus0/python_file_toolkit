import argparse
import logging
from .file_manager import catch_file_type, read_txt_file, read_csv_file





def main():
             # We use .strip() here just in case, though argparse usually handles this
           
    while attempt < 3:  # Retry up to 3 times for file-related errors
        attempt = 1
        parser = argparse.ArgumentParser(description='Python file Toolkit')
        parser.add_argument("file", help="File Name")   
        args = parser.parse_args()             # Get the path from argparse instead of input() 
        file_path = args.file.strip()    
        file_type = catch_file_type(file_path)
        
        if file_type is None:
            attempt += 1
            print("filetype nor found")
            continue   
        try:
            if file_type == "txt_file":
                content = read_txt_file(file_path)
                print(content)
                break  # if file type is .txt and excuted to prevent infinte loop or extra loop break used 
        
            elif file_type == "csv_file":
                data = read_csv_file(file_path)
                if not data:
                    print("The file is empty")
                else:
                    print("\nCSV SUMMARY")
                    print("-----------")
                    print(f"Rows: {len(data)}")
                    print(f"Columns: {len(data[0])}")
                    print("\nColumn Names:")
                    for col in data[0].keys():
                        print(col)
                    break  # if file type is .csv and excuted to prevent infinte loop or extra loop break used
        except (PermissionError, FileNotFoundError, FileExistsError) as e:
            attempt += 1   
            print(f"The opend file 'Error {e}'")
            
    if attempt == 3:    # when count reaches 3 the excution restart.
            print("Your three attempt as been used try again")
            
    
    
if __name__ == "__main__":
    main()