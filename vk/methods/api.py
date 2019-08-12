from vk.methods import Messages, Account
from vk.utils import ContextInstanceMixin
from vk import VK


class API(ContextInstanceMixin):
    def __init__(self, vk: VK):
        self.vk = vk

        self.messages = Messages(vk, category="messages")
        self.account = Account(vk, category="account")
