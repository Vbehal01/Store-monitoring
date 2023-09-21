import model
import csv
from constants import BQ_RESULTS_FILE_PATH, MENU_HOURS_FILE_PATH, STORE_STATUS_FILE_PATH
from datetime import datetime, timedelta


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

def string_to_time(time):
    if(len(time)>7):
        time=datetime.strftime("time", "%H:%M:%S")
    else:
        time="0"+time
        time = datetime.strptime(time.replace(".",":"), "%H:%M:%S")
    return (time.strftime("%H:%M:%S"))


def insert_menu_hours(db):
    with open (MENU_HOURS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            day=row["day"]
            start_time_local=string_to_time(row["start_time_local"])
            end_time_local=string_to_time(row["end_time_local"])
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

def time():
    current_time=datetime.now()
    one_hour_ago=current_time - timedelta(minutes=60)
    time_range={"current_time": current_time.strftime("%H:%M:%S"), "one_hour_ago": one_hour_ago.strftime("%H:%M:%S")}
    return time_range

def get_business_hour(db):
    return db.query(model.MenuHours).filter(and_(model.MenuHours.store_id==579100056021594000),(model.MenuHours.day==0)).all()

# data=time()
# print(data)