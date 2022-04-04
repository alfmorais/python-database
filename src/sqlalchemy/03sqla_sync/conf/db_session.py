import sqlalchemy
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models.model_base import ModelBase


__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    """This function will create the engine for our database

    Args:
        sqlite (bool, optional): if sqlite = True,
        means the user want to use SQLite as default. Defaults to False.
    """
    global __engine

    if __engine:
        return

    if sqlite:
        file_db = 'db/picoles.sqlite'
        folder = Path(file_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{file_db}'
        __engine = sqlalchemy.create_engine(
            url=conn_str, echo=False, connect_args={'check_same_thread': False}
        )
    else:
        # Essa conn_str pode colocar em arquivo .env para não ocorrer ataques
        # admin é usuario do banco, 1234 é a senha
        # o número 5432 é a porta do banco de dados
        conn_str = 'postgresql://admin:1234@localhost:5432/picoles'
        __engine = sqlalchemy.create_engine(url=conn_str, echo=False)
    return __engine


def create_session() -> Session:
    """This function will create a session in our database

    Returns:
        Session: database session
    """
    global __engine

    if not __engine:
        # Caso for usar o SQLite como padrão, chamar a função dessa forma:
        # create_engine(sqlite=True)
        # Do jeto que está, estamos usando o postgresql como padrão.
        create_engine()

    __session = sessionmaker(
        __engine,
        expire_on_commit=False,
        class_=Session,
    )

    session: Session = __session()

    return session


def create_tables() -> None:
    global __engine

    if not __engine:
        # Caso for usar o SQLite como padrão, chamar a função dessa forma:
        # create_engine(sqlite=True)
        # Do jeto que está, estamos usando o postgresql como padrão.
        create_engine()

    import models.__all_models

    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
