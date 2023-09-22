import model
import csv
from constants import STORE_TIMEZONE_FILE_PATH, STORE_BUSINESS_HOURS_FILE_PATH, STORE_STATUS_FILE_PATH
from sqlalchemy import and_
from utils.time import business_hour_string_to_time, last_hour_time_interval, string_to_time
from utils.math import get_intersection_of_intervals

def insert_store_status_update(db):
    with open (STORE_STATUS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            status=row["status"]
            timestamp_utc=row["timestamp_utc"]
            data=model.StoreStatusUpdates(store_id=store_id, status=status, timestamp_utc=timestamp_utc)
            db.add(data)
            db.commit()
            db.refresh(data)
            unique_store_id_business_hours=db.query(model.StoreBusinessHours).filter(model.StoreBusinessHours.store_id==store_id).first()
            if unique_store_id_business_hours is None:
                for day in range(0,7):
                    business_hour_data=model.StoreBusinessHours(store_id=store_id, day=day, start_time_local=string_to_time("00:00:00"), end_time_local=string_to_time("23:59:59"))
                    db.add(business_hour_data)
                    db.commit()
                    db.refresh(business_hour_data)
            unique_store_id_store_timezone=db.query(model.StoreTimezone).filter(model.StoreTimezone.store_id==store_id).first()
            if unique_store_id_store_timezone is None:
                data=model.StoreTimezone(store_id=store_id, timezone_str="America/Chicago")
                db.add(data)
                db.commit()
                db.refresh(data)   
    return

def find_storeid_timezone(db, store_id):
    data=db.query(model.StoreTimezone).filter(model.StoreTimezone.store_id==store_id).first()
    return data.timezone_str

def insert_store_business_hour(db):
    with open (STORE_BUSINESS_HOURS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            day=row["day"]
            timezone={"Asia/Beirut": "+3", "America/Boise": "-7", "America/Denver": "-7", "America/Chicago": "-6", "America/New_York": "-5", "America/Los_Angeles": "-8"}
            zone=find_storeid_timezone(db, store_id)
            start_time_local=business_hour_string_to_time(row["start_time_local"],timezone[zone])
            end_time_local=business_hour_string_to_time(row["end_time_local"],timezone[zone])
            data=model.StoreBusinessHours(store_id=store_id, day=day, start_time_local=start_time_local, end_time_local=end_time_local)
            db.add(data)
            db.commit()
            db.refresh(data)
    return

def insert_store_time_zone(db):
    with open (STORE_TIMEZONE_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        unique_store_id={}
        for row in file_content:
            store_id=row["store_id"]
            timezone_str=row["timezone_str"]
            unique_store_id[f"{store_id}"]=1
            data=model.StoreTimezone(store_id=store_id, timezone_str=timezone_str)
            db.add(data)
            db.commit()
            db.refresh(data)
    return

def get_business_hour(db):
    data= db.query(model.StoreBusinessHours).filter(and_(model.StoreBusinessHours.store_id==579100056021594000),(model.StoreBusinessHours.day==0)).all()
    return data

def query(db):
    business_hour=get_business_hour(db)
    time=last_hour_time_interval()
    for i in business_hour:
        data
        start_time=string_to_time(i.start_time_local)
        end_time=string_to_time(i.end_time_local)
        intervals=[[time["one_hour_ago"].time(), time["current_time"].time()], [start_time, end_time]]
        if(end_time<=time["one_hour_ago"].time()):
            data="NO"
        elif((start_time<=time["one_hour_ago"].time()) and (end_time<=time["current_time"].time())):
            data=get_intersection_of_intervals(intervals)
        elif(((start_time>=time["one_hour_ago"].time()) and (start_time<time["current_time"].time())) and (end_time>time["current_time"].time())):
            data=get_intersection_of_intervals(intervals)
        else:
            data="no"
    return {"message": data}
