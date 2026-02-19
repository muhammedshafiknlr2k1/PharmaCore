from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from typing import List
from app.modules.batch.models import Batch


class Pharmacy(Base):
    __tablename__ = 'pharmacies'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=True)

    batches: Mapped[List["Batch"]] = relationship(
        "Batch",
        back_populates="pharmacy",
        cascade="all, delete-orphan"
    )