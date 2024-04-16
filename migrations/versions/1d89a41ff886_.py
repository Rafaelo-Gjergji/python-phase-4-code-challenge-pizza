"""empty message

Revision ID: 1d89a41ff886
Revises: 84f014b38fca
Create Date: 2024-04-16 00:48:51.026330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d89a41ff886'
down_revision = '84f014b38fca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint('fk_restaurant_pizzas_pizza_id_pizzas', type_='foreignkey')
        batch_op.drop_constraint('fk_restaurant_pizzas_restaurant_id_restaurants', type_='foreignkey')
        batch_op.drop_column('restaurant_id')
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('restaurant_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_restaurant_pizzas_restaurant_id_restaurants', 'restaurants', ['restaurant_id'], ['id'])
        batch_op.create_foreign_key('fk_restaurant_pizzas_pizza_id_pizzas', 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###
