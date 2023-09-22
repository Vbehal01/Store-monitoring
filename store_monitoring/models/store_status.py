from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class StoreStatus(BaseModel):
    __tablename__ = "store_status"

    id = Column(Integer, primary_key=True)
    store_id = Column(ForeignKey("store.id", ondelete="CASCADE"), nullable=False)
    status=Column(String)
    timestamp=Column(TIMESTAMP)
