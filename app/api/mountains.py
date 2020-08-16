from typing import List
from fastapi import Header, APIRouter

from app.api.models import Mountain

mountains_db = [
    {
        'name': 'Mount Adams',
        'elevation': '1,766 meters',
        'coordinate': '44°19′14″N 71°17′29W',
        'links': ['https://en.wikipedia.org/wiki/Mount_Adams_(New_Hampshire)', 'http://www.mountwashington.org/visitor/mountains/mountains.html']
    }
]

mountains = APIRouter()

@mountains.get('/', response_model=List[Mountain])
async def index():
    return mountains_db

@mountains.post('/', status_code=201)
async def add_mountain(payload: Mountain):
    mountain = payload.dict()
    mountains_db.append(mountain)
    return {'id': len(mountain_db) - 1}

@mountains.put('/{id}')
async def update_mountain(id: int, payload: Mountain):
    mountain = payload.dict()
    mountains_length = len(mountains_db)
    if 0 <= id <= mountains_length:
        mountains_db[id] = mountain
        return None
    raise HTTPException(status_code=404, detail="Mountain with given id not found")

@mountains.delete('/{id}')
async def delete_mountain(id: int):
    mountains_length = len(mountains_db)
    if 0 <= id <= mountains_length:
        del mountains_db[id]
        return None
    raise HTTPException(status_code=404, detail="Mountain with given id not found")
