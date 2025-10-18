from pathlib import Path


def total_salary(path: str | Path) -> tuple[int, int]:
    """
    Calculates the total sum of salaries and the average salary from a given file.

    :param path: The path to the file containing salary data.
    :return: A tuple containing the total salary sum and the average salary.
    :raises FileNotFoundError: If the specified file does not exist.
    :raises PermissionError: If there is no permission to read the specified file.
    :raises OSError: If an error occurs while attempting to read the file.
    :raises ValueError: If the file is empty or contains invalid data.
    """
    pathname = Path(path)  # Convert path to the Path object in case it's a string
    try:
        with open(pathname, "r") as file:
            data = file.read().strip()  # Read and remove whitespace

            if not data:
                raise ValueError(f"File '{pathname}' is empty.")

            try:
                salaries = [int(salary.split(",")[1]) for salary in data.splitlines()]  # Extract salary values
                return sum(salaries), int(sum(salaries) / len(salaries))  # Return total and average
            except (ValueError, IndexError):
                raise ValueError(f"File '{pathname}' has invalid data format.")

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{pathname}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{pathname}'.")
    except OSError:
        raise OSError(f"Error occurred while reading file '{pathname}'.")


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
