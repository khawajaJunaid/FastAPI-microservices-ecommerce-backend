from fastapi import FastAPI
from api.routes import router as product_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(product_router, tags=["products"], prefix="/products")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

