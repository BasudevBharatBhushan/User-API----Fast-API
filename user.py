import json
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    # __slots__ = ("chad_id" , "wallet_id" , "discord_id" , "twitter_id" , "c3" , "created_at" , "updated_at")
    chad_id:str
    wallet_id:str
    discord_id:str
    twitter_id:str
    c3:int
    created_at:datetime
    updated_at:datetime

def __init__(
        self, 

        wallet_id: str,
    
        ) -> None:

        self.wallet_id = wallet_id
        if not isinstance(self.wallet_id, str):
            raise TypeError("wallet id should be a string")
        

        

def to_dict(self):
    user_json: json = {
        "chad_id": self.chad_id,
        "wallet_id": self.wallet_id,
        "discord_id": self.discord_id,
        "twitter_id": self.twitter_id,
        "c3": self.c3,
        "created_at": self.created_at,
        "updated_at": self.updated_at,

    }
    return user_json

class UserSchema(User):
    class Config:
        orm_mode = True

  