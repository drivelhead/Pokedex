from pydantic import BaseModel, validator


class Anything(BaseModel):
    title: str
    description: str

    @validator("title")
    def title_must_be_min_3_characters(cls, v): 
        if len(v) < 3:
            raise ValueError("Title must be at least 3 characters")
        
        return v
    
class AnythingResponseModel(Anything):
    id: int    

    class Config():
        orm_mode = True