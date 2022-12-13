from fastapi import APIRouter, Body
import database
from cryptography.fernet import Fernet
import json
from userModel import User

router = APIRouter()

User = database.user


crypt_key = Fernet.generate_key()

fernet = Fernet(crypt_key)

@router.post("/signup")
async def signup(data:str = Body(...)):
    try:
        dictObj = []
        dictObj = json.loads(data)

        encode_password = dictObj["password"].encode();

        encrypt_password = fernet.encrypt(encode_password)
        dictObj.update({"password":encrypt_password})

        dictObj : User

        findUser = User.find_one({"email":dictObj["email"]})
        if findUser is not None:
            return {"message":"Email already exist"}
        else:
            User.insert_one(dictObj)
            return {"message":"Success"}
    except Exception as e:
        print(e)
        return {"message":"Server Error"}

@router.post("/login")
async def login(data:str = Body(...)):
    try:
        dictObj = []
        dictObj = json.loads(data)
        findUser = User.find_one({"email":dictObj["email"]})
        if findUser is None:
            return {"message":"Email do not Exist"}
        else:
            decrypt_password = fernet.decrypt(findUser["password"])
            decoded_password = decrypt_password.decode()
            if decoded_password == dictObj["password"]:
                return {"message":"Success"}
            else:
                return {"message":"Enter valid Password"}
    except Exception as e:
        print(type(e))
        return {"message":"Server Error"}



