from datetime import UTC, datetime

from sqlalchemy import ForeignKey, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    password: Mapped[str | None] = mapped_column(String(150), nullable=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    signed_up_with: Mapped[str | None] = mapped_column(String(150), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

class Membership(Base):
    __tablename__ = 'memberships'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_free_trial: Mapped[bool] = mapped_column(Boolean, nullable=False)
    tier: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)


class Food(Base):
    __tablename__ = 'foods'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str | None] = mapped_column(String(150), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    nutritional_information_id: Mapped[int] = mapped_column(ForeignKey('nutritional_information.id'), nullable=False)

class NutritionalInformation(Base):
    __tablename__ = 'nutritional_information'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    per_amount: Mapped[int] = mapped_column(Integer, nullable=False)
    per_amount_measurement: Mapped[str] = mapped_column(String(10), nullable=False)
    energy: Mapped[int] = mapped_column(Integer, nullable=False)
    fat: Mapped[int] = mapped_column(Integer, nullable=False)
    on_which_saturates: Mapped[int] = mapped_column(Integer, nullable=False)
    carbohydrates: Mapped[int] = mapped_column(Integer, nullable=False)
    of_which_sugars: Mapped[int] = mapped_column(Integer, nullable=False)
    fibre: Mapped[int] = mapped_column(Integer, nullable=False)
    protein: Mapped[int] = mapped_column(Integer, nullable=False)
    salt: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    standardized_name: Mapped[str] = mapped_column(String(100), nullable=False)
    key_dangers: Mapped[str] = mapped_column(String(4096), nullable=False)
    key_negatives: Mapped[str] = mapped_column(String(4096), nullable=False)
    key_benefits: Mapped[str] = mapped_column(String(4096), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

class IngredientName(Base):
    __tablename__ = 'ingredient_names'

    ingredient_name: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    ingredient_id: Mapped[int] = mapped_column(ForeignKey('ingredients.id'), nullable=False)
