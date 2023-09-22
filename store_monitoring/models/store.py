from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class Store(BaseModel):
    __tablename__ = "store"

    id=Column(Integer, primary_key=True, autoincrement=True)
    store_id=Column(BigInteger, nullable=False)
    timezone=Column(String)
