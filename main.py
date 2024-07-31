import os
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

LOG_FILE = "process_log.txt"

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, file_to_watch):
        self.file_to_watch = file_to_watch

    def process(self, event):
        if event.event_type == 'modified' or event.event_type == 'created':
            if event.src_path.endswith(self.file_to_watch):
                self.log_processes_accessing_file()

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def log_processes_accessing_file(self):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"\n[{time.ctime()}] {self.file_to_watch} accessed by:\n")
            for proc in psutil.process_iter(['pid', 'name', 'open_files']):
                try:
                    if any(f.path == self.file_to_watch for f in proc.info['open_files'] or []):
                        log_file.write(f"PID: {proc.info['pid']}, Name: {proc.info['name']}\n")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

def monitor_file(file_to_watch):
    event_handler = FileEventHandler(file_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(file_to_watch), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    file_to_watch = "mali_tablolar.xlsx"
    if not os.path.isabs(file_to_watch):
        file_to_watch = os.path.join(os.getcwd(), file_to_watch)
    monitor_file(file_to_watch)
