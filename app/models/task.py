from sqlalchemy import column ,integer,boolean,string,datetime
from datetime import datetime
from app.database import Base
class task(Base):
    __tablename__=="task"
    id=column(primary_key=True)
    title=column(string,nullable=False)
    description=column(string,nullable=True)
    is_completed=column(boolean,default=False)
    created_at=column(datetime,default=datetime.utcnow)
