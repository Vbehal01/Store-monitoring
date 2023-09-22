from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class StoreBusinesHours(BaseModel):
    __tablename__ = "store_business_hours"

    id=Column(Integer, primary_key=True, autoincrement=True)
    day=Column(Integer)
    start_time_local=Column(String)
    end_time_local=Column(String)
    store_id = Column(ForeignKey("store.id", ondelete="CASCADE"), nullable=False)