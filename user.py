import json
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    __slots__ = ("chad_id" , "wallet_id" , "discord_id" , "twitter_id" , "c3" , "created_at" , "updated_at")
    chad_id:str
    wallet_id:str
    discord_id:str
    twitter_id:str
    c3:int
    created_at:datetime
    updated_at:datetime

def __init__(
        self, 
        chad_id: str,
        wallet_id: str,
        discord_id: str,
        twitter_id: str,
        c3: int,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
        ) -> None:
        self.chad_id = chad_id
        if not isinstance(self.chad_id, str):
            raise TypeError("chad id should be a string")
        
        self.wallet_id = wallet_id
        if not isinstance(self.wallet_id, str):
            raise TypeError("wallet id should be a string")
        
        self.discord_id = discord_id
        if not isinstance(self.discord_id, str):
            raise TypeError("discord id should be a string")
        
        self.twitter_id = twitter_id
        if not isinstance(self.twitter_id, str):
            raise TypeError("twitter id should be a string")
        
        self.c3 = c3
        if not isinstance(self.c3, int):
            raise TypeError("c3 should be a int")
        
        self.created_at = created_at
        if not isinstance(self.created_at, datetime):
            raise TypeError("created at should be a datetime")
        
        self.updated_at = updated_at
        if not isinstance(self.updated_at, datetime):
            raise TypeError("updated at should be a datetime")
        

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

  