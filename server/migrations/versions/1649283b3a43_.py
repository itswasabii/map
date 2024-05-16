"""empty message

Revision ID: 1649283b3a43
Revises: c625acb8a165
Create Date: 2024-05-18 19:13:08.880942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1649283b3a43'
down_revision = 'c625acb8a165'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_course_association')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=6), nullable=False))

    op.create_table('user_course_association',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('course_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], )
    )
    # ### end Alembic commands ###