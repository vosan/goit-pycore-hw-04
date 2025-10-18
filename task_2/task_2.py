from pathlib import Path

def get_cats_info(path: str | Path) -> list[dict[str, str]]:
    """
    Reads cat information from a file and returns a list of dictionaries with cats' information.

    :param path: The path to the file containing cats data.
    :return: A list of dictionaries with cats' information (id, name, age).
    :raises FileNotFoundError: If the specified file does not exist.
    :raises PermissionError: If there is no permission to read the specified file.
    :raises OSError: If an error occurs while attempting to read the file.
    :raises ValueError: If the file is empty or contains invalid data.
    """
    pathname = Path(path)  # Convert path to the Path object in case it's a string
    
    try:
        with open(pathname, 'r') as file:
            data = file.read().strip()  # Read and remove whitespace
            
            if not data:
                raise ValueError(f"File '{pathname}' is empty.")
            
            cats_info = []
            for line_number, line in enumerate(data.splitlines(), start=1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_info.append(
                        {'id': cat_id.strip(), 'name': name.strip(), 'age': age.strip()}
                    )
                except ValueError:
                    raise ValueError(
                        f"Invalid data format at line {line_number} in file '{pathname}'. "
                        f"Expected format: 'id,name,age'"
                    )
            
            return cats_info
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{pathname}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{pathname}'.")
    except OSError:
        raise OSError(f"Error occurred while reading file '{pathname}'.")

print(get_cats_info('cats_db.txt'))