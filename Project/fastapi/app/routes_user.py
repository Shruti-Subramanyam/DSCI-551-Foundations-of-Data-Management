from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from typing import List
from app.schema import Farmer, Purchase, Review
from app.crud import (list_farmers_by_product_db, purchase_product_db, review_product_db)

router = APIRouter()


@router.get("/find/{product_name}", response_description="List farmers by product", response_model=List[Farmer])
def list_farmers_by_product(product_name: str, request: Request):
    farmers = list_farmers_by_product_db([request.app.database0, request.app.database1], product_name)
    return farmers


@router.patch("/purchase/{id}/{product_name}/", response_description="Purchase a product", response_model=Farmer)
def purchase_product(id: str, product_name: str, request: Request, purchase: Purchase = Body(...)):
    existing_farmer = purchase_product_db([request.app.database0, request.app.database1], id, product_name, purchase)
    if existing_farmer is not None:
        return existing_farmer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Farmer with ID {id} not found")


@router.patch("/review/{id}/{product_name}/", response_description="Review a product", response_model=Farmer)
def review_product(id: str, product_name: str, request: Request, review: Review = Body(...)):
    existing_farmer = review_product_db([request.app.database0, request.app.database1], id, product_name, review)
    if existing_farmer is not None:
        return existing_farmer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Farmer with ID {id} not found")
