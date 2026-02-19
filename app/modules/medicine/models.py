from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Text
from app.core.database import Base
from app.modules.batch.models import Batch
from typing import List


class Medicine(Base):
    __tablename__ = 'medicines'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    category: Mapped[str | None] = mapped_column(String(50), default=None)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    batches: Mapped[List["Batch"]] = relationship(
        "Batch",
        back_populates="medicine",
        cascade="all, delete-orphan"
    )

