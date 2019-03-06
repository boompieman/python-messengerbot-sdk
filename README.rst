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
