import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:315315@localhost/jet',encoding = 'utf-8')

Base = declarative_base()

class User(Base):
    __tablename__='ai'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<%s name %s, ped %s>'%(self.id,self.name,self.password)


Base.metadata.create_all(engine)

Session_class = sessionmaker(bind = engine)
Session = Session_class()
# user_obj1 = User(name = 'jet',password = '315315')
# user_obj2 = User(name = 'lily',password = '325325')
# user_obj3 = User(name = 'song',password = '335335')

# Session.add(user_obj1)
# Session.add(user_obj2)
# Session.add(user_obj3)

# data = Session.query(User).filter_by(id=1).first()
# data.name = 'szw'
# data.password = '123456'
Session.query(User).filter(User.name.like('Ra%')).count()
from sqlalchemy import func
print(Session.query(func.count(User.name),User.name).group_by(User.name).all())
Session.commit()






