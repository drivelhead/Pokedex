from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    

    anythings = relationship("Anything", backref="owner")


class Anything(Base):
    __tablename__ = "anythings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

#class User(Base):
  #  __tablename__ = "users"
   # id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    #email = Column(String(255), unique=True)
    #password = Column(String(255))
    #created_at = Column(DateTime, default=datetime.now)
    #name = Column(String(50))

#pokemons =relationship("Pokemon", backref="own")

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    classification = Column(String)
    name = Column(String)
    percentage_male = Column(Float)
    type1 = Column(String)
    type2 = Column(String)
    generation = Column(Integer)
    is_legendary = Column(Boolean)
    # One to one relationship with PokemonStats, uselist = False means that there will be only one PokemonStats object for each Pokemon object
    pokemonstats = relationship("PokemonStats", back_populates="pokemon", uselist=False, lazy="subquery")


class PokemonStats(Base):
    __tablename__ = "pokemonstats"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    against_bug = Column(Float)
    against_dark = Column(Float)   
    against_dragon = Column(Float)
    against_electric = Column(Float)
    against_fairy = Column(Float)
    against_fight = Column(Float)
    against_fire = Column(Float)
    against_flying = Column(Float)
    against_ghost = Column(Float)
    against_grass = Column(Float)
    against_ground = Column(Float)
    against_ice = Column(Float)
    against_normal = Column(Float)
    against_poison = Column(Float)
    against_psychic = Column(Float)
    against_rock = Column(Float)
    against_steel = Column(Float)
    against_water = Column(Float)
    attack = Column(Integer, nullable=True)
    base_egg_steps = Column(Integer)
    base_happiness = Column(Integer)
    base_total = Column(Integer)
    #capture_rate = Column(Varchar)
    defense = Column(Integer)
    experience_growth = Column(Integer)
    height_m = Column(Float, nullable=True)
    hp = Column(Integer)
    sp_attack = Column(Integer)
    sp_defense = Column(Integer)
    speed = Column(Integer)
    weight_kg = Column(Float, nullable=True)

    pokemon = relationship("Pokemon", back_populates="pokemonstats")

    #pokemon = relationship("Pokemon", back_populates="pokemonstats")

