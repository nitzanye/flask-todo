import csv
import os
import time


def log_csv(message):
    log_entry = {'Time': time.asctime(time.localtime(time.time())), 'Message': message}
    logs_path = os.path.join(os.path.dirname(__file__), '../logs/logs.csv')

    file_exists = os.path.isfile(logs_path)
    with open(logs_path, mode='a') as file:
        fieldnames = ['Time', 'Message']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow(log_entry)
