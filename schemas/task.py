from enum import Enum
from pydantic import model_validator, BaseModel


class Status(str, Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    completed = 'completed'


class Task(BaseModel):
    title: str
    description: str
    state: str


class CreateTask(BaseModel):
    title: str
    description: str
    state: Status = Status.pending

    @model_validator(mode='before')
    def validate_state(cls, values):
        state = values.get('state')
        if state and state not in Status.__members__:
            raise ValueError(f"Invalid state: {state}. Allowed values are: {', '.join(Status.__members__.keys())}")
        return values


class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    state: Status | None = None


class DeleteTask(BaseModel):
    id: int
