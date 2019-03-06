python-messengerbot-sdk
===================

SDK of the Facebook Messenger API for Python.

Install
-------

::

    $ pip install python-messengerbot-sdk
    
Synopsis
--------

Usage:    

.. code:: python

    from flask import Flask, request

    from facebookbot import (
        FacebookBotApi, WebhookHandler
    )

    from facebookbot.models import (

        TextMessageEvent, TextSendMessage, TextSendMessage
    )

    app = Flask(__name__)
    
    facebook_bot_api = FacebookBotApi("YOUR_PAGE_ACCESS_TOKEN")

    handler = WebhookHandler()


    @app.route('/callback', methods=['GET'])
    def verify():
        # when the endpoint is registered as a webhook, it must echo back
        # the 'hub.challenge' value it receives in the query arguments
        if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
            if not request.args.get("hub.verify_token") == "YOUR_VERIFY_TOKEN":
                return "Verification token mismatch", 403
            return request.args["hub.challenge"], 200

        return "Hello world", 200


    @app.route('/callback', methods=['POST'])
    def webhook():

        # endpoint for processing incoming messaging events

        body = request.get_json()

        handler.handle(body)

        return "ok", 200  

    @handler.add(TextMessageEvent)
    def handle_text_message(event):
        facebook_bot_api.push_message(
           event.sender.id,
           message=TextSendMessage(text=event.message.text)
        )

    if __name__ == "__main__":
        app.run()

API
---

MessengerBotApi
~~~~~~~~~~

\_\_init\_\_(self, page\_access\_token, endpoint='https://graph.facebook.com', timeout=5, http\_client=RequestsHttpClient)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new FacebookBotApi instance.

.. code:: python

    facebook_bot_api = facebookbot.LineBotApi('YOUR_PAGE_ACCESS_TOKEN')

You can override the ``timeout`` value for each method.

setup\_started\_button(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

setup started button, when press it, then responding from GetStartedEvent

.. code:: python

    facebook_bot_api.setup_started_button()

push\_message(self, user\_id, message, is\_sender\_action = True, timeout = None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send messages to users

.. code:: python

    facebook_bot_api.push_message(user_id, TextSendMessage(text='Hello World!'))

broadcast(self, message, notification\_type="REGULAR", timeout = 60)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

broadcast to all page followers but limited to 10,000 per message.

.. code:: python

    facebook_bot_api.broadcast(TextSendMessage(text='Hello World!'))
    
broadcast(self, message, notification\_type="REGULAR", timeout = 60)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

broadcast to all page followers but limited to 10,000 per message.

.. code:: python

    facebook_bot_api.broadcast(TextSendMessage(text='Hello World!'))

get\_profile(self, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get user profile information.

.. code:: python

    profile = facebook_bot_api.get_profile(user_id)

    print(profile.first_name)
    print(profile.last_name)
    print(profile.gender)
    print(profile.profile_pic)
    print(profile.locale)
    print(profile.timezone)
    
upload\_attachment(self, attachment\_send\_message, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

upload attachment to reuse and get attachment_id

.. code:: python

    image = ImageSendMessage(image_url="pic_url.jpg")
    attachment_id = facebook_bot_api.upload_attachment(image)
    print(attachment_id)

