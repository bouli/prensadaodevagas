import os
from ohmyscrapper import config
import sqlite3
from datetime import datetime, timedelta
def main():
    today = datetime.today()
    limit_date = today - timedelta(days=8)

    limit_date = str(limit_date).split(".")[0]
    today = str(today).split(".")[0]

    limit_timestamp = str2timestamp(str_date=str(limit_date))
    reset_history()
    conn = get_connection()
    c = conn.cursor()

    sql = f"UPDATE urls SET history = 1 WHERE created_at <= {limit_timestamp} "
    c.execute(sql)
    conn.commit()
    conn.close()

    print(today)
    print(limit_date)

def reset_history():
    conn = get_connection()
    c = conn.cursor()

    sql = f"UPDATE urls SET history = 0 "
    c.execute(sql)
    conn.commit()
    conn.close()

def get_connection():
    db_file = os.path.join(config.get_dir("db"),config.get_db())
    conn = sqlite3.connect(db_file)
    return conn

def str2timestamp(str_date:str,str_format:str='%Y-%m-%d %H:%M:%S'):
    timestamp = str(datetime.strptime(str(str_date), str_format).timestamp()).split(".")[0]
    return timestamp

if __name__ == "__main__":
    main()
