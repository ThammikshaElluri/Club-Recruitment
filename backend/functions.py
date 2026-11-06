
from sqlalchemy import Integer, String, Column, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, Session

DB_PATH = "recruitment.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()


class Clubs(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    seats = Column(Integer)
    deadline = Column(String)
    recruiting = Column(Integer)


class Applications(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("clubs.id"))
    roll_no = Column(Integer)
    why_join = Column(String)
    status = Column(String)
    applied_on = Column(String)


Base.metadata.create_all(engine)



def get_all_clubs(category=None):
    session = Session(engine)

    if category is None:
        clubs = session.query(Clubs).all()
    else:
        clubs = session.query(Clubs).filter(
            Clubs.category == category
        ).all()

    response = []

    for club in clubs:
        application_count = session.query(Applications).filter(
            Applications.club_id == club.id,
            Applications.status != "withdrawn"
        ).count()

        temp_club = {
            "id": club.id,
            "name": club.name,
            "category": club.category,
            "seats": club.seats,
            "deadline": club.deadline,
            "recruiting": club.recruiting,
            "application_count": application_count
        }

        response.append(temp_club)

    session.close()
    return response


# E2
def get_club(id):
    session = Session(engine)

    club = session.query(Clubs).filter(Clubs.id == id).first()

    if club is None:
        session.close()
        return None

    applications = session.query(Applications).filter(
        Applications.club_id == id
    ).all()

    response = {
        "id": club.id,
        "name": club.name,
        "applications": []
    }

    for application in applications:
        response["applications"].append({
            "roll_no": application.roll_no,
            "why_join": application.why_join,
            "status": application.status
        })

    session.close()
    return response


def add_club(name, category, seats, deadline):
    session = Session(engine)

    club = Clubs(
        name=name,
        category=category,
        seats=seats,
        deadline=deadline,
        recruiting=1
    )

    session.add(club)
    session.commit()
    session.refresh(club)

    response = {
        "id": club.id,
        "name": club.name,
        "category": club.category,
        "seats": club.seats,
        "deadline": club.deadline,
        "recruiting": club.recruiting
    }

    session.close()
    return response

def set_recruiting(id, recruiting):
    session = Session(engine)

    club = session.query(Clubs).filter(Clubs.id == id).first()

    if club is None:
        session.close()
        return None

    club.recruiting = int(recruiting)
    session.commit()

    response = {
        "id": club.id,
        "name": club.name,
        "recruiting": club.recruiting
    }

    session.close()
    return response

# E5
def apply_to_club(club_id, roll_no, why_join):
    session = Session(engine)

    application = Applications(
        club_id=club_id,
        roll_no=roll_no,
        why_join=why_join,
        status="applied"
    )

    session.add(application)
    session.commit()
    session.refresh(application)

    response = {
        "id": application.id,
        "club_id": application.club_id,
        "roll_no": application.roll_no,
        "why_join": application.why_join,
        "status": application.status
    }

    session.close()
    return response


# E6
def update_application_status(id, status):
    session = Session(engine)

    application = session.query(Applications).filter(
        Applications.id == id
    ).first()

    if application is None:
        session.close()
        return None

    application.status = status
    session.commit()

    response = {
        "id": application.id,
        "club_id": application.club_id,
        "roll_no": application.roll_no,
        "status": application.status
    }

    session.close()
    return response


