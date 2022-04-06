from typing import List
import sqlalchemy
from datetime import datetime
from models.model_base import ModelBase
from sqlalchemy.orm import orm
from models.revendedor import Revendedor
from models.lote import Lote


# Nota Fiscal pode ter vários lotes
lotes_nota_fiscal = sqlalchemy.Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    sqlalchemy.Column(
        "id_nota_fiscal",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("notas_fiscais.id"),
    ),
    sqlalchemy.Column(
        "id_lote",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("lotes.id"),
    ),
)

class NotaFiscal(ModelBase):
    __tablename__: str = "notas_fiscais"

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
    valor: float = sqlalchemy.Column(
        sqlalchemy.DECIMAL(8,2),
        nullable=False,
    )
    numero_serie: str = sqlalchemy.Column(
        sqlalchemy.String(45),
        unique=True,
        nullable=False,
    )
    descricao: str = sqlalchemy.Column(
        sqlalchemy.String(200),
        nullable=False,
    )
    id_revendedor: int = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("revendedores.id")
    )
    revendedor: Revendedor = orm.relationship(
        "Revendedor",
        lazy="joined",
    )
    # uma nota fiscal pode ter vários lotes e uma lote sempre estará atrelado a nf
    lotes: List[Lote] = orm.relationship(
        "Lote",
        secondary=lotes_nota_fiscal,
        backref="lote",
        lazy="dynamic",
    )

    def __repr__(self) -> str:
        return f"<Nota Fiscal: {self.numero_serie}>"