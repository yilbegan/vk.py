"""
 MIT License
 
 Copyright (c) 2019 prostomarkeloff
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""

"""
File which contains all constants of project.
"""

API_VERSION: str = "5.101"  # current api version https://vk.com/dev/versions

API_LINK: str = "https://api.vk.com/method/"  # link to access API

try:
    import orjson
except:
    try:
        import ujson as orjson
    except:
        import json as orjson

JSON_LIBRARY = orjson


def default_rules():
    from vk.bot_framework.rules.rules import Commands, Text, Payload, ChatAction

    DEFAULT_RULES = {
        "commands": Commands,
        "text": Text,
        "payload": Payload,
        "chat_action": ChatAction,
    }
    return DEFAULT_RULES
