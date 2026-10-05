from fastapi import FastAPI

from routes.stu_routes import router

app = FastAPI(title='Student-CRUD-202326900090')

app.include_router(router)