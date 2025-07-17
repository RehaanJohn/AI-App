from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///app.db', echo=True)
Base = declarative_base()

class Challenge(Base):
    __tablename__ = 'challenges'
    
    id = Column(Integer, primary_key=True)
    difficulty = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=False)
    options = Column(String, nullable=True)
    correct_answer = Column(Integer, nullable=True)
    explanation = Column(String, nullable=True)

    def __repr__(self):
        return f"<Challenge(title={self.title}, description={self.description})>"


class ChallengeQuota(Base):
    __tablename__ = 'challenge_quotas'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    last_reset_date = Column(DateTime, default=datetime.now)
    quota_remaining = Column(Integer, default=50)

    def __repr__(self):
        return f"<ChallengeQuota(user_id={self.user_id}, challenge_type={self.challenge_type}, quota={self.quota})>"
    

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()