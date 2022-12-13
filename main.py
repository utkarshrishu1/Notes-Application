#Notes App

import notesRouter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import userRoute

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRoute.router)
app.include_router(notesRouter.router)
