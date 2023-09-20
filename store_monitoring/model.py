from sqlalchemy import Column, Integer, String, TIMESTAMP, TIME
from database import Base

class Input_1(Base):
    __tablename__="input_1"

    store_id=Column(Integer, primary_key=True)
    timestamp_utc=Column(TIMESTAMP)
    status=Column(String)

class Input_2(Base):
    __tablename__="input_2"

    store_id=Column(Integer, primary_key=True)
    dayofweek=Column(Integer)
    start_time_local=Column(TIME)
    end_time_local=Column(TIME)

class Input_3(Base):
    __tablename__="input_3"

    store_id=Column(Integer, primary_key=True)
    timezone_str=Column(String)