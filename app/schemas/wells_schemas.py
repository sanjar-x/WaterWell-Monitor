from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class WelleSchema(BaseModel):
    name: Optional[str] = None
    number: str
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None


class WelleUpdateSchema(BaseModel):
    name: Optional[str] = None
    number: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    depth: Optional[str] = None


from datetime import datetime


class WellSchema(BaseModel):
    well_id: UUID
    name: str
    number: str
    address: str
    latitude: str
    longitude: str
    depth: str
    status: bool
    created_time: datetime
