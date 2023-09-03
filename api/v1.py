import datetime
from typing import List
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError, available_timezones

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()


class v1_ResponseTime(BaseModel):
    timestamp: float
    display: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    day_of_year: int
    day_of_week: int
    timezone: str
    offset: int
    dst: bool

    class Config:
        json_schema_extra = {
            "example": {
                "timestamp": 1688600651.170084,
                "display": "2023-07-06 01:44:11",
                "year": 2023,
                "month": 7,
                "day": 6,
                "hour": 1,
                "minute": 44,
                "second": 11,
                "day_of_year": 187,
                "day_of_week": 4,
                "timezone": "UTC",
                "offset": 0,
                "dst": False
            }
        }


@router.get("/", response_model=v1_ResponseTime, responses={400: {"description": "Invalid timezone"}})
async def get_time(timezone: str = "UTC") -> v1_ResponseTime:
    """
    Get the current time in the specified timezone.
    """
    utc_dt = datetime.datetime.utcnow()
    try:
        tz = ZoneInfo(timezone)
    except ZoneInfoNotFoundError:
        raise HTTPException(status_code=400, detail="Invalid timezone")
    local_dt = utc_dt.replace(tzinfo=ZoneInfo("UTC")).astimezone(tz)
    return {
        "timestamp": utc_dt.timestamp(),
        "display": local_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "year": local_dt.year,
        "month": local_dt.month,
        "day": local_dt.day,
        "hour": local_dt.hour,
        "minute": local_dt.minute,
        "second": local_dt.second,
        "day_of_year": local_dt.timetuple().tm_yday,
        "day_of_week": local_dt.isoweekday(),
        "timezone": local_dt.tzname(),
        "offset": local_dt.utcoffset().total_seconds(),
        "dst": local_dt.dst() != datetime.timedelta(0)
    }


@router.get("/timezones")
async def get_timezones() -> List[str]:
    """
    Get a list of available timezones.
    """
    return available_timezones()
