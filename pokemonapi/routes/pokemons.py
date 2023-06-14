from fastapi import APIRouter, Depends, UploadFile, Response, status, HTTPException
from fastapi.responses import JSONResponse
from schemas.pokemons import Pokemon, ShowPandS, PokeStatsRM
#from database.dataset import pokemonDataBase
from database.connection import get_db
from database.models import Pokemon as PokemonTableModel
from database.models import PokemonStats as StatsTableModel
from sqlalchemy.orm import Session, subqueryload, joinedload
import csv
from typing import List


router = APIRouter(prefix ="/pokemons", tags=["pokemons"])


# #get pokemon, show all data, nested list of stats
# @router.get("/", response_model=list[ShowPandS])
# def get_All_Pokemon(db: Session = Depends(get_db)):
#     pokemons = db.query(PokemonTableModel).options(joinedload(PokemonTableModel.pokemonstats).subqueryload(StatsTableModel.pokemon)).all()
    
#     return pokemons 

#Display all pokemon in pokemon csv. 
@router.get("/")
def get_all_Pokemon(db: Session = Depends(get_db)):
    pokemon = db.query(PokemonTableModel).all()
    return pokemon 

#get one result by name
@router.get("/{pokemonName}")
def getSpecific_Pokemon(pokemonName: str, db: Session = Depends(get_db)):
    pokemon = db.query(PokemonTableModel).filter(PokemonTableModel.name.ilike(f"%{pokemonName}%")).first()
    if pokemon:
       return pokemon
    return {"message": "No such Monster"}


# get only stats by id
@router.get("/stats/{id}")
def stats_Only(id: int, db: Session = Depends(get_db)):
    stats = db.query(StatsTableModel).filter(StatsTableModel.id == id).first()
    if stats:
       return stats
    return {"message": "No stats found"}

#by id, get name and basic info
@router.get("/id/{pokemon_id}", status_code=200, response_model=List[ShowPandS])
def getPokemon_By_Id(pokemon_id: int, response:Response, db: Session = Depends(get_db)):
    # avoid n+1 problem with eager loading using subqueryload (will be discussed in the session remind me if I forget please :))
    pokemons = db.query(PokemonTableModel).filter(PokemonTableModel.id == pokemon_id).all()
    if not pokemons:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                           detail = f"No Monster found at {pokemon_id}")
     

    return pokemons

# # Define a route to retrieve the combined data from the tables
# @router.get("/pokemon_stats")
# def get_pokemon_stats(db: Session = Depends(get_db)):
#     # Query the database to retrieve the necessary data
#     data = (
#         db.query(PokemonTableModel.id, PokemonTableModel.name, StatsTableModel)
#         .join(StatsTableModel)
#         .options(joinedload(PokemonTableModel.stats))
#         .all()
#     )
#     response_data = []
#     for row in data:
#         pokemon_stats = row[2]
#         pokemon_stats_dict = pokemon_stats.__dict__.copy()
#         del pokemon_stats_dict["_sa_instance_state"]
#         pokemon_stats_response = StatsTableModel(**pokemon_stats_dict)
#         response_data.append(pokemon_stats_response)

#         pokemon_stats_response_model = PokeStatsRM(
#         id=row[0],
#         name=row[1],
#         stats=response_data,
#     )
#     return JSONResponse(content=pokemon_stats_response_model.dict())


#@router.get("/pokemon", response_model=List[PokeStatsResponseModel])
#def getPokeStats(db: Session = Depends(get_db)):
    #pokemon = db.query(PokemonTableModel).filter(subqueryload(PokemonTableModel.name.stats)).all()
    #if pokemon:
        #return pokemon


@router.post("/")
def addPokemon(pokemon: Pokemon, db: Session = Depends(get_db)):
    pokemonData = PokemonTableModel(name=pokemon.name, type1=pokemon.type1)
    db.add(pokemonData)
    db.commit()
    db.refresh(pokemonData)
    return {"data": pokemonData}




# upload csv for core info
@router.post("/pokemons/")
def uploadCSVFileToPokemonDatabase(file: UploadFile, db: Session = Depends(get_db)):
    fileContent = file.file.read().decode("utf-8")
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)
    for row in rows:
        print(row)
        pokemon = PokemonTableModel(id=row[0], classification=row[1], name=row[3], percentage_male=float(row[4]) if row[4] else None, type1=row[5], type2=row[6], generation=row[7], is_legendary=False if row[8]== "0" else True)
        db.add(pokemon)
    db.commit()   

# upload csv for stats info
@router.post("/pokemonstats/")
def uploadCSVFileToPokemonStatsDatabase(file: UploadFile, db: Session = Depends(get_db)):
    fileContent = file.file.read().decode("utf-8")
    rows = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)
    for row in rows: 
        pokemonStats = StatsTableModel(pokemon_id=row[0], against_bug=row[1], against_dark=row[2], against_dragon=row[3], against_electric=row[4], against_fairy=row[5], against_fight=row[6], against_fire=row[7], against_flying=row[8], against_ghost=row[9], against_grass=row[10], against_ground=row[11], against_ice=row[12], against_normal=row[13], against_poison=row[14], against_psychic=row[15], against_rock=row[16], against_steel=row[17], against_water=row[18], attack=row[19], base_egg_steps=row[20], base_happiness=row[21], base_total=row[22], defense=row[24], experience_growth=row[25], height_m=row[26] if row [26] else None, hp=row[27], sp_attack=row[28], sp_defense=row[29], speed=row[30], weight_kg=row[31] if row[31] else None)
        db.add(pokemonStats)
    db.commit()




