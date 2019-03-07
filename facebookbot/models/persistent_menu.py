from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .actions import get_actions
from .base import Base

class PersistentMenu(with_metaclass(ABCMeta, Base)):

    def __init__(self, locale="default", composer_input_disabled=False, call_to_actions=None, **kwargs):

        super(PersistentMenu, self).__init__(**kwargs)

        self.locale = locale
        self.composer_input_disabled = composer_input_disabled

        self.call_to_actions = get_actions(call_to_actions)
        
        
