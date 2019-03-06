python-messengerbot-sdk
===================

SDK of the Facebook Messenger API for Python.

Most code structure were followed by `line-bot-sdk-python <https://github.com/line/line-bot-sdk-python>`__

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

Message objects
~~~~~~~~~~~~~~~

The following classes are found in the ``facebookbot.models`` package.

TextSendMessage
^^^^^^^^^^^^^^^

.. code:: python

    text_message = TextSendMessage(text='Hello, world')

ImageSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    image_message = ImageSendMessage(
        image_url='https://example.com/original.jpg',
        is_reusable=True
    )

VideoSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    video_message = VideoSendMessage(
        video_url='https://example.com/original.mp4',
        is_reusable=True
    )

AudioSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    audio_message = AudioSendMessage(
        audio_url='https://example.com/original.m4a',
        is_reusable=True
    )
    
FileSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    file_message = FileSendMessage(
        file_url='https://example.com/original.pdf',
        is_reusable=True
    )

TemplateSendMessage - ButtonsTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    buttons_template_message = TemplateSendMessage(
        template=ButtonsTemplate(
            text="Buttons template",
            buttons=[
                PostbackAction(
                    title="postback",
                    payload="action=buy&itemid=1"
                ),
                URLAction(
                    title="url", 
                    url="http://example.com/", 
                    webview_height_ratio='full', 
                    messenger_extensions=None, 
                    fallback_url=None
                )
            ]
        )
    )

TemplateSendMessage - GenericTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    generic_template_message = TemplateSendMessage(
        template=GenericTemplate(
            elements=[
                GenericElement(
                    title="GenericElement 1",
                    image_url="https://example.com/item1.jpg",
                    subtitle="description1",
                    default_action=URLAction(url="http://example.com/"),
                    buttons=[
                        PostbackAction(title="postback_1", payload="data_1"),
                        URLAction(
                            title="url_1", 
                            url="http://example.com/1", 
                            webview_height_ratio='full', 
                            messenger_extensions=None, 
                            fallback_url=None
                        )
                    ]
                ),
                GenericElement(
                    title="GenericElement 2",
                    image_url="https://example.com/item2.jpg",
                    subtitle="description2",
                    default_action=URLAction(url="http://example.com/"),
                    buttons=[
                        PostbackAction(title="postback_2", payload="data_2"),
                        URLAction(
                            title="url_2", 
                            url="http://example.com/2", 
                            webview_height_ratio='compact', 
                            messenger_extensions=None, 
                            fallback_url=None
                        )
                    ]
                )            
            ]
        )
    )
    
TemplateSendMessage - MediaTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By attachment_id

.. code:: python

    media_template_message = TemplateSendMessage(
        template=MediaTemplate(
            elements=[
                ImageElement(
                    attachment_id=attachment_id,
                    buttons=[
                        PostbackAction(title="postback_1", payload="data_1"),
                        URLAction(
                            title="url_1", 
                            url="http://example.com/1", 
                            webview_height_ratio='full', 
                            messenger_extensions=None, 
                            fallback_url=None
                        )
                    ]
                )
            ]
        )
    )

By facebook_url

.. code:: python

    media_template_message = TemplateSendMessage(
        template=MediaTemplate(
            elements=[
                ImageElement(
                    url="https://www.facebook.com/photo.php?fbid=<NUMERIC_ID>",
                    buttons=[
                        PostbackAction(title="postback_1", payload="data_1"),
                        URLAction(
                            title="url_1", 
                            url="http://example.com/1", 
                            webview_height_ratio='full', 
                            messenger_extensions=None, 
                            fallback_url=None
                        )
                    ]
                )
            ]
        )
    )


Hints
-----

Examples
~~~~~~~~

`object-example <https://github.com/boompieman/python-messengerbot-sdk>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

