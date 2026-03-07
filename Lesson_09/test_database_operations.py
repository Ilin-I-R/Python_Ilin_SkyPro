import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:121@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)


class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String)
    group_id = Column(Integer)


@pytest.fixture
def db_session():
    session = SessionLocal()
    yield session
    session.close()


class TestDBOperations:
    def test_add_student(self, db_session):
        new_student = Student(
            user_id=90001,
            level="Beginner",
            education_form="group",
            subject_id=1
        )
        db_session.add(new_student)
        db_session.commit()
        result = db_session.query(Student).filter_by(
            user_id=90001
        ).first()
        assert result is not None
        assert result.level == "Beginner"
        db_session.query(Student).filter_by(user_id=90001).delete()
        db_session.commit()

    def test_get_student(self, db_session):
        student = Student(
            user_id=90002,
            level="Intermediate",
            education_form="individual",
            subject_id=2
        )
        db_session.add(student)
        db_session.commit()
        found_student = db_session.query(Student).filter_by(
            user_id=90002
        ).first()
        assert found_student.education_form == "individual"
        db_session.query(Student).filter_by(user_id=90002).delete()
        db_session.commit()

    def test_update_student(self, db_session):
        student = Student(
            user_id=90003,
            level="Beginner",
            education_form="group",
            subject_id=1
        )
        db_session.add(student)
        db_session.commit()
        student.level = "Advanced"
        db_session.commit()
        updated_student = db_session.query(Student).filter_by(
            user_id=90003
        ).first()
        assert updated_student.level == "Advanced"
        db_session.query(Student).filter_by(user_id=90003).delete()
        db_session.commit()

    def test_delete_student(self, db_session):
        student = Student(
            user_id=90004,
            level="Beginner",
            education_form="group",
            subject_id=1
        )
        db_session.add(student)
        db_session.commit()
        db_session.query(Student).filter_by(user_id=90004).delete()
        db_session.commit()
        result = db_session.query(Student).filter_by(
            user_id=90004
        ).first()
        assert result is None

    def test_add_subject(self, db_session):
        subject = Subject(subject_id=901, subject_title="Math Test")
        db_session.add(subject)
        db_session.commit()
        result = db_session.query(Subject).filter_by(
            subject_id=901
        ).first()
        assert result.subject_title == "Math Test"
        db_session.query(Subject).filter_by(subject_id=901).delete()
        db_session.commit()

    def test_add_teacher(self, db_session):
        teacher = Teacher(
            teacher_id=1001,
            email="teacher@example.com",
            group_id=101
        )
        db_session.add(teacher)
        db_session.commit()
        result = db_session.query(Teacher).filter_by(
            teacher_id=1001
        ).first()
        assert result.email == "teacher@example.com"
        assert result.group_id == 101
        db_session.query(Teacher).filter_by(teacher_id=1001).delete()
        db_session.commit()
