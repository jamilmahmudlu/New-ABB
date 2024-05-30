"""empty message

Revision ID: 2d3560d1fe22
Revises: 
Create Date: 2024-05-31 02:43:47.091957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d3560d1fe22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_filename', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('desc2', sa.String(length=200), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('button1_text', sa.String(length=50), nullable=True),
    sa.Column('button2_text', sa.String(length=50), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('imkan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('kart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kart_id'], ['kart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sup', sa.String(length=10), nullable=True),
    sa.Column('explanation', sa.String(length=500), nullable=True),
    sa.Column('kart_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['kart_id'], ['kart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tarif',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('column1', sa.String(length=200), nullable=True),
    sa.Column('column2', sa.String(length=500), nullable=True),
    sa.Column('kart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kart_id'], ['kart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarif')
    op.drop_table('sans')
    op.drop_table('imkan')
    op.drop_table('user')
    op.drop_table('kart')
    # ### end Alembic commands ###
