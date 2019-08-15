from .base import BaseMethod
from vk.types.responses import messages as m

import typing


class Messages(BaseMethod):
    async def add_chat_user(self, chat_id: int, user_id: int):
        """

        :param chat_id:
        :param user_id:
        :return:
        """
        method = self.get_method_name(self.add_chat_user)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AddChatUser(**r)

    async def allow_messages_from_group(self, group_id: int, key: str = None):
        """

        :param group_id:
        :param key:
        :return:
        """
        method = self.get_method_name(self.allow_messages_from_group)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.AllowMessagesFromGroup(**r)

    async def create_chat(self, user_ids: typing.List[int], title: str):
        """

        :param user_ids:
        :param title:
        :return:
        """
        method = self.get_method_name(self.create_chat)
        if user_ids:
            user_ids = self.list_to_str(user_ids)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.CreateChat(**r)

    async def delete(
        self,
        message_ids: typing.List[int],
        spam: int = None,
        group_id: int = None,
        delete_for_all: int = None,
    ):
        """

        :param message_ids:
        :param spam:
        :param group_id:
        :param delete_for_all:
        :return:
        """
        method = self.get_method_name(self.delete)
        if message_ids:
            message_ids = self.list_to_str(message_ids)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Delete(**r)

    async def delete_chat_photo(self, chat_id: int, group_id: int = None):
        """

        :param chat_id:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.delete_chat_photo)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteChatPhoto(**r)

    async def delete_conversation(
        self, peer_id: int, user_id: str = None, group_id: int = None
    ):
        """

        :param peer_id:
        :param user_id:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.delete_conversation)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DeleteConversation(**r)

    async def deny_messages_from_group(self, group_id: int):
        method = self.get_method_name(self.deny_messages_from_group)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.DenyMessagesFromGroup(**r)

    async def edit(
        self,
        peer_id: int,
        message_id: int,
        message: str = None,
        lat: float = None,
        long: float = None,
        attachment: str = None,
        keep_forward_messages: int = None,
        keep_snippets: int = None,
        group_id: int = None,
        dont_parse_links: int = None,
    ):
        """

        :param peer_id:
        :param message_id:
        :param message:
        :param lat:
        :param long:
        :param attachment:
        :param keep_forward_messages:
        :param keep_snippets:
        :param group_id:
        :param dont_parse_links:
        :return:
        """
        method = self.get_method_name(self.edit)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Edit(**r)

    async def edit_chat(self, chat_id: int, title: str):
        """

        :param chat_id:
        :param title:
        :return:
        """
        method = self.get_method_name(self.edit_chat)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.EditChat(**r)

    async def get_by_conversation_message_id(
        self,
        peer_id: int,
        conversation_message_ids: typing.List[int],
        extended: int = None,
        fields: typing.List[str] = None,
        group_id: int = None,
    ):
        """

        :param peer_id:
        :param conversation_message_ids:
        :param extended:
        :param fields:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.get_by_conversation_message_id)
        if conversation_message_ids:
            conversation_message_ids = self.list_to_str(conversation_message_ids)
        if fields:
            fields = self.list_to_str(fields)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetByConversationMessageId(**r)

    async def get_by_id(
        self,
        message_ids: typing.List[int],
        preview_legth: int = None,
        extended: int = 1,
        fields: typing.List[str] = None,
        group_id: str = None,
    ):
        """

        :param message_ids:
        :param preview_legth:
        :param extended:
        :param fields:
        :param group_id:
        :return:
        """
        method = self.get_method_name(self.get_by_id)
        if fields:
            fields = self.list_to_str(fields)
        if message_ids:
            message_ids = self.list_to_str(message_ids)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetById(**r)

    async def get_chat(
        self,
        chat_id: int = None,
        chat_ids: typing.List[int] = None,
        fields: typing.List[str] = None,
        name_case: str = None,
    ):
        """

        :param chat_id:
        :param chat_ids:
        :param fields:
        :param name_case:
        :return:
        """
        method = self.get_method_name(self.get_chat)
        if chat_ids:
            chat_ids = self.list_to_str(chat_ids)
        if fields:
            fields = self.list_to_str(fields)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.GetChat(**r)

    async def send(
        self,
        peer_id: int = None,
        random_id: int = 0,
        user_id: int = None,
        domain: str = None,
        chat_id: int = None,
        user_ids: typing.List[int] = None,
        message: str = None,
        lat: float = None,
        long: float = None,
        attachment: str = None,
        reply_to: int = None,
        forward_messages: typing.List[int] = None,
        sticker_id: int = None,
        group_id: int = None,
        keyboard: dict = None,
        payload: str = None,
        dont_parse_links: int = None,
        disable_mentions: int = None,
    ):
        method = self.get_method_name(self.send)
        if user_ids:
            user_ids = self.list_to_str(user_ids)
        if forward_messages:
            forward_messages = self.list_to_str(forward_messages)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return m.Send(**r)
