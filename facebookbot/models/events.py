from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base
from .messages import (
    TextMessage,
    AttachmentMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    FileMessage,
    QuickReplyMessage
)

from .quick_reply import (
    TextQuickReply
)

from .obj import Obj

# from .sources import SourceUser, SourceGroup, SourceRoom

class Event(with_metaclass(ABCMeta, Base)):

    def __init__(self, timestamp=None, sender=None, recipient=None, **kwargs):

        super(Event, self).__init__(**kwargs)

        self.sender = self.get_or_new_from_json_dict(sender, Obj)
        self.recipient = self.get_or_new_from_json_dict(recipient, Obj)
        self.timestamp = timestamp
        
class TextMessageEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, message=None, **kwargs):

        super(TextMessageEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.message = self.get_or_new_from_json_dict(message, TextMessage)

        
class AttachmentMessageEvent(Event):    

    def __init__(self, timestamp=None, sender=None, recipient=None, message=None, **kwargs):

        super(AttachmentMessageEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.message = self.get_or_new_from_json_dict(message, AttachmentMessage)

class QuickReplyMessageEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, message=None, **kwargs):

        super(QuickReplyMessageEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.message = self.get_or_new_from_json_dict(message, QuickReplyMessage)

    
class PostbackEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, postback=None, **kwargs):

        super(PostbackEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.postback = self.get_or_new_from_json_dict(
            postback, Postback
        )
        
class TextEchoMessageEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, message=None, **kwargs):

        super(TextEchoMessageEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )
        
        self.message = self.get_or_new_from_json_dict(message, TextMessage)  
        
class AttachmentEchoMessageEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, message=None, **kwargs):

        super(AttachmentEchoMessageEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )
        
        self.message = self.get_or_new_from_json_dict(message, AttachmentMessage)        
        
class LinkingEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, account_linking=None, **kwargs):

        super(LinkingEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.account_linking = self.get_or_new_from_json_dict(
            account_linking, AccountLinking
        )
        
class UnLinkingEvent(Event):

    def __init__(self, timestamp=None, sender=None, recipient=None, account_linking=None, **kwargs):

        super(UnLinkingEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.account_linking = self.get_or_new_from_json_dict(
            account_linking, AccountLinking
        )
        
class GetStartedEvent(Event):
    
    def __init__(self, timestamp=None, sender=None, recipient=None, postback=None, **kwargs):
        
        super(GetStartedEvent, self).__init__(
            timestamp=timestamp, sender=sender, recipient=recipient, **kwargs
        )

        self.postback = self.get_or_new_from_json_dict(
            postback, Postback
        )
        
class Postback(Base):

    def __init__(self, title=None, payload=None, referral=None, **kwargs):

        super(Postback, self).__init__(**kwargs)

        self.title = title
        self.payload = payload
        self.referral = self.get_or_new_from_json_dict(
            referral, Referral
        )

class Referral(Base):
    
    def __init__(self, ref=None, source=None, type=None, ad_id=None, referer_uri=None, **kwargs):
        
        self.ref = ref
        self.source = source
        self.type = type
        self.ad_id = ad_id
        self.referer_uri = referer_uri

class AccountLinking(Base):
    
    def __init__(self, status=None, authorization_code=None, **kwargs):

        super(Linking, self).__init__(**kwargs)

        self.status = status
        self.authorization_code = authorization_code    
                    
    