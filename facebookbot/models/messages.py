from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base

class Message(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Message."""

    def __init__(self, id=None, mid=None, seq=None, is_echo=None, app_id=None, metadata=None, **kwargs):

        super(Message, self).__init__(**kwargs)

        self.id = id
        self.mid = mid
        self.seq = seq

class TextMessage(Message):

    def __init__(self, id=None, mid=None, seq=None, text=None, **kwargs):

        super(TextMessage, self).__init__(id=id, mid=mid, seq=seq, **kwargs)

        self.text = text

class QuickReplyMessage(Message):

    def __init__(self, id=None, mid=None, seq=None, text=None, quick_reply=None, **kwargs):

        super(QuickReplyMessage, self).__init__(id=id, mid=mid, seq=seq, text=text, quick_reply=quick_reply, **kwargs)

        self.text = text
        self.quick_reply = self.get_or_new_from_json_dict(quick_reply, QuickReply)

class AttachmentMessage(Message):
    
    def __init__(self, id=None, mid=None, seq=None, attachments=None, **kwargs):
      
        super(AttachmentMessage, self).__init__(id=id, mid=mid, seq=seq, attachments=attachments, **kwargs)
        
        for attachment in attachments:
        
            self.attachment = self.get_or_new_from_json_dict_with_types(
                attachment, {
                    'image': ImageMessage,
                    'video': VideoMessage,
                    'audio': AudioMessage,
                    'file': FileMessage,
                    'template': TemplateMessage,
                    'location': LocationMessage,
                    'fallback': FallbackMessage
                }
            )


## Payload        
class ImageMessage(Message):
    
    def __init__(self, id=None, payload=None, **kwargs):

        self.type = 'image'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
class VideoMessage(Message):

    def __init__(self, id=None, payload=None, **kwargs):
        
        self.type = 'video'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
class AudioMessage(Message):

    def __init__(self, id=None, payload=None, **kwargs):
        
        self.type = 'audio'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
class FileMessage(Message):

    def __init__(self, id=None, payload=None, **kwargs):
        
        self.type = 'file'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
        
class TemplateMessage(Message):

    def __init__(self, id=None, payload=None, **kwargs):
        
        self.type = 'template'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
class LocationMessage(Message):
    
    def __init__(self, id=None, payload=None, **kwargs):
        
        self.type = 'location'
        self.payload = self.get_or_new_from_json_dict(payload, Payload)
        
class FallbackMessage(Message):
    
    def __init__(self, id=None, title=None, url = None, payload=None, **kwargs):
        
        self.type = 'fallback'
        self.title = title
        self.url = url
        self.payload = self.get_or_new_from_json_dict(payload, Payload)            
    
class Coordinates(with_metaclass(ABCMeta, Base)):
    
    def __init__(self, lat, long, **kwargs):

        super(Coordinates, self).__init__(**kwargs)

        self.lat = lat
        self.long = long
        
class Payload(with_metaclass(ABCMeta, Base)):
    
    def __init__(self, id=None, url=None, coordinates=None, **kwargs):
        
        super(Payload, self).__init__(**kwargs)
        
        self.url = url
        self.coordinates = self.get_or_new_from_json_dict(coordinates, Coordinates)


class QuickReply(with_metaclass(ABCMeta, Base)):

    def __init__(self, payload=None, **kwargs):
        super(QuickReply, self).__init__(**kwargs)

        self.payload = payload
    
    