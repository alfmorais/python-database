import sqlalchemy
from datetime import datetime
from models.model_base import ModelBase


class Revendedor(ModelBase):
    __tablename__: str = "revendedores"

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
        sqlalchemy.String(45),
        unique=True,
        nullable=False,
    )
    razao_social: str = sqlalchemy.Column(
        sqlalchemy.String(100),
        nullable=False,
    )
    contato: str = sqlalchemy.Column(
        sqlalchemy.String(100),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Revendedor: {self.nome}>"