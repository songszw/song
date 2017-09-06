import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine(
    'mysql+pymysql://root:315315@localhost/song',
    encoding='utf-8'
)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)


    def __repr__(self):
        return '<%s name %s>'%(self.id,self.name)

class StudyRecord(Base):
    __tablename__='study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))

    student = relationship('Student',backref = 'my_study_record')
    def __repr__(self):
        return '<%s day %s>'%(self.student.name,self.day)

Base.metadata.create_all(engine)

Session_class =sessionmaker(bind=engine)
session = Session_class()

# s1 = Student(name='song',register_date='2011-1-1')
# s2 = Student(name='lily',register_date='2012-6-11')
# s3 = Student(name='anna',register_date='2013-2-5')
# s4 = Student(name='maya',register_date='2014-5-21')
# s5 = Student(name='alisa',register_date='2051-11-5')
# s6 = Student(name='jane',register_date='2016-12-9')

# stuobj1 = StudyRecord(day=1,status='YES',stu_id=1)
# stuobj2 = StudyRecord(day=2,status='NO',stu_id=1)
# stuobj3 = StudyRecord(day=3,status='YES',stu_id=1)
# stuobj4 = StudyRecord(day=1,status='YES',stu_id=2)
# stuobj5 = StudyRecord(day=2,status='yes',stu_id=3)
# stuobj6 = StudyRecord(day=3,status='no',stu_id=2)
#
# session.add_all([stuobj1,stuobj2,stuobj3,stuobj4,stuobj5,stuobj6])
# session.add_all([s1,s2,s3,s4,s5,s6])

stu_obj = session.query(Student).filter(Student.name=='song').first()
print(stu_obj.my_study_record)
session.commit()