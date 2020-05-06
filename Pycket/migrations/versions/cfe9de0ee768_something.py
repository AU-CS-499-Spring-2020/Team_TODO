"""something

Revision ID: cfe9de0ee768
Revises: 
Create Date: 2020-05-02 13:36:19.478178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfe9de0ee768'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=False)
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('subject', sa.String(length=140), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=35), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ticket_email'), 'ticket', ['email'], unique=False)
    op.create_index(op.f('ix_ticket_firstname'), 'ticket', ['firstname'], unique=False)
    op.create_index(op.f('ix_ticket_lastname'), 'ticket', ['lastname'], unique=False)
    op.create_index(op.f('ix_ticket_location'), 'ticket', ['location'], unique=False)
    op.create_index(op.f('ix_ticket_phone_number'), 'ticket', ['phone_number'], unique=False)
    op.create_index(op.f('ix_ticket_subject'), 'ticket', ['subject'], unique=False)
    op.create_index(op.f('ix_ticket_timestamp'), 'ticket', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ticket_timestamp'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_subject'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_phone_number'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_location'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_lastname'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_firstname'), table_name='ticket')
    op.drop_index(op.f('ix_ticket_email'), table_name='ticket')
    op.drop_table('ticket')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###