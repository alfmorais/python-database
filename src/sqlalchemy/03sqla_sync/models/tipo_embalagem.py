import sqlalchemy
from datetime import datetime
from models.model_base import ModelBase


class Sabor(ModelBase):
    __tablename__: str = "tipos_embalagem"

    id: int = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        primary_key=True,
        autoincrement=True
    )
    data_criacao: datetime = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.now,
        index=True,
    )
    nome: str = sqlalchemy.Column(
        sqlalchemy.String,
        unique=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Tipo Embalagem: {self.nome}>"