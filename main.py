from fastapi import FastAPI

from routes.stu_routes import router

app = FastAPI(title='Student-CRUD-20232690009')

app.include_router(router)