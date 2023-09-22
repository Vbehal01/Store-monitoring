import csv
from fastapi import APIRouter
from datetime import datetime


from ..models.store import Store
from ..models.store_business_hours import StoreBusinesHours
from ..models.store_status import StoreStatus
from ..models.report import Report

from .utils.logging import get_logger
from ..constants import STORE_TIMEZONE_FILE_PATH, STORE_BUSINESS_HOURS_FILE_PATH, STORE_STATUS_FILE_PATH, DEFAULT_TIMEZONE

router = APIRouter()

logger = get_logger(__name__)

def sync_stores():
    logger.info("Syncing stores...")
    with open (STORE_TIMEZONE_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            store_id=row["store_id"]
            timezone_str=row["timezone_str"]
            Store.create(actual_store_id=store_id, timezone=timezone_str)

def sync_store_business_hours():
    logger.info("Syncing store business hours...")
    with open (STORE_BUSINESS_HOURS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            actual_store_id=row["store_id"]
            day=row["day"]
            start_time_local=row["start_time_local"]
            end_time_local=row["end_time_local"]
            store = Store.where(actual_store_id=actual_store_id).first()
            if store is None:
                logger.info("Skipping business hour entry with actual store id {actual_store_id}")
                continue
            StoreBusinesHours.create(day=day, start_time_local=start_time_local, end_time_local=end_time_local, store_id=store.id)


def sync_store_status():
    logger.info("Syncing store status...")
    with open (STORE_STATUS_FILE_PATH, mode='r', encoding='utf-8-sig') as file:
        file_content=csv.DictReader(file)
        for row in file_content:
            actual_store_id=row["store_id"]
            status=row["status"]
            timestamp_str=row["timestamp_utc"]
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f %Z")
            store = Store.where(actual_store_id=actual_store_id).first()
            if store is None:
                logger.info("Creating as store doesn't exist store id {actual_store_id}")
                store = Store.create(actual_store_id=actual_store_id, timezone=DEFAULT_TIMEZONE)
            StoreStatus.create(timestamp=timestamp, status=status, store_id=store.id)


@router.post("/trigger_report/", tags=["report"])
async def trigger_report():
    Report.create()
    sync_stores()
    sync_store_business_hours()
    sync_store_status()

    return [{"username": "Rick"}, {"username": "Morty"}]
