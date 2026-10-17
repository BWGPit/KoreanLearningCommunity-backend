from pydantic import BaseModel
from enum import Enum

class Language(Enum):
    korean = "kr"
    english = "en"
    italian = "it"

class FCBox(BaseModel):
    srcLanguage: Language
    destLanguage: Language
    name: str
    mapping: tuple[list[str], list[str]]