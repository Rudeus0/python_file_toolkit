from .file_manager import catch_file_type, read_txt_file, read_csv_file

def main():
    attempt = 0
    while attempt < 3:  # Retry up to 3 times for file-related errors
    
        file_path = input("Enter the file name: ").strip()   #.strip() is used to "prevent" extra space after file name enter
        file_type = catch_file_type(file_path)
        
        if file_type is None:
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
                    print(data[0].keys())
                    print(data[:5])
                    break  # if file type is .csv and excuted to prevent infinte loop or extra loop break used
        except (PermissionError, FileNotFoundError, FileExistsError) as e:
            attempt += 1   
            print(f"The opend file 'Error {e}'")
            
    if attempt == 3:    # when count reaches 3 the excution restart.
            print("Your three attempt as been used try again")
            
    
    
if __name__ == "__main__":
    main()