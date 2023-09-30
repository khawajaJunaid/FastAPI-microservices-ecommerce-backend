from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.get("/",status_code=status.HTTP_200_OK)
def get_products():
    '''
    Get all products
    '''
    return {"products": "product list"}