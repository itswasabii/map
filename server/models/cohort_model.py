from . import  db
from datetime import datetime
from enum import Enum

class CohortType(Enum):
    PUBLIC = "public"
    PRIVATE = "private"


# # Example of creating a public cohort
# public_cohort = Cohort.create_cohort(
#     name="Public Cohort",
#     created_by=user_id,
#     description="Description of public cohort",
#     type=CohortType.PUBLIC,
#     course_id=course_id
# )

# # Example of creating a private cohort
# private_cohort = Cohort.create_cohort(
#     name="Private Cohort",
#     created_by=user_id,
#     description="Description of private cohort",
#     type=CohortType.PRIVATE,
#     year_of_enrollment=year_of_enrollment,
#     course_id=course_id
# )

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

class Cohort(db.Model):
    cohort_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cohort_name = db.Column(db.String(255), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.Enum(CohortType), nullable=False)
    year_of_enrollment = db.Column(db.Integer, nullable=True) 
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=True)

    members = db.relationship('CohortMember', backref='cohort', lazy='dynamic')
    posts = db.relationship('Post', backref='cohort', lazy='dynamic')
    # fundraisers = db.relationship('Fundraiser', backref='cohort', lazy='dynamic')

class CohortMember(db.Model):
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohort.cohort_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    joined_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
