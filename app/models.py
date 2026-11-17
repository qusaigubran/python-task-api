from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(description="Short description of the task", examples=["Study FastAPI"])
    completed: bool = Field(default=False, description="Whether the task is done", examples=[False])


class TaskUpdate(BaseModel):
    title: str = Field(description="New title for the task", examples=["Study FastAPI routing"])
    completed: bool = Field(description="New completion status", examples=[True])
