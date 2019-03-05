from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base

class TextQuickReply(with_metaclass(ABCMeta, Base)):

    def __init__(self, content_type=None, title=None, payload=None, image_url=None, **kwargs):

        super(TextQuickReply, self).__init__(**kwargs)

        self.content_type = "text"
        self.title = title
        self.payload = payload
        self.image_url = image_url
        
class LocationQuickReply(with_metaclass(ABCMeta, Base)):

    def __init__(self, **kwargs):

        super(LocationQuickReply, self).__init__(**kwargs)

        self.content_type = "location"
        