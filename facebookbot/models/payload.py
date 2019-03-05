from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base

## Payload  
class ImagePayload(Message):
    
    def __init__(self, id=None, image_url=None, is_reusable=None, **kwargs):

        self.type = 'image'
        self.payload = Payload(url=image_url, is_reusable=is_reusable)          
        
class VideoPayload(Message):

    def __init__(self, id=None, video_url=None, is_reusable=True, **kwargs):
        
        self.type = 'video'
        self.payload = Payload(url=video_url, is_reusable=is_reusable)
        
class AudioPayload(Message):

    def __init__(self, id=None, audio_url=None, is_reusable=True, **kwargs):
        
        self.type = 'audio'
        self.payload = Payload(url=audio_url, is_reusable=is_reusable)
        
class FilePayload(Message):

    def __init__(self, id=None, file_url=None, is_reusable=True, **kwargs):
        
        self.type = 'file'
        self.payload = Payload(url=file_url, is_reusable=is_reusable)
        
class Payload(Message):
    
    def __init__(self, id=None, url=None, is_reusable=None, **kwargs):
        
        self.url = url
        self.is_reusable = is_reusable      