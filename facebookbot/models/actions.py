from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


def get_action(action):
    """Get action."""
    action_obj = Base.get_or_new_from_json_dict_with_types(
        action, {
            'postback': PostbackAction,
            'web_url': URLAction,
            'nested': NestedAction
        }
    )
    return action_obj


def get_actions(actions):
    """Get actions."""
    new_actions = []
    if actions:
        for action in actions:
            action_obj = get_action(action)
            if action_obj:
                new_actions.append(action_obj)

    return new_actions


class Action(with_metaclass(ABCMeta, Base)):
    """Abstract base class of Action."""

    def __init__(self, **kwargs):

        super(Action, self).__init__(**kwargs)

        self.type = None


class PostbackAction(Action):

    def __init__(self, title=None, payload=None, **kwargs):

        super(PostbackAction, self).__init__(**kwargs)

        self.type = 'postback'
        self.title = title
        self.payload = payload
        
class URLAction(Action):
    
    def __init__(self, title=None, url=None, webview_height_ratio="full", messenger_extensions=None, fallback_url=None, **kwargs):

        super(URLAction, self).__init__(**kwargs)

        self.type = 'web_url'
        self.title = title
        self.url = url
        self.webview_height_ratio = webview_height_ratio
        self.messenger_extensions = messenger_extensions
        self.fallback_url = fallback_url
        
class NestedAction(Action):
    
    def __init__(self, title=None, call_to_actions=None, **kwargs):

        super(NestedAction, self).__init__(**kwargs)

        self.type = 'nested'
        self.title = title
        self.call_to_actions = get_actions(call_to_actions)
