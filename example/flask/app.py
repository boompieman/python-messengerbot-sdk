from flask import Flask, request

from facebookbot import (
    FacebookBotApi, WebhookHandler
)

from facebookbot.models import (
    TextMessage, ImageMessage, VideoMessage, AudioMessage, 
    FileMessage, AttachmentMessage, LocationMessage, FallbackMessage,
    
    TextMessageEvent, AttachmentMessageEvent, GetStartedEvent, 
    PostbackEvent, LinkingEvent, UnLinkingEvent, TextEchoMessageEvent, AttachmentEchoMessageEvent,
    
    PostbackAction, URLAction, 
    TemplateSendMessage, ButtonsTemplate, GenericTemplate, MediaTemplate, 
    GenericElement, ImageElement, VideoElement,
    
    TextSendMessage, ImageSendMessage, VideoSendMessage, AudioSendMessage, FileSendMessage,
    LocationQuickReply, TextQuickReply,
    PostbackAction, URLAction, 
    ButtonsTemplate, TemplateSendMessage, GenericTemplate, GenericElement, ImageElement, VideoElement
)



app = Flask(__name__)



fb_bot_api = FacebookBotApi("YOUR_PAGE_ACCESS_TOKEN")

handler = WebhookHandler()

@app.route('/callback', methods=['GET'])
def verify():
    
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


@handler.add(GetStartedEvent)
def handle_get_started(event):
    
    fb_bot_api.push_message(
        user_id, 
        message=TextSendMessage(text='Welcome to this page/app...')
    )    
    
    # set welcome message   

@handler.add(TextMessageEvent)
def handle_text_message(event):
        
    text = event.message.text
    
    user_id = event.sender.id
    
    if text == "profile":
        
        profile = fb_bot_api.get_profile(user_id)
        
        fb_bot_api.push_message(
            user_id, 
            message=TextSendMessage(text='Display name: ' + profile.last_name + profile.first)
        )
    if text == "buttons":
        
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
        
        fb_bot_api.push_message(
            user_id, 
            message=buttons_template_message
        )
    if text == "generic":
        
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
        
        fb_bot_api.push_message(
            user_id, 
            message=generic_template_message
        )        
        
    if text == "media":
        
        # by URL
        image_send_message = ImageSendMessage(url="https://via.placeholder.com/1024x1024")

        attachment_id = fb_bot_api.upload_attachment(image_send_message)        
        
        media_template_message = TemplateSendMessage(
            template=MediaTemplate(
                elements=[
                    ImageElement(
                        attachment_id=attachment_id,
                        buttons=[
                            PostbackAction(title="postback_1", payload="data_1"),
                        ]
                    )
                ]
            )
        )
        
        fb_bot_api.push_message(
            user_id, 
            message=media_template_message
        )           
        
        # by facebook
        
#         media_template_message = TemplateSendMessage(
#             template=MediaTemplate(
#                 elements=[
#                     VideoElement(
#                         # see documents: 
#                         # https://developers.facebook.com/docs/messenger-platform/send-messages/template/media#facebook_url
#                         facebook_url="https://www.facebook.com/{USER_NAME}/videos/<NUMERIC_ID>/",
#                         buttons=[
#                             PostbackAction(title="postback_1", payload="data_1"),
#                             URLAction(
#                                 title="url_1",
#                                 url="http://example.com/1",
#                                 webview_height_ratio='full',
#                                 messenger_extensions=None,
#                                 fallback_url=None
#                             )
#                         ]
#                     )
#                 ]
#             )
#         )
        
#         fb_bot_api.push_message(
#             user_id, 
#             message=media_template_message
#         )          
        
                
        
        
    if text == "quick_reply":
        
        # Text Message quick reply
        fb_bot_api.push_message(
            user_id, 
            message=TextSendMessage(
                text = "Quick reply",
                quick_replies = [
                    TextQuickReply(title="title1", payload="payload_1"),
                    TextQuickReply(title="title2", payload="payload_2")
                ]          
            )
        )
        
        # Attachment Message quick reply
        
        buttons_template = ButtonsTemplate(
            text="buttons_template",
            buttons= [
                PostbackAction(title="action_1", payload="payload_1"),
                PostbackAction(title="action_2", payload="payload_2")
            ])

        templateSendMessage = TemplateSendMessage(
            template=buttons_template,
            quick_replies = [
                TextQuickReply(title="title1", payload="payload_1"),
                TextQuickReply(title="title2", payload="payload_2")
            ]
        )       


        fb_bot_api.push_message(
            user_id, 
            message=templateSendMessage
        )              
        
        
    if text.lower() == "broadcast":
        
        text_message = TextMessage(text = "broadcast 1")
        
        fb_bot_api.broadcast(message = text_message)
    
@handler.add(AttachmentMessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    
    url = event.message.attachment.payload.url
    
    user_id = event.sender.id
    
    if isinstance(event.message.attachment, ImageMessage):
        pass
        fb_bot_api.push_message(
            user_id, 
            message=ImageSendMessage(
                url = url
            )
        )
        
    elif isinstance(event.message.attachment, VideoMessage):
        
        fb_bot_apipush_message(
            user_id, 
            message=VideoSendMessage(
                url = url
            )
        )        
        
    elif isinstance(event.message.attachment, AudioMessage):
        
        fb_bot_apipush_message(
            user_id, 
            message=AudioSendMessage(
                url = url
            )
        )        
        
    else:
        return    
    
    
@handler.add(AttachmentMessageEvent, message=FileMessage)
def handle_file_message(event):
    
    print(event.message.attachment.type)
    
@handler.add(AttachmentMessageEvent, message=LocationMessage)
def handle_location_message(event):    

    print(event.message.attachment.type)
    
@handler.add(AttachmentMessageEvent, message=FallbackMessage)
def handle_fallback_message(event):    

    print(event.message.attachment.type)


@handler.add(PostbackEvent)
def handle_postback_message(event):

    postback_payload = event.postback.payload
    
    print(postback_payload)

@handler.add(LinkingEvent)
def handle_linking(event):
    print("event.LinkingEvent")
    
@handler.add(UnLinkingEvent)
def handle_unlinking(event):
    print("event.UnLinkingEvent")    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
