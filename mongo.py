from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os
from klc_types import Language, FCBox

# NOTE: Environment variables must be uploaded to the /environment-variables section of Fastapi Cloud
load_dotenv()

URI = os.getenv("CONNECTION")

def test():
    return "This is a test, " + os.getenv("TEST")

class DBClient:
    def __init__(self):
        self.client = AsyncMongoClient(URI)
        self.db = self.client[os.getenv("DATABASE")]
        self.main_collection = self.db[os.getenv("MAIN_COLLECTION")]

    async def get_latest(self, limit: int = 1) -> FCBox:
        """Gets n latest boxes | TODO: GET ACTUALLY THE LATEST AND NOT ONE AT RANDOM WITH A PIPELINE"""
        res: dict = await self.main_collection.find_one({}, {"_id": 0})
        return FCBox(**res)