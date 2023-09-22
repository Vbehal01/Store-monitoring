from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship

from .base import BaseModel


class ReportDetails(BaseModel):
    __tablename__ = "report_details"

    id=Column(Integer, primary_key=True, autoincrement=True)
    status=Column(String, nullable=False)
    uptime_last_hour=Column(Integer)
    uptime_last_day=Column(Integer)
    update_last_week=Column(Integer)
    downtime_last_hour=Column(Integer)
    downtime_last_day=Column(Integer)
    downtime_last_week=Column(Integer)
    report_details_id = Column(ForeignKey("report.id", ondelete="CASCADE"), nullable=False)
    store_id = Column(ForeignKey("store.id", ondelete="CASCADE"), nullable=False)

    report = relationship("Report", back_populates="report_details")
