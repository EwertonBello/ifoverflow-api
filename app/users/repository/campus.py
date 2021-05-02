from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.users.models import Campus


def get_all(db: Session):
    campus_list = db.query(Campus).all()
    return campus_list

def show(id: int, db: Session):
    campus = db.query(Campus).filter(Campus.id == id).first()
    if not campus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Campus with the id {id} is not available")
    return campus

def users_by_campus(id: int, db: Session):
	campus = db.query(Campus).filter(Campus.id == id).first()
	if not campus:
	    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
	                        detail=f"Campus with the id {id} is not available")
	return campus
