from sqlalchemy.orm import mapped_column, Mapped, declarative_base
from sqlalchemy import Integer, String, Text

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
