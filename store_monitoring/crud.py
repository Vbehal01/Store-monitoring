import model
import csv
from constants import BQ_RESULTS_FILE_PATH, MENU_HOURS_FILE_PATH, STORE_STATUS_FILE_PATH


def insert_store_status(db):
    with open (STORE_STATUS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            status=row["status"]
            timestamp_utc=row["timestamp_utc"]
            data=model.StoreStatus(store_id=store_id, status=status, timestamp_utc=timestamp_utc)
            db.add(data)
            db.commit()
            db.refresh(data)
    return

def insert_menu_hours(db):
    with open (MENU_HOURS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            day=row["day"]
            start_time_local=row["start_time_local"]
            end_time_local=row["end_time_local"]
            data=model.MenuHours(store_id=store_id, day=day, start_time_local=start_time_local, end_time_local=end_time_local)
            db.add(data)
            db.commit()
            db.refresh(data)
    return

def insert_bq_results(db):
    with open (BQ_RESULTS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            timezone_str=row["timezone_str"]
            data=model.BqResults(store_id=store_id, timezone_str=timezone_str)
            db.add(data)
            db.commit()
            db.refresh(data)
    return
        