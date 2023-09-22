from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class Report(BaseModel):
    __tablename__ = "report"

    id=Column(Integer, primary_key=True, autoincrement=True)
    status=Column(String, nullable=False)
