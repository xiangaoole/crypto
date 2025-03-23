import zipfile
import getpass
from io import TextIOWrapper

def clean_path(path: str) -> str:
    """Clean path string by removing quotes and extra spaces"""
    # Remove leading/trailing spaces first
    return path.strip().strip("'").strip('"')

def read_encrypted_zip(zip_path: str, password: str = None) -> None:
    """Read and print contents of password-protected ZIP without extracting"""
    # Clean the path before using
    zip_path = clean_path(zip_path)
    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            # List all files in the ZIP
            for file_info in zip_file.filelist:
                print(f"\nReading file: {file_info.filename}")
                
                # Open file in ZIP with password
                with zip_file.open(file_info.filename, pwd=password.encode() if password else None) as file:
                    # Wrap binary file with TextIOWrapper for text files
                    text_file = TextIOWrapper(file, encoding='utf-8')
                    print("Contents:")
                    print("-" * 50)
                    print(text_file.read())
                    print("-" * 50)

    except zipfile.BadZipFile:
        print("Error: Invalid ZIP file")
    except RuntimeError as e:
        if "Bad password" in str(e):
            print("Error: Incorrect password")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    zip_path = input("Enter ZIP file path: ")
    password = getpass.getpass("Enter ZIP password (press Enter if none): ")
    
    if not password.strip():
        password = None
        
    read_encrypted_zip(zip_path, password)

if __name__ == "__main__":
    main()