from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from webapp_reactpy.gallery import Gallery
# from webapp_reactpy.todolist import TodoList

app = FastAPI()
# configure(app, TodoList)
configure(app, Gallery)
