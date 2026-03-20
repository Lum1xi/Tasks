from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routers.tasks import tasks as tasks_router

app = FastAPI(title="Task Manager API", description="API for managing tasks", version="0.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(tasks_router)
