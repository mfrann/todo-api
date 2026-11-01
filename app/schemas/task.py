from datetime import datetime as dt
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)

class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    completed: bool | None = None
    
class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: dt
    updated_at: dt