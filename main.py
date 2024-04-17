from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = {
    1: {"name": "Foo", "finished": True},
    2: {"name": "Bar", "description": "The bartenders", "finished": False},
    3: {"name": "Baz", "description": None, "finished": False},
}


class Task(BaseModel):
    name: str
    description: str = Field(default=None)
    finished: bool = Field(default=False)


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    if not tasks.get(task_id):
        raise HTTPException(status_code=404, detail="tache n'est pas trouvée")
    return tasks[task_id]


@app.get("/tasks")
def read_task():
    return tasks


@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    new_id = len(tasks) + 1
    tasks[new_id] = jsonable_encoder(task)
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    stored_task_data = tasks[task_id]
    stored_task_model = Task(**stored_task_data)
    update_data = task.model_dump(exclude_unset=True)  # exclude_unset to skip default values
    updated_task = stored_task_model.model_copy(update=update_data)
    tasks[task_id] = jsonable_encoder(updated_task)
    return updated_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    del tasks[task_id]


