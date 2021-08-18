#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """
    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Method to add a new user"""
        session = self._session
        newUser = User()
        newUser.email = email
        newUser.hashed_password = hashed_password
        session.add(newUser)
        session.commit()

        return newUser

    def find_user_by(self, **kwargs) -> User:
        """Method to find a user"""
        try:
            instance = self._session.query(User).filter_by(**kwargs)[0]
            return instance
        except InvalidRequestError:
            raise InvalidRequestError
        except IndexError:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """Method to update a user"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if key not in user.__dict__:
                raise ValueError
            else:
                user.key = value

        self._session.commit()
