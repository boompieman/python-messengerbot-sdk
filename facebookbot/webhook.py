from .models.events import (
    TextMessageEvent,
    AttachmentMessageEvent,
    LinkingEvent,
    UnLinkingEvent,
    GetStartedEvent,
    QuickReplyMessageEvent,
#     JoinEvent,
#     LeaveEvent,
    TextEchoMessageEvent,
    AttachmentEchoMessageEvent,
    PostbackEvent,
#     BeaconEvent,
#     AccountLinkEvent,
)

import inspect

from .utils import LOGGER, PY3, safe_compare_digest

class WebhookParser(object):
    """Webhook Parser."""

    def __init__(self):
        pass

    def parse(self, body_json):
        
        events = []

        print(body_json)
        
        if body_json["object"] == "page":
            for entry in body_json["entry"]:
                for event in entry["messaging"]:
                    
                    if event.get("message") and event["message"].get("text"):  # someone sent us a message
                        
                        if event["message"].get("app_id"):
                            
                            events.append(TextEchoMessageEvent.new_from_json_dict(event))

                        elif event["message"].get("quick_reply"):

                            events.append(QuickReplyMessageEvent.new_from_json_dict(event))
                            
                        else:
                            
                            events.append(TextMessageEvent.new_from_json_dict(event))
                
                    elif event.get("message") and event["message"].get("attachments"):
            
                        if event["message"].get("app_id"):
                    
                            events.append(AttachmentEchoMessageEvent.new_from_json_dict(event))
                    
                        else:
                        
                            events.append(AttachmentMessageEvent.new_from_json_dict(event))
            
                    elif event.get("delivery"):  # delivery confirmation
                        pass
                    
                    elif event.get("read"):  # read confirmation
                        pass
                    
                
                    elif event.get("optin"):  # optin confirmation
                        pass

                    elif event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                        
                        if event["postback"]["payload"] == "get_started":
                            events.append(GetStartedEvent.new_from_json_dict(event))
                        
                        else:
                            events.append(PostbackEvent.new_from_json_dict(event))
                            
                    elif event.get("referral"):  # optin confirmation
                        pass                            
                        
                    elif event.get("account_linking"):
                        if event["account_linking"]["status"] == "linked":
                            
                            events.append(LinkingEvent.new_from_json_dict(event))
                            
                        elif event["account_linking"]["status"] == "unlinked":
                            
                            events.append(UnLinkingEvent.new_from_json_dict(event))
                    else:
                        print('Webhook received unknown event: ', event)
                    
        return events
                    
class WebhookHandler(object):
    """Webhook Handler."""

    def __init__(self):

        self.parser = WebhookParser()
        self._handlers = {}
        self._default = None
        
    def handle(self, body_json):
        """Handle webhook.
        :param str body: Webhook request body (as text)
        """
        events = self.parser.parse(body_json)

        for event in events:
            func = None
            key = None


#             if isinstance(event, TextMessageEvent):
#                 key = self.__get_handler_key(
#                     event.__class__, event.message.__class__)
#                 func = self._handlers.get(key, None)
                
            if isinstance(event, AttachmentMessageEvent):
                key = self.__get_handler_key(
                    event.__class__, event.message.attachment.__class__)
                func = self._handlers.get(key, None)
                

            if func is None:
                key = self.__get_handler_key(event.__class__)
                func = self._handlers.get(key, None)
                
            if func is None:
                func = self._default

            if func is None:
                LOGGER.info('No handler of ' + key + ' and no default handler')

            else:
                args_count = self.__get_args_count(func)
                if args_count == 0:
                    func()
                else:
                    func(event)        

    def add(self, event, message=None):
        """[Decorator] Add handler method.
        :param event: Specify a kind of Event which you want to handle
        :type event: T <= :py:class:`linebot.models.events.Event` class
        :param message: (optional) If event is MessageEvent,
            specify kind of Messages which you want to handle
        :type: message: T <= :py:class:`linebot.models.messages.Message` class
        :rtype: func
        :return: decorator
        """
        def decorator(func):
            if isinstance(message, (list, tuple)):
                for it in message:
                    self.__add_handler(func, event, message=it)
            else:
                self.__add_handler(func, event, message=message)

            return func

        return decorator

    def default(self):
        """[Decorator] Set default handler method.
        :rtype: func
        :return:
        """
        def decorator(func):
            self._default = func
            return func

        return decorator
    
    def __add_handler(self, func, event, message=None):
        key = self.__get_handler_key(event, message=message)
        self._handlers[key] = func

    @staticmethod
    def __get_args_count(func):
        if PY3:
            arg_spec = inspect.getfullargspec(func)
            return len(arg_spec.args)
        else:
            arg_spec = inspect.getargspec(func)
            return len(arg_spec.args)        
                    
    @staticmethod
    def __get_handler_key(event, message=None):
        if message is None:
            return event.__name__
        else:
            return event.__name__ + '_' + message.__name__                    
        
        
        
        
        
        
        