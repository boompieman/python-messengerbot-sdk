# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

# from .actions import get_action
from .base import Base 


class SendMessage(with_metaclass(ABCMeta, Base)):

    def __init__(self, id=None, **kwargs):

        super(SendMessage, self).__init__(**kwargs)
        self.id = id


class TextSendMessage(SendMessage):

    def __init__(self, id=None, text=None, quick_replies=None, **kwargs):

        super(TextSendMessage, self).__init__(id=id, **kwargs)

        self.text = text
        
        new_quick_replies = []
        
        if quick_replies:
            for quick_reply in quick_replies:  
                
                new_quick_replies.append(
                    self.get_or_new_from_json_dict_with_types(
                        quick_reply, {
                            'text': TextQuickReply,
                            'location': LocationQuickReply
                        },
                        type_key = 'content_type'
                    )
                )
                
            self.quick_replies = new_quick_replies        
        
class ImageSendMessage(SendMessage):

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):

        super(ImageSendMessage, self).__init__(id=id, **kwargs)
        
        payload = ImagePayload(url=url, is_reusable=is_reusable)
        
        self.attachment = self.get_or_new_from_json_dict(payload, ImagePayload)

class VideoSendMessage(SendMessage):

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):

        super(VideoSendMessage, self).__init__(id=id, **kwargs)
        
        payload = VideoPayload(url=url, is_reusable=is_reusable)
        
        self.attachment = self.get_or_new_from_json_dict(payload, VideoPayload)
        
class AudioSendMessage(SendMessage):

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):

        super(AudioSendMessage, self).__init__(id=id, **kwargs)
        
        payload = AudioPayload(url=url, is_reusable=is_reusable)
        
        self.attachment = self.get_or_new_from_json_dict(payload, AudioPayload)
        
class FileSendMessage(SendMessage):

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):

        super(FileSendMessage, self).__init__(id=id, **kwargs)
        
        payload = FilePayload(url=url, is_reusable=is_reusable)
        
        self.attachment = self.get_or_new_from_json_dict(payload, FilePayload)        
        
## Payload        
class ImagePayload(SendMessage):
    
    def __init__(self, id=None, url=None, is_reusable=None, **kwargs):

        self.type = 'image'
        self.payload = Payload(url=url, is_reusable=is_reusable)          
        
class VideoPayload():

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):
        
        self.type = 'video'
        self.payload = Payload(url=url, is_reusable=is_reusable)
        
class AudioPayload():

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):
        
        self.type = 'audio'
        self.payload = Payload(url=url, is_reusable=is_reusable)
        
class FilePayload():

    def __init__(self, id=None, url=None, is_reusable=True, **kwargs):
        
        self.type = 'file'
        self.payload = Payload(url=url, is_reusable=is_reusable)
        
class Payload(SendMessage):
    
    def __init__(self, id=None, url=None, is_reusable=None, **kwargs):
        
        self.url = url
        self.is_reusable = is_reusable       

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
        
    
            
        