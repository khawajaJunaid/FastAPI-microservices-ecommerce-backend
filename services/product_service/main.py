from fastapi import FastAPI
from api.routes import router as product_router

app = FastAPI()
app.include_router(product_router, tags=["products"], prefix="/products")


