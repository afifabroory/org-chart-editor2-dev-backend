from fastapi import APIRouter, Response
from models.response import ImageAsset

endpoint = APIRouter(prefix="/api")

@endpoint.get('/image/assets', response_model=dict[str, list[ImageAsset]])
async def get_image_assets(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"

    return {
        "High-Res": [
            {
                "name": "NAME_1",
                "position": "POSITION_1",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_2",
                "position": "POSITION_2",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_3",
                "position": "POSITION_3",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_4",
                "position": "POSITION_4",
                "photo": "/path/to/files"
            }
        ], "Low-Res": [
            {
                "name": "NAME_1",
                "position": "POSITION_1",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_2",
                "position": "POSITION_2",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_3",
                "position": "POSITION_3",
                "photo": "/path/to/files"
            },
            {
                "name": "NAME_4",
                "position": "POSITION_4",
                "photo": "/path/to/files"
            }
        ]
    }