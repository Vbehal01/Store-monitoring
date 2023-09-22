from fastapi import APIRouter

from ..models.store import Store
from ..models.store_business_hours import StoreBusinesHours
from ..models.store_status import StoreStatus
from .utils.logging import get_logger

router = APIRouter()

logger = get_logger(__name__)

@router.post("/trigger_report/", tags=["report"])
async def trigger_report():
    return [{"username": "Rick"}, {"username": "Morty"}]
