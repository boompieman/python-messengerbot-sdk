# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

# from .actions import (  # noqa
#     Action,
#     PostbackAction,
#     MessageAction,
#     URIAction,
#     DatetimePickerAction,
#     CameraAction,
#     CameraRollAction,
#     LocationAction,
#     Action as TemplateAction,  # backward compatibility
#     PostbackAction as PostbackTemplateAction,  # backward compatibility
#     MessageAction as MessageTemplateAction,  # backward compatibility
#     URIAction as URITemplateAction,  # backward compatibility
#     DatetimePickerAction as DatetimePickerTemplateAction,  # backward compatibility
# )
from .base import (  # noqa
    Base,
)
from .error import (  # noqa
    Error,
    ErrorDetail,
)
from .events import (  # noqa
    Event,
    TextMessageEvent,
    AttachmentMessageEvent,
    GetStartedEvent,
    LinkingEvent,
    UnLinkingEvent,
#     FollowEvent,
#     UnfollowEvent,
#     JoinEvent,
#     LeaveEvent,
    PostbackEvent,
    TextEchoMessageEvent,
    AttachmentEchoMessageEvent,
    QuickReplyMessageEvent
#     AccountLinkEvent,
#     BeaconEvent,
#     Postback,
#     Beacon,
#     Link,
)
# from .flex_message import (  # noqa
#     FlexSendMessage,
#     FlexContainer,
#     BubbleContainer,
#     BubbleStyle,
#     BlockStyle,
#     CarouselContainer,
#     FlexComponent,
#     BoxComponent,
#     ActionComponent,
#     FillerComponent,
#     IconComponent,
#     ImageComponent,
#     SeparatorComponent,
#     SpacerComponent,
#     TextComponent
# )
# from .imagemap import (  # noqa
#     ImagemapSendMessage,
#     BaseSize,
#     ImagemapAction,
#     URIImagemapAction,
#     MessageImagemapAction,
#     ImagemapArea,
# )
from .messages import (  # noqa
    Message,
    TextMessage,
    AttachmentMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    FallbackMessage,
    QuickReplyMessage,
#     StickerMessage,
    FileMessage
)
from .responses import (  # noqa
    Profile,
#     MemberIds,
    Content,
#     RichMenuResponse,
#     Content as MessageContent,  # backward compatibility
)

from .persistent_menu import (
    PersistentMenu,
    
)
# from .rich_menu import (  # noqa
#     RichMenu,
#     RichMenuSize,
#     RichMenuArea,
#     RichMenuBounds,
# )
from .send_messages import (  # noqa
    SendMessage,
    TextSendMessage,
#     AttachmentMessage
    ImageSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    FileSendMessage,
#     LocationSendMessage,
#     StickerSendMessage,
    TextQuickReply,
    LocationQuickReply,
)

from .obj import (
    Obj
)

from .actions import (
    Action,
    PostbackAction,
    URLAction,
    NestedAction
)
# from .sources import (  # noqa
#     Source,
#     SourceUser,
#     SourceGroup,
#     SourceRoom,
# )

from .template import (  # noqa
    TemplateSendMessage,
    Template,
    ButtonsTemplate,
    GenericTemplate,
    MediaTemplate,
    GenericElement,
    ImageElement,
    VideoElement
#     ConfirmTemplate,
#     CarouselTemplate,
#     CarouselColumn,
#     ImageCarouselTemplate,
#     ImageCarouselColumn,
)