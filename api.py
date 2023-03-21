from fastapi import APIRouter
from dbclient import user_collection
from user import User, UserSchema
from datetime import datetime



user = APIRouter()

@user.post("/user")
async def create_user(user: User)->bool:
    try:
        user_dict = user.dict()
        user_dict["created_at"] = datetime.now() 
        result = user_collection.insert_one(user_dict)  
        inserted_id = str(result.inserted_id) 
        chad_id = inserted_id
        update_result = user_collection.update_one({"_id": result.inserted_id}, {"$set": {"chad_id": chad_id }}).acknowledged  
        return update_result
    except Exception as e:
        return {"message": str(e)}
    
@user.post("/user/wallet_id")
async def create_user(wallet_id: str)->bool:
    try:
        result = user_collection.insert_one({"wallet_id": wallet_id, "created_at": datetime.now()})
        inserted_id = str(result.inserted_id) 
        chad_id = inserted_id
        update_result = user_collection.update_one({"_id": result.inserted_id}, {"$set": {"chad_id": chad_id }}).acknowledged  
        return update_result
    except Exception as e:
        return {"message": str(e)}

@user.put("/user/discord/{chad_id}")
async def update_user_discord_Id(chad_id: str, discord_id:str):
    try:
        result = user_collection.update_one({"chad_id": chad_id}, {"$set":{"discord_id":discord_id , "updated_at":datetime.now()}}).acknowledged
        return result
    except Exception as e:
        return {"message": str(e)}

@user.put("/user/twitter/{chad_id}")
async def update_user_twitter_Id(chad_id: str, twitter_id:str):
    try:
        result = user_collection.update_one({"chad_id": chad_id}, {"$set":{"twitter_id":twitter_id , "updated_at":datetime.now()}}).acknowledged
        return result
    except Exception as e:
        return {"message": str(e)}
    
@user.put("/user/c3/{chad_id}")
async def update_user_C3(chad_id: str, c3:int):
    try:
        result = user_collection.update_one({"chad_id": chad_id}, {"$set":{"c3":c3}}).acknowledged
        return result
    except Exception as e:
        return {"message": str(e)}
    
@user.put("/user/{chad_id}")
async def update_user(chad_id: str, user: User):
    try:
        result = user_collection.update_one({"chad_id": chad_id}, {"$set":user.dict()}).acknowledged
        return result
    except Exception as e:
        return {"message": str(e)}   

@user.get("/user")
async def get_all_users():
    result = user_collection.find()
    user_list = []
    for user in result:
        user_list.append(UserSchema(**user))
    return user_list

@user.get("/user/{chad_id}")
async def get_user(chad_id: str):
    result = user_collection.find_one({"chad_id": chad_id})
    if result:
        user = UserSchema(**result)
        return user
    else:
        return {"message": "User not found"}

@user.get("/user/wallet/{wallet_id}")
async def get_user(wallet_id: str):
    result = user_collection.find_one({"wallet_id": wallet_id})
    if result:
        user = UserSchema(**result)
        return user
    else:
        return {"message": "User not found"}

@user.get("/user/discord/{discord_id}")
async def get_user_by_discord_id(discord_id: str):
    result = user_collection.find_one({"discord_id": discord_id})
    if result:
        user = UserSchema(**result)
        return user
    else:
        return {"message": "User not found"}

@user.get("/user/twitter/{twitter_id}")
async def get_user_by_twitter_id(twitter_id: str):
    result = user_collection.find_one({"twitter_id": twitter_id})
    if result:
        user = UserSchema(**result)
        return user
    else:
        return {"message": "User not found"}


