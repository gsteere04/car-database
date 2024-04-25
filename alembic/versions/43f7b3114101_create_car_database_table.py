"""create car_database table

Revision ID: 43f7b3114101
Revises: 
Create Date: 2024-04-25 11:01:48.954785

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43f7b3114101'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("cars", 
                   sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                   sa.Column("vin", sa.Text),
                   sa.Column("model", sa.Text),
                   sa.Column("make", sa.Text),
                   sa.Column("engine", sa.Text),
                   sa.Column("year", sa.Integer))  
    
    op.create_table("dealerships", 
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("name", sa.Text),
                    sa.Column("address", sa.Text),
                    sa.Column("phone_number", sa.Text))
   
    op.create_table("inventory", 
                    sa.Column("car_id", sa.Integer, sa.ForeignKey("cars.id"), primary_key=True),
                    sa.Column("dealer_id", sa.Integer, sa.ForeignKey("dealerships.id"), primary_key=True),
                    sa.Column("cost", sa.Float),
                    sa.Column("is_sold", sa.Boolean))


def downgrade() -> None:
    op.drop_table("inventory")

    op.drop_table("dealerships")

    op.drop_table("cars")
