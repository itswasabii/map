"""empty message

<<<<<<<< HEAD:server/migrations/versions/9e2118668d83_.py
Revision ID: 9e2118668d83
Revises: 
Create Date: 2024-05-18 23:18:30.607815
========
Revision ID: c625acb8a165
Revises: 
Create Date: 2024-05-18 18:35:13.342277
>>>>>>>> 7544fdc9 (feat: add username to posts and course to user):server/migrations/versions/c625acb8a165_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:server/migrations/versions/9e2118668d83_.py
revision = '9e2118668d83'
========
revision = 'c625acb8a165'
>>>>>>>> 7544fdc9 (feat: add username to posts and course to user):server/migrations/versions/c625acb8a165_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('course_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
<<<<<<<< HEAD:server/migrations/versions/9e2118668d83_.py
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('occupation', sa.String(length=50), nullable=True),
    sa.Column('qualification', sa.Text(), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
========
    sa.Column('role', sa.Enum('admin', 'normal'), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
>>>>>>>> 7544fdc9 (feat: add username to posts and course to user):server/migrations/versions/c625acb8a165_.py
    sa.Column('joined_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cohort',
    sa.Column('cohort_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cohort_name', sa.String(length=255), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.Enum('PUBLIC', 'PRIVATE', name='cohorttype'), nullable=False),
    sa.Column('year_of_enrollment', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('cohort_id')
    )
    op.create_table('fundraiser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('goal_amount', sa.Float(), nullable=False),
    sa.Column('current_amount', sa.Float(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('success_story',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tech_news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_course_association',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.course_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], )
    )
    op.create_table('cohort_member',
    sa.Column('member_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cohort_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('joined_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohort.cohort_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('member_id')
    )
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fundraiser_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('donation_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['fundraiser_id'], ['fundraiser.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cohort_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.Enum('SUCCESS_STORY', 'TECH_NEWS', 'GENERAL_DISCUSSION', name='postcategory'), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohort.cohort_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('comment',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cohort_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cohort_id'], ['cohort.cohort_id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('donation')
    op.drop_table('cohort_member')
    op.drop_table('user_course_association')
    op.drop_table('tech_news')
    op.drop_table('success_story')
    op.drop_table('fundraiser')
    op.drop_table('cohort')
    op.drop_table('user')
    op.drop_table('course')
    # ### end Alembic commands ###
