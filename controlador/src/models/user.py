from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from server import Server


class User(Server.database.Model):
    __tablename__: str = "usuarios"
    id: int = Column(
        Integer, primary_key=True, nullable=False, unique=True, autoincrement=True
    )
    id_uuid: str = Column(
        UUID(False), unique=True, nullable=False, default=lambda: str(uuid4())
    )
    email: str = Column(String(200))
    password: str = Column(Text)
