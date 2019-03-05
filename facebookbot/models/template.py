from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

# from .actions import get_action
from .base import Base
from .send_messages import SendMessage, TextQuickReply, LocationQuickReply
from .actions import get_action, get_actions


class TemplateSendMessage(SendMessage):
    
    def __init__(self, id=None, text=None, template = None, quick_replies=None, **kwargs):
    
        super(TemplateSendMessage, self).__init__(id=id,  **kwargs)
        
        payload = TemplatePayload(template=template)

        self.attachment = self.get_or_new_from_json_dict(payload, TemplatePayload)
        
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

class TemplatePayload(SendMessage):
    
    def __init__(self, id=None, template=None, **kwargs):
        
        self.type = "template"
        self.payload = template
        
        
class Template(with_metaclass(ABCMeta, Base)):

    def __init__(self, **kwargs):

        super(Template, self).__init__(**kwargs)

        self.template_type = None        
        
class ButtonsTemplate(Template):
    
    def __init__(self, template_type=None, text=None, buttons=None, **kwargs):

        self.template_type = "button"
        self.text = text
        self.buttons = get_actions(buttons)
        
class GenericTemplate(Template):
    
    def __init__(self, template_type=None, elements=None, **kwargs):
        
        self.template_type = "generic"
        
        print(elements)
        
        new_elements = []
        if elements:
            for element in elements:
                new_elements.append(self.get_or_new_from_json_dict(
                    element, Element
                ))                
        
        self.elements = new_elements
        
class Element(Base):
    
    def __init__(self, title=None, image_url=None, subtitle=None, default_action=None, buttons=None, **kwargs):
        
        self.title = title
        self.image_url = image_url
        self.subtitle = subtitle
        self.default_action = get_action(default_action)
        self.buttons = get_actions(buttons)
        
        
        
        
        