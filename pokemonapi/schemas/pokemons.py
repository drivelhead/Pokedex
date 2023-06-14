from pydantic import BaseModel, validator, BaseConfig
from typing import List, Optional

BaseConfig.arbitrary_types_allowed = True

class Pokemon(BaseModel):
    id: int
    classification: str
    name: str
    percentage_male: float
    type1: str
    type2: str
    generation: int
    is_legendary: bool
    

    class Config():
        orm_mode = True   


class PokemonStats(BaseModel):
    id: int
    pokemon_id: int
    attack: int
    defense: int
    speed: int
    weight_kg: float
    # against_bug: float
    # against_dark: float   
    # against_dragon: float
    # against_electric: float
    # against_fairy: float
    # against_fight: float
    # against_fire: float
    # against_flying: float
    # against_ghost:float
    # against_grass: float
    # against_ground: float
    # against_ice: float
    # against_normal: float
    # against_poison: float
    # against_psychic: float
    # against_rock: float
    # against_steel: float
    # against_water: float
    # base_egg_steps: int
    # base_happiness: int
    # base_total: int
    #capture_rate: str
    defense: int
    experience_growth: int
    height_m: float
    hp: int
    sp_attack: int
    sp_defense: int
    
    class Config():
        orm_mode = True


        
class PokeStatsRM(BaseModel):
     stats: List[PokemonStats]
 
    
class ShowPandS(BaseModel):
    name: str
    classification: str 
    generation: int
    type1: str
    type2: str
    is_legendary: bool
    pokemonstats: List[PokemonStats]

    @validator('pokemonstats')
    def check_pokemonstats(cls, lst):
        return lst or []

    class Config():
        orm_mode = True


    #@validator("title")
    #def title_must_be_min_3_characters(cls, v): 
       # if len(v) < 3:
           # raise ValueError("Title must be at least 3 characters")
        
        #return v
    
#class PokemonResponseModel(Pokemon):
#      id: int    
    
      
