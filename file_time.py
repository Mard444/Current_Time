import sys
import datetime

def file_time(filename):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, 'w') as file:
        file.write(current_time)

    print(f"Successfully created file with current time . {filename}:")

# Check for errors
if len(sys.argv) != 3:
    print("Err: python file_time.py <filename> <path>")
else:
    filename = sys.argv[1]
    path = sys.argv[2]
    file_time(filename)
