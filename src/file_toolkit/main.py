from .file_manager import catch_file_type, read_txt_file, read_csv_file

def main():
    
    file_path = input("Enter the file name: ").strip()
    
    file_type = catch_file_type(file_path)
    
    if file_type == "txt_file":
        read_txt_file(file_path)
    
    elif file_type == "csv_file":
        read_csv_file(file_path)
    
    else:
        print("Unknown file type. Supported file_type: .txt, .csv") 
    
    
    
if __name__ == "__main__":
    main()