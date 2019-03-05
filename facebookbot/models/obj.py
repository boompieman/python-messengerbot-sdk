from __future__ import unicode_literals

import warnings
from abc import ABCMeta, abstractproperty

from future.utils import with_metaclass

from .base import Base


class Obj(with_metaclass(ABCMeta, Base)):

    def __init__(self, id=None, **kwargs):

        super(Obj, self).__init__(**kwargs)
        self.id = id

    @abstractproperty
    def object_id(self):

        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        raise NotImplementedError

    @property
    def object_id(self):
        """Alias of user_id.
        'object_id' is deprecated. Use 'user_id' instead.
        :rtype: str
        :return:
        """
        warnings.warn("'sender_id' is deprecated.", DeprecationWarning, stacklevel=2)
        return self.id
