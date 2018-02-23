# Created by Max on 2/22/18
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, DateTime

Base = declarative_base()


class Toutiao(Base):
    # 表名
    __tablename__ = 'toutiao'

    id = Column(BigInteger, primary_key=True, unique=True)
    media_name = Column(String(100))
    abstract = Column(String(500))
    create_time = Column(DateTime)
    keywords = Column(String(100))
    title = Column(String(100))
    article_url = Column(String(500))
    publish_time = Column(DateTime)

    def __int__(self, **kw):
        self.id = id
        self.media_name = kw['media_name']
        self.abstract = kw['abstract']
        self.create_time = kw['create_time']
        self.keywords = kw['keywords']
        self.title = kw['title']
        self.article_url = kw['article_url']
        self.publish_time = kw['publish_time']

    def __repr__(self):
        return "<Toutiao(id='%s', title='%s')>" % (self.id, self.title)
