import os
from ohmyscrapper import config
import sqlite3

from datetime import datetime
from urlextract import URLExtract
def main():
    input_dir_name = "ohmyscrapper_input"
    input_files = os.listdir(input_dir_name)
    extractor = URLExtract()
    conn = get_connection()
    for input_file_name in input_files:
        input_file_path = os.path.join(input_dir_name,input_file_name)
        with open(input_file_path, "r") as input_file:
            input_file_content = input_file.read()
        messages = input_file_content.split("[__message__]")
        for message in messages:
            for url in extractor.find_urls(message):
                timestamp = int(datetime.strptime(str(message[:22]), '[%d/%m/%Y, %H:%M:%S]').timestamp())

                c = conn.cursor()
                c.execute("UPDATE urls SET created_at = ? WHERE url = ?", (timestamp, url))

                print(timestamp, url)


def get_connection():
    db_file = os.path.join(config.get_dir("db"),config.get_db())
    conn = sqlite3.connect(db_file)
    return conn

if __name__ == "__main__":
    main()
    timestamp = 1769973109
    date_time = datetime.fromtimestamp(timestamp)
    timestamp = datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S').timestamp()
