from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mongo
from klc_types import FCBox


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)
dbclient = mongo.DBClient()

@app.get("/")
async def root():
    return {"message": "행복하게 한국어를 배우는중"}

@app.get("/getbox")
async def getbox():
    """Get the latest box"""
    res: FCBox = await dbclient.get_latest()
    return res.model_dump(mode="json")