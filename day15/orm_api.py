
from day15 import many_orm
from sqlalchemy.orm import sessionmaker
Session_class = sessionmaker(bind=many_orm.engine)
session = Session_class()

b1 = many_orm.Book(
    name = 'how to learn python',
    pub_date = '2011-1-1'
)
b2 = many_orm.Book(
    name = 'learn python song',
    pub_date = '2012-2-2'
)
b3 = many_orm.Book(
    name = 'what the fuck',
    pub_date = '2013-3-3'
)

a1 = many_orm.Author(name = 'song')
a2 = many_orm.Author(name = 'lily')
a3 = many_orm.Author(name = 'jet')

b1.authors = [a1,a3]
b2.authors = [a3]
b3.authors = [a1,a2,a3]

session.add_all([b1,b2,b3,a1,a2,a3])
session.commit()