import sqlalchemy as sa
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, unique=True, index=True, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)
    hourly_rate = sa.Column(sa.Float, nullable=True)
    wallos_api_key = sa.Column(sa.String, nullable=True)
    wallos_host_url = sa.Column(sa.String, nullable=True)
    
    
    