from typing import List
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from app.core.database import get_session
from app.models.models import MessageModel, ErrorMessageModel
from app.schemas.message_schemas import Message


async def create_message(data: Message) -> MessageModel:
    try:
        async with get_session() as session:
            created_message = MessageModel(**data.model_dump())
            session.add(created_message)
            await session.commit()
            return created_message
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error creating message: {e}")


async def create_error_messages(data: Message) -> ErrorMessageModel:
    try:
        async with get_session() as session:
            created_message = ErrorMessageModel(**data.model_dump())
            session.add(created_message)
            await session.commit()
            return created_message
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error creating message: {e}")


async def get_messages() -> List[MessageModel]:
    try:
        async with get_session() as session:
            result = await session.execute(select(MessageModel))
            messages = result.scalars().all()
            return list(messages)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving messages: {e}")


async def delete_messages():
    try:
        async with get_session() as session:
            await session.execute(delete(MessageModel))
            await session.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error deleting messages")
