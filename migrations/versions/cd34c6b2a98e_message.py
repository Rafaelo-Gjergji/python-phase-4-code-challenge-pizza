"""message

Revision ID: cd34c6b2a98e
Revises: 1d89a41ff886
Create Date: 2024-04-16 00:57:01.029218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd34c6b2a98e'
down_revision = '1d89a41ff886'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ingredients', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_pizzas_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizza_table.id'], name=op.f('fk_restaurant_pizzas_table_pizza_id_pizza_table')),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant_table.id'], name=op.f('fk_restaurant_pizzas_table_restaurant_id_restaurant_table')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('restaurants')
    op.drop_table('pizzas')
    op.drop_table('restaurant_pizzas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_pizzas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pizzas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('ingredients', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('restaurant_pizzas_table')
    op.drop_table('restaurant_table')
    op.drop_table('pizza_table')
    # ### end Alembic commands ###
