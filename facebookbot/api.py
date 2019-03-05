import json

from .http_client import HttpClient, RequestsHttpClient

from .exceptions import FacebookBotApiError

from .models import (
    Profile, Error
)

class FacebookBotApi(object):

    DEFAULT_API_ENDPOINT = 'https://graph.facebook.com'

    def __init__(self, channel_access_token, endpoint=DEFAULT_API_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
                 
            
        self.endpoint = endpoint
        
        self.headers = {}
        
        self.params = {
            "access_token": channel_access_token
        }
        
        if http_client:
            self.http_client = http_client(timeout=timeout)
        else:
            self.http_client = RequestsHttpClient(timeout=timeout)
        
    def push_message(self, user_id, message, is_sender_action = True, timeout = None):
        
        if is_sender_action:
            sender_action_data = {
                "recipient": {
                    "id": user_id
                },

                "sender_action":"typing_on"
            }
            
            self._post(path="/v3.2/me/messages", params=self.params, data=json.dumps(sender_action_data), timeout=timeout)
        
        data = {
            
            "recipient": {
                "id": user_id
            },
            
            "message": message.as_json_dict()
        }
        
        self._post(path="/v3.2/me/messages", params=self.params, data=json.dumps(data), timeout=timeout)
        
#     def multicast(self, messages):
        

    def setup_started_button(self, timeout=None):
        
        started_button = {
            "get_started": {
                "payload":"get_started"
            }
        }
        
        self._post(path="/v3.2/me/messenger_profile", params = self.params, data=json.dumps(started_button), timeout=timeout)
        
    def get_profile(self, user_id, timeout=None):
        
        params = {"fields": "first_name,last_name,profile_pic,gender,locale,timezone"}
        
        params.update(self.params)
        
        response = self._get(
            '/{user_id}'.format(user_id=user_id),
            params = params,
            timeout=timeout
        )
        
        return Profile.new_from_json_dict(response.json)

        
        
        
    def _get(self, path, params=None, headers=None, stream=False, timeout=None):
        
        url = self.endpoint + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.get(
            url, headers=headers, params=params, stream=stream, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _post(self, path, params=None, data=None, headers=None, timeout=None):
        url = self.endpoint + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.post(
            url, params=params, headers=headers, data=data, timeout=timeout
        )
        
        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            print(response.json)
            error = Error.new_from_json_dict(response.json)
            print(error)
            raise FacebookBotApiError(response.status_code, error)