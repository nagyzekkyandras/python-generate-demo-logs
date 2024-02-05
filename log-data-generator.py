import os
import string
import random
import datetime

start_date = "2024-01-01"
end_date = "2024-02-01"
length = 250

def generate_random_timestamp(start_date, end_date):
    """
    Generate a random timestamp between start_date and end_date
    """
    # Convert start_date and end_date to datetime objects
    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    # Calculate the time difference in seconds
    time_diff = (end_datetime - start_datetime).total_seconds()

    # Generate a random timestamp within the time difference
    random_seconds = random.randint(0, int(time_diff))

    # Add the random time difference to the start_date
    random_datetime = start_datetime + datetime.timedelta(seconds=random_seconds)

    # Format the timestamp
    timestamp = random_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    return timestamp

def choose_log_level():
    """
    Randomly choose a log level
    """
    log_levels = ["ERROR", "WARNING", "INFO", "DEBUG", "TRACE"]
    return random.choice(log_levels)

def generate_random_string(length):
    """
    Generate a random string with a specific length using only letters and digits
    """
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def create_log_line(logfile):
    time = generate_random_timestamp(start_date, end_date)
    level = choose_log_level()
    message = generate_random_string(length)

    file1 = open(logfile, "a")
    logfilefile = str(time) + ' stdout F {"timestamp":"' + str(time) + '","level":"' + level + ',"message":"' + message + '"}\n'
    file1.writelines(logfilefile)
    file1.close()

def get_file_size(file_path):
    """
    Get the size of a file in bytes
    """
    try:
        # Get the size of the file
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print("File not found.")
        return -1

def check_and_create_file(file_path):
    """
    Check if a file exists, if not, create it
    """
    if not os.path.exists(file_path):
        try:
            # Create the file if it doesn't exist
            with open(file_path, 'a') as file:
                file.write("")  # You can write initial content if needed
            print(f"File '{file_path}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")
    else:
        print(f"File '{file_path}' already exists.")

def make_predefined_size_file(file_path, size_in_md):
    """
    Generates loglines using the functions before.
    """
    check_and_create_file(file_path)
    while True:
        file_size = get_file_size(file_path)
        if file_size < int(size_in_md) * 1024 * 1024:
            create_log_line(file_path)
        else:
            print("File size exceeds " + str(size_in_md) + "MB.")
            break

if __name__ == "__main__":
    make_predefined_size_file("app.log", 10)
