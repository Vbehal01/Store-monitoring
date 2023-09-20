from sqlalchemy import Column, Integer, String, TIMESTAMP, TIME, BigInteger
from database import Base

class StoreStatus(Base):
    __tablename__="store_status"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(BigInteger)
    timestamp_utc=Column(TIMESTAMP)
    status=Column(String)

    class StoreStatus:
        def __init__(self, store_id, status, timestamp_utc):
            self.store_id = store_id
            self.status = status
            self.timestamp_utc = timestamp_utc

class StoreHours(Base):
    __tablename__="store_hours"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(Integer)
    dayofweek=Column(Integer)
    start_time_local=Column(TIME)
    end_time_local=Column(TIME)

class StoreTimeZone(Base):
    __tablename__="store_timezone"

    store_id=Column(Integer, primary_key=True)
    timezone_str=Column(String)                                                                                                                                                            