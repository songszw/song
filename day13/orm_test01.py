import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:315315@localhost/jet',encoding='utf-8',echo=True)

#生成orm基类
Base = declarative_base()


class User(Base):
    __tablename__ = 'songszw' #表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    age = Column(String(32))
    password = Column(String(64))

#创建表结构
Base.metadata.create_all(engine)

#创建与数据库的会话session class---注意，这是一个类，不是实例化
Session_class = sessionmaker(bind=engine)

#生成session实例
Session = Session_class()

#生成你要创建的数据对象
song_obj01 = User(name='jet',age='25',password='Song0315')
song_obj02 = User(name='szw',age='26',password='Song0325')
song_obj03 = User(name='lily',age='27',password='Song0335')

#把要创建的数据对象添加到session里面，
Session.add(song_obj01)
Session.add(song_obj02)
Session.add(song_obj03)

#统一提交，创建数据
Session.commit()












