import sqlalchemy
from datetime import datetime
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
from sqlalchemy.orm import orm


class Lote(ModelBase):
    __tablename__: str = "lotes"

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
    id_tipo_picole: int = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("tipos_picole.id"),  # tabela.campo
    )
    tipo_picole: TipoPicole = orm.relationship(
        "TipoPicole",
        lazy="joined",
    )  # configuração interna do orm sqlalchemy
    quantidade: int = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Lote: {self.nome}>"