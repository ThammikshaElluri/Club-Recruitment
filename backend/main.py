from http.client import HTTPException

from fastapi import FastAPI
from datetime import datetime
import functions

app = FastAPI()




@app.get("/clubs")
def clubs(category=None):
    return functions.get_all_clubs(category=category)

@app.get("/clubs/{club_id}")
def club(club_id: int):
    response = functions.get_club(club_id)

    if response is None:
        raise HTTPException(status_code=404, detail="Club not found")

    return response

@app.post("/clubs")
def add_club(name, category, seats: int, deadline):
    if not name or not category or not deadline:
        raise HTTPException(status_code=422, detail="All fields are required")

    if category not in ["technical", "cultural", "sports", "social", "literary"]:
        raise HTTPException(status_code=422, detail="Invalid category")

    if seats < 1 or seats > 30:
        raise HTTPException(status_code=422, detail="Seats must be between 1 and 30")
    
    try:
        dt = datetime.strptime(deadline,"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        
    except ValueError as v:
        raise HTTPException(status_code=422, detail="Invalid DateTime Format")

    return functions.add_club(name, category, seats, deadline)


@app.patch("/clubs/{club_id}/recruitment")
def recruitment(club_id: int, recruiting: int):
    response = functions.set_recruiting(club_id, recruiting)

    if response is None:
        raise HTTPException(status_code=404, detail="Club not found")

    return response

@app.post("/clubs/{club_id}/applications")
def apply(club_id: int, roll_no: int, why_join: str):
    if len(why_join) < 20:
        raise HTTPException(status_code=422, detail="Reason must be at least 20 characters")

    return functions.apply_to_club(club_id, roll_no, why_join)

@app.patch("/applications/{application_id}/status")
def update_status(application_id: int, status: str):
    response = functions.update_application_status(application_id, status)

    if response is None:
        raise HTTPException(status_code=404, detail="Application not found")

    if response == "move_not_allowed":
        raise HTTPException(status_code=400, detail="This status move is not allowed")

    if response == "seats_full":
        raise HTTPException(status_code=400, detail="Club seats are full")

    return response
