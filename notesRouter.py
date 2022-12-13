import json

from bson import ObjectId
from fastapi import APIRouter, Body
import database
from datetime import date

router = APIRouter()

Note = database.notes

@router.post("/addNote")
async def addNode(data: str = Body(...)):
    try:
        json_data = json.loads(data)

        today_date = date.today()
        today_date = str(today_date)

        dict = {"email": json_data["email"], "note": json_data["note"], "date": today_date}

        dict : Note

        Note.insert_one(dict)


        return {"message":"Success"}

    except Exception as e:
        print(e)
        return {"message":"Server Error"}

@router.delete("/deleteNote")
async def deleteNote(data: str = Body(...)):
    try:
        json_data = json.loads(data)
        Note.delete_one({"email":json_data["email"],"note":json_data["note"],"date":json_data["date"],"_id":ObjectId(json_data["_id"])});
        return {"message":"Success"}
    except Exception as e:
        print(e)
        return {"message":"Server Error"}

@router.patch("/editNote")
async def editNote(data:str = Body(...)):
    try:
        json_data = json.loads(data)
        Note.update_one({"_id":ObjectId(json_data["_id"])},{"$set":{"note":json_data["newNote"]}})
        return {"message":"Success"}
    except Exception as e:
        print(e)
        return {"message":"Server Error"}

@router.get("/getNotes/{email}")
async def getNotes(email:str):
    try:
        Notes = list(Note.find({"email":email}))
        i = 0
        for i in  range(len(Notes)):
            Notes[i]["_id"] = str(Notes[i]["_id"])
        return Notes
    except Exception as e:
        print(e)
        return {"message":"Server Error"}


@router.get("/searchNotes/{email}/{search}")
async def searchNotes(email:str,search:str):
    try:
        SearchedNotes = list()
        Notes = list(Note.find({"email":email}))
        i = 0
        print(search)
        for i in range(len(Notes)):
            Notes[i]["_id"] = str(Notes[i]["_id"])
            if search.lower() in Notes[i]["note"].lower():
                SearchedNotes.append(Notes[i])
        return SearchedNotes

    except Exception as e:
        print(e)
        return {"message": "Server Error"}


@router.get("/getNotesByDate/{email}/{date}")
async def getNotesByDate(email:str,date:str):
    try:
        Notes = list(Note.find({"email": email,"date":date}))
        i = 0
        for i in range(len(Notes)):
            Notes[i]["_id"] = str(Notes[i]["_id"])
        return Notes

    except Exception as e:
        print(e)
        return {"message": "Server Error"}

