from fastapi import APIRouter, Request, Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import Menu
from typing import List, Optional

router = APIRouter()

#Route pour retourner l'ensemble des menus
@router.get('/', response_description="List All menus")
async def list_menu(request: Request):
    query = request.app.mongodb['Menu'].find()
    results = [Menu(**menu) async for menu in query]
    return results
    

@router.post('/', response_description="Create menu")
async def create_menu(request: Request, menu: Menu = Body(...)):
    menu = jsonable_encoder(menu)
    new_menu = await request.app.mongodb['Menu'].insert_one(menu)
    
    created_menu = await request.app.mongodb["Menu"].find_one({"_id": new_menu.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_menu)
