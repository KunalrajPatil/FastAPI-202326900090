from fastapi import FastAPI

from routes.stu_routes import router

app = FastAPI(title='Student-CRUD')

app.include_router(router)