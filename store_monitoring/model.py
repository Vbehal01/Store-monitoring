from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger
from database import Base

class StoreStatus(Base):
    __tablename__="store_status"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(BigInteger)
    timestamp_utc=Column(TIMESTAMP)
    status=Column(String)

    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = status
        self.timestamp_utc = timestamp_utc

class MenuHours(Base):
    __tablename__="menu_hours"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(BigInteger)
    day=Column(Integer)
    start_time_local=Column(String)
    end_time_local=Column(String)

    def __inti__(self, store_id, day, start_time_local, end_time_local):
        self.store_id=store_id
        self.day=day
        self.start_time_local=start_time_local
        self.end_time_local=end_time_local

class BqResults(Base):
    __tablename__="bq_results"

    store_id=Column(BigInteger, primary_key=True)
    timezone_str=Column(String)       

    def __init__(self, store_id, timezone_str):
        self.store_id=store_id
        self.timezone_str=timezone_str                                                                                                                                                     