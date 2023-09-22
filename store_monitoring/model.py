from sqlalchemy import Column, Integer, String, TIMESTAMP, BigInteger
from database import Base
from datetime import datetime

class StoreStatusUpdates(Base):
    __tablename__="store_status_updates"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(BigInteger)
    timestamp_utc=Column(TIMESTAMP)
    status=Column(String)

    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = status
        self.timestamp_utc = timestamp_utc

class StoreBusinessHours(Base):
    __tablename__ = "store_business_hours"

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(BigInteger)
    day = Column(Integer)
    start_time_local = Column(String)
    end_time_local = Column(String)

    def __init__(self, store_id, day, start_time_local, end_time_local):
        self.store_id = store_id
        self.day = day
        self.start_time_local = start_time_local
        self.end_time_local = end_time_local

class StoreTimezone(Base):
    __tablename__="store_time_zone"

    store_id=Column(BigInteger, primary_key=True)
    timezone_str=Column(String)       

    def __init__(self, store_id, timezone_str):
        self.store_id=store_id
        self.timezone_str=timezone_str                                                                                                                                                     