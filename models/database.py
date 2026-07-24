from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Incident(Base):
    __tablename__ = "incidents"

    runId = Column(String, primary_key=True)
    profile = Column(String)
    status = Column(String)
    body = Column(Text)
