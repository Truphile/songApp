import hashlib

from sqlalchemy.exc import IntegrityError

from models.user import User


def hash_password(password: str):
    return hashlib.sha512(password.encode()).hexdigest()

def verify_password(password: str, hashed_password: str):
    return hashed_password == hashlib.sha512(password.encode()).hexdigest()

def register_user(database, user_data):

    try:
        new_user = User(
        password = hash_password(user_data.password),
        email = user_data.email,
        role = "user"
        )

        database.add(new_user)
        database.commit()
        database.refresh(new_user)

        return new_user

    except IntegrityError:
        database.rollback()
        return None
