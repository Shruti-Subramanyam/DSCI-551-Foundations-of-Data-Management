from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from typing import List
from app.schema import Farmer, FarmerUpdate
from app.crud import (create_farmer_db, list_farmers_db, find_farmer_db,
                              update_farmer_db, delete_farmer_db, delete_product_db)

router = APIRouter()

@router.post("/", response_description="Create a new farmer", status_code=status.HTTP_201_CREATED, response_model=Farmer)
def create_farmer(request: Request, farmer: Farmer = Body(...)):
    created_farmer = create_farmer_db([request.app.database0, request.app.database1], farmer)
    return created_farmer


@router.get("/", response_description="List all farmers", response_model=List[Farmer])
def list_farmers(request: Request):
    farmers = list_farmers_db([request.app.database0, request.app.database1])
    return farmers


@router.get("/{id}", response_description="Get a single farmer by id", response_model=Farmer)
def find_farmer(id: str, request: Request):
    farmer = find_farmer_db([request.app.database0, request.app.database1], id)
    if farmer is not None:
        return farmer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Farmer with ID {id} not found")


@router.patch("/{id}", response_description="Update a farmer", response_model=Farmer)
def update_farmer(id: str, request: Request, farmer: FarmerUpdate = Body(...)):
    existing_farmer = update_farmer_db([request.app.database0, request.app.database1], id, farmer)
    if existing_farmer is not None:
        return existing_farmer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Farmer with ID {id} not found")


@router.delete("/{id}", response_description="Delete a farmer")
def delete_farmer(id: str, request: Request, response: Response):
    deleted_count = delete_farmer_db([request.app.database0, request.app.database1], id)
    if deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Farmer with ID {id} not found")


@router.delete("/{id}/product_list/{product_name}", response_description="Remove a product from a farmer")
def delete_product(id: str, product_name: str, request: Request, response: Response):
    deleted_count = delete_product_db([request.app.database0, request.app.database1], id, product_name)
    if deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {product_name} with ID {id} not found")
