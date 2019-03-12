from __future__ import unicode_literals

from .base import Base

class Profile(Base):

    def __init__(self, id=None, first_name=None, last_name=None, gender=None,
                 profile_pic=None, locale=None, timezone=None, **kwargs):

        super(Profile, self).__init__(**kwargs)
        
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.profile_pic = profile_pic
        self.locale = locale
        self.timezone = timezone

class Content(object):
    
    def __init__(self, response):

        self.response = response

    @property
    def content_type(self):

        return self.response.headers.get('content-type')

    @property
    def content(self):

        return self.response.content

    def iter_content(self, chunk_size=1024):

        return self.response.iter_content(chunk_size=chunk_size)        