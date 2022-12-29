from pydantic import BaseModel

class ImageAsset(BaseModel):
    name: str
    position: str
    photo: str
