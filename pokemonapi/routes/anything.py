from fastapi import APIRouter, Depends
from schemas.anything import Anything, AnythingResponseModel
from database.dataset import anythingDataBase
from database.connection import get_db
from database.models import Anything as AnythingTableModel
from sqlalchemy.orm import Session 

router = APIRouter(prefix ="/anything", tags=["anything"])


@router.get("/", response_model=list[AnythingResponseModel])
def getAnything(db: Session = Depends(get_db)):
    anything = db.query(AnythingTableModel).all()
    return anything 

@router.post("/")
def addAnything(anything: Anything, db: Session = Depends(get_db)):
    anythingData = AnythingTableModel(title=anything.title, description=anything.description)
    db.add(anythingData)
    db.commit()
    db.refresh(anythingData)
    return {"data": anythingData}


@router.delete("/{anythingId}")
def deleteAnything(anythingId: int):
   # for drum in drumDataBase:
   #    if drum["Id"] == drumId:
    #        drumDataBase.remove(drum) 
     #       return{"data": drumDataBase}
     newSet = [anything for anything in anythingDataBase if anything["id"] != anythingId]
     return {"data": newSet}  

@router.get("/{anythingName}")
def getSpecificAnything(anythingName: str, db: Session = Depends(get_db)):
    anything = db.query(AnythingTableModel).filter(AnythingTableModel.title.ilike(f"%{anythingName}%")).first()
    if anything:
                return {"data": anything}
    return {"message": "Found nothing"}