from enum import Enum
from ..base import BaseModel
from .photo import Photo, PostedPhoto
from .video import Video
from .audio import Audio
from .document import Document
from .graffiti import Graffiti
from .link import Link
from .note import Note
from .app import App
from .poll import Poll
from .page import Page
from .album import Album
from .market import Market
from .market_album import MarketAlbum
from .sticker import Sticker
from .pretty_cards import PrettyCards
from .audio_msg import AudioMsg

import typing


# https://vk.com/dev/objects/attachments_w


class Attachments(str, Enum):
    not_attachments = []
    photo = Photo
    posted_photo = PostedPhoto
    video = Video
    audio = Audio
    document = Document
    graffiti = Graffiti
    link = Link
    note = Note
    app = App
    poll = Poll
    page = Page
    album = Album
    photos_list = typing.List[int]
    market = Market
    market_album = MarketAlbum
    sticker = Sticker
    pretty_cards = PrettyCards


class Attachment(BaseModel):
    type: str = None
    photo: Photo = None
    posted_photo: PostedPhoto = None
    video: Video = None
    audio: Audio = None
    document: Document = None
    graffiti: Graffiti = None
    link: Link = None
    note: Note = None
    app: App = None
    poll: Poll = None
    page: Page = None
    album: Album = None
    photos_list: typing.List[Photo] = []
    market: Market = None
    market_album: MarketAlbum = None
    sticker: Sticker = None
    pretty_cards: PrettyCards = None
    audio_message: AudioMsg = None
