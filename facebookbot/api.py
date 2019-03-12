import json

from .http_client import HttpClient, RequestsHttpClient

from .exceptions import FacebookBotApiError

from .models import (
    Profile, Error, Content
)

class FacebookBotApi(object):

    DEFAULT_API_ENDPOINT = 'https://graph.facebook.com'

    def __init__(self, page_access_token, endpoint=DEFAULT_API_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
                 
            
        self.endpoint = endpoint
        
        self.headers = {}
        
        self.params = {
            "access_token": page_access_token
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
        
        
    def broadcast(self, message, notification_type="REGULAR", timeout = 60):   
        
        data = {
            
            "messages": [message.as_json_dict()]
            
        }
        
        response = self._post(path="/v3.2/me/message_creatives", params=self.params, data=json.dumps(data), timeout=timeout)
        
        message_creative_id = response.json["message_creative_id"]
        
        multicast_data = {
            "message_creative_id": message_creative_id,
            "notification_type": notification_type,
            "messaging_type": "MESSAGE_TAG",
            "tag": "NON_PROMOTIONAL_SUBSCRIPTION"
        }
        
        self._post(path="/v3.2/me/broadcast_messages", params=self.params, data=json.dumps(multicast_data), timeout=timeout)
        
        
    def setup_persistent_menu(self, persistent_menus, timeout=None):        
        
        if not isinstance(persistent_menus, (list, tuple)):
            persistent_menus = [persistent_menus]        
        
        persistent_menu = {
            "persistent_menu":[ persistent_menu.as_json_dict() for persistent_menu in persistent_menus ]
        }
        
        self._post(path="/v3.2/me/messenger_profile", params = self.params, data=json.dumps(persistent_menu), timeout=timeout)        
        

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
    
    def upload_local_attachment(self, file_path, file_type, timeout=None):
        
        if "image" in file_type:
            
            data = {"attachment":{"type":"image", "payload":{"is_reusable":True}}}
            
        elif "video" in file_type:
            
            data = {"attachment":{"type":"video", "payload":{"is_reusable":True}}}
        
        
        if '/' in file_path:
            file_name = file_path.split('/')[-1]

        else:
            file_name = file_path


        files = {
            'filedata': (file_name, open(file_path, 'rb'), file_type)
        }

        response = self._post(
            path="/v3.2/me/message_attachments",
            params = self.params,
            data = {'message': json.dumps(data)},
            timeout=timeout,
            headers = {},
            files=files
        )        

        return response.json.get("attachment_id")
        
    def upload_remote_attachment(self, attachment_send_message, timeout=None):
        
        attachment_data = {
            
            "message": attachment_send_message.as_json_dict()
        }
        
        response = self._post(path="/v3.2/me/message_attachments", params = self.params, data=json.dumps(attachment_data), timeout=timeout)
        
        return response.json.get("attachment_id")
        
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

    def _post(self, path, params=None, data=None, headers=None, timeout=None, files=None):
        url = self.endpoint + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)
        
        response = self.http_client.post(
            url, params=params, headers=headers, data=data, timeout=timeout, files=files
        )
        
        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:

            response_error = Error.new_from_json_dict(response.json)

            raise FacebookBotApiError(response_error.error.code, response_error.error)