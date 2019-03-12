from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod, abstractproperty

import requests
from future.utils import with_metaclass


class HttpClient(with_metaclass(ABCMeta)):
    """Abstract Base Classes of HttpClient."""

    DEFAULT_TIMEOUT = 5
    

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """__init__ method.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        self.timeout = timeout

    @abstractmethod
    def get(self, url, headers=None, params=None, stream=False, timeout=None):
        """GET request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param bool stream: (optional) get content as stream
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
    def post(self, url, headers=None, params=None, data=None, timeout=None, files=None):
        """POST request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, url, headers=None, data=None, timeout=None):
        """DELETE request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError


class RequestsHttpClient(HttpClient):
    """HttpClient implemented by requests."""

    def __init__(self, timeout=HttpClient.DEFAULT_TIMEOUT):
        """__init__ method.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        """
        super(RequestsHttpClient, self).__init__(timeout)

    def get(self, url, headers=None, params=None, stream=False, timeout=None):
        """GET request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param bool stream: (optional) get content as stream
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.get(
            url, headers=headers, params=params, stream=stream, timeout=timeout
        )

        return RequestsHttpResponse(response)

    def post(self, url, headers=None, params=None, data=None, timeout=None, files=None):
        """POST request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.post(
            url, headers=headers, params=params, data=data, timeout=timeout, files = files
        )

        return RequestsHttpResponse(response)

    def delete(self, url, headers=None, data=None, timeout=None):
        """DELETE request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.delete(
            url, headers=headers, data=data, timeout=timeout
        )

        return RequestsHttpResponse(response)


class HttpResponse(with_metaclass(ABCMeta)):
    """HttpResponse."""

    @abstractproperty
    def status_code(self):
        """Get status code."""
        raise NotImplementedError

    @abstractproperty
    def headers(self):
        """Get headers."""
        raise NotImplementedError

    @abstractproperty
    def text(self):
        """Get request body as text-decoded."""
        raise NotImplementedError

    @abstractproperty
    def content(self):
        """Get request body as binary."""
        raise NotImplementedError

    @abstractproperty
    def json(self):
        """Get request body as json-decoded."""
        raise NotImplementedError

    @abstractmethod
    def iter_content(self, chunk_size=1024, decode_unicode=False):
        """Get request body as iterator content (stream).
        :param int chunk_size:
        :param bool decode_unicode:
        """
        raise NotImplementedError


class RequestsHttpResponse(HttpResponse):
    """HttpResponse implemented by requests lib's response."""

    def __init__(self, response):
        """__init__ method.
        :param response: requests lib's response
        """
        self.response = response

    @property
    def status_code(self):
        """Get status code."""
        return self.response.status_code

    @property
    def headers(self):
        """Get headers."""
        return self.response.headers

    @property
    def text(self):
        """Get request body as text-decoded."""
        return self.response.text

    @property
    def content(self):
        """Get request body as binary."""
        return self.response.content

    @property
    def json(self):
        """Get request body as json-decoded."""
        return self.response.json()

    def iter_content(self, chunk_size=1024, decode_unicode=False):
        """Get request body as iterator content (stream).
        :param int chunk_size:
        :param bool decode_unicode:
        """
        return self.response.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode)