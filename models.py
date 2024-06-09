from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Restaurant(Base):
    __tablename__ = "restaurant"
    
    id : Mapped[str] = mapped_column(primary_key=True)
    rating: Mapped[int]
    name: Mapped[str]
    site: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    street: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]