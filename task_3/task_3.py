import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)


def visualize_directory_structure(directory_path: Path, prefix: str = "", is_last: bool = True):
    """
    Recursively visualizes the directory structure with colored output.

    :param directory_path: Path object representing the directory to visualize
    :param prefix: String prefix for proper tree structure formatting
    :param is_last: Boolean indicating if this is the last item in the current level
    """
    try:
        # Get the connector symbol based on whether this is the last item
        connector = "└─" if is_last else "├─"

        # Print the current directory or file with the appropriate color
        if directory_path.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT} 📂 {directory_path.name}")
        else:
            print(f"{prefix}{connector}{Fore.GREEN} 📜 {directory_path.name}")

        # If it's a directory, recursively process its contents
        if directory_path.is_dir():
            # Get all items in the directory and sort them (directories first, then files)
            try:
                items = sorted(directory_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
            except PermissionError:
                print(f"{prefix}   {Fore.RED}[Permission Denied]")
                return

            # Calculate the new prefix for children
            extension = "   " if is_last else "│  "
            new_prefix = prefix + extension

            # Process each item in the directory
            for index, item in enumerate(items):
                is_last_item = (index == len(items) - 1)
                visualize_directory_structure(item, new_prefix, is_last_item)

    except Exception as e:
        print(f"{prefix}   {Fore.RED}[Error: {str(e)}]")


def main():
    """
    Main function that handles command-line arguments and initiates directory visualization.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: No directory path provided.")
        print(f"{Fore.YELLOW}Usage: python task_3.py <directory_path>")
        sys.exit(1)

    # Get the directory path from command-line arguments
    directory_path_str = sys.argv[1]
    directory_path = Path(directory_path_str)

    # Validate that the path exists
    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path_str}' does not exist.")
        sys.exit(1)

    # Validate that the path is a directory
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path_str}' is not a directory.")
        sys.exit(1)

    # Print the root directory name
    print(f"{Fore.CYAN}{Style.BRIGHT} 📦 {directory_path.name}")

    # Get all items in the root directory
    try:
        items = sorted(directory_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

        # Visualize each item
        for index, item in enumerate(items):
            is_last = (index == len(items) - 1)
            visualize_directory_structure(item, "", is_last)

    except PermissionError:
        print(f"{Fore.RED}Error: Permission denied to access '{directory_path_str}'.")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main() # omg this task gave me a head aich...