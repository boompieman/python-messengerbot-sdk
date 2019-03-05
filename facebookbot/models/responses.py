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
