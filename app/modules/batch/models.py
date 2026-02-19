from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Date, func
from app.core.database import Base
from typing import Optional
from datetime import date


class Batch(Base):
    __tablename__ = 'batches'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    medicine_id: Mapped[int] = mapped_column(ForeignKey("medicines.id"), nullable=False)
    pharmacy_id: Mapped[int] = mapped_column(ForeignKey("pharmacies.id"), nullable=False)
    batch_number: Mapped[str] = mapped_column(String(50), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    expiry_date: Mapped[date] = mapped_column(nullable=False)
    created_at: Mapped[date] = mapped_column(server_default=func.now())
    updated_at: Mapped[Optional[date]] = mapped_column(onupdate=func.now())

    medicine = relationship("Medicine", back_populates='batches')
    pharmacy = relationship("Pharmacy", back_populates='batches')

