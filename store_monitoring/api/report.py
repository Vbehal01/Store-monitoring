import csv
from fastapi import APIRouter
from datetime import datetime


from ..models.store import Store
from ..models.store_business_hours import StoreBusinesHours
from ..models.store_status import StoreStatus
from ..models.report import Report
from ..models.report_details import ReportDetails

from .utils.logging import get_logger
from ..constants import STORE_TIMEZONE_FILE_PATH, STORE_BUSINESS_HOURS_FILE_PATH, STORE_STATUS_FILE_PATH, DEFAULT_TIMEZONE, REPORT_DIR_PATH

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

def generate_report(report_id, report_file_path):
    report = Report.find(report_id)
    report_details = ReportDetails.where(report_id=report_id).all()
    rows = []
    column_names = [
        "store_id",
        "uptime_last_hour",
        "uptime_last_day",
        "update_last_week",
        "downtime_last_hour",
        "downtime_last_day",
        "downtime_last_week",
    ]

    for report_detail in report_details:
        row = {
            "store_id": report_detail.store_id,
            "uptime_last_hour": report_detail.uptime_last_hour,
            "uptime_last_day": report_detail.uptime_last_day,
            "update_last_week": report_detail.update_last_week,
            "downtime_last_hour": report_detail.downtime_last_hour,
            "downtime_last_day": report_detail.downtime_last_day,
            "downtime_last_week": report_detail.downtime_last_week,
        }

    with open(report_file_path, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(rows)

@router.post("/trigger_report/", tags=["report"])
async def trigger_report():
    report = Report.create(status="processing")
    sync_stores()
    sync_store_business_hours()
    sync_store_status()

    return {
        "report_id": report.id,
        "status": "processing"
    }


@router.get("/get_report/{id}", tags=["report"])
async def get_report(id):
    report = Report.find(id=id)
    if report.status in ["processing"]:
        return {
            "status": report.status
        }
    else:
        report_file_path = f"{REPORT_DIR_PATH}/report-{id}.csv"
        generate_report(id, report_file_path)
        return {
            "report_file_path": report_file_path,
            "status": "complete"
        }

