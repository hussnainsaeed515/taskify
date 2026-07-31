from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title:str
    description:Optional[str]=None
    
class TaskResponse(BaseModel):
    id:int
    title:str
    description:Optional[str]=None
    created_at:datetime
    is_completed:bool
    class config:
        from_attributes=True


