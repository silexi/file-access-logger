
# FileAccessLogger

## Project Description

FileAccessLogger is a tool designed to monitor a specific file for modifications or creations and log the processes that access this file. It uses the `watchdog` library to observe the file system and the `psutil` library to track processes interacting with the file. All process activities related to the file are logged into a text file.

## Features
- Monitors a specified file for any modifications or creations.
- Logs the processes (including PID and process name) that access the monitored file.
- Continuously runs until interrupted, allowing real-time monitoring.
- Outputs logs to `process_log.txt` file.

## Technologies Used
- Python 3
- `watchdog` library (for file system event handling)
- `psutil` library (for process information retrieval)

## Installation Steps

1. **Install the required libraries:**
   - Install the necessary Python libraries by running:
     ```sh
     pip install watchdog psutil
     ```

2. **Running the Script:**
   - Start the file monitoring by running:
     ```sh
     python main.py
     ```

   - The `main.py` script will monitor the file `mali_tablolar.xlsx` by default. You can modify the script to monitor any other file.

3. **Customizing the Monitored File:**
   - To monitor a different file, change the `file_to_watch` variable in the `main.py` script:
     ```python
     file_to_watch = "your_file_name_here"
     ```
   - Replace `"your_file_name_here"` with the path to the file you want to monitor.

## Example Usage

1. **Monitor a File:**
   - By default, the script monitors `mali_tablolar.xlsx`. 
   - Any process that accesses or modifies this file will be logged in `process_log.txt`.

2. **Log Format:**
   - Each log entry includes the timestamp, the file accessed, and the details of the processes that accessed the file:
     ```
     [Thu Mar  4 10:20:42 2024] mali_tablolar.xlsx accessed by:
     PID: 12345, Name: python.exe
     ```

## Potential Enhancements
- Allow the user to specify the file to monitor via command-line arguments.
- Enhance logging to include more detailed process information.
- Implement a feature to alert the user when a specific process accesses the file.

## Support and Contact
If you have any questions or suggestions, feel free to contact the project maintainer at [kilicbartu@gmail.com](mailto:kilicbartu@gmail.com).
