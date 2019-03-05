from __future__ import unicode_literals

from .base import Base


class Error(Base):

    def __init__(self, error=None, message=None, type=None, code=None, error_subcode=None, fbtrace_id=None, **kwargs):

        super(Error, self).__init__(**kwargs)
#         self.message = message
#         self.type = type
#         self.code = code
#         self.error_subcode = error_subcode
#         self.fbtrace_id = fbtrace_id        
        

        self.error = self.get_or_new_from_json_dict(error, ErrorDetail)

class ErrorDetail(Base):

    def __init__(self, message=None, type=None, code=None, error_subcode=None, fbtrace_id=None, **kwargs):

        super(ErrorDetail, self).__init__(**kwargs)

        self.message = message
        self.type = type
        self.code = code
        self.error_subcode = error_subcode
        self.fbtrace_id = fbtrace_id