# Welcome to vk.py 👋

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000) [ ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ](https://github.com/prostomarkeloff/vk.py/blob/master/LICENSE) [![Twitter: prostomarkeloff](https://img.shields.io/twitter/follow/prostomarkeloff.svg?style=social)](https://twitter.com/prostomarkeloff)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cac2f27aab0a41f993660a525c054bb5)](https://app.codacy.com/app/prostomarkeloff/vk.py?utm_source=github.com&utm_medium=referral&utm_content=prostomarkeloff/vk.py&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/prostomarkeloff/vk.py.svg?branch=master)](https://travis-ci.org/prostomarkeloff/vk.py)

> Extremely-fast Python 3.6+ toolkit for create applications work`s with VKAPI.



### 🏠 [Homepage](github.com/prostomarkeloff/vk.py)


## Install

```sh
pip install https://github.com/prostomarkeloff/vk.py/archive/master.zip --upgrade
```

or (old version)

```sh
pip install vk.py
```

## Usage

Simple example
```python
from vk import VK
from vk.utils.task_manager import TaskManager
import logging

logging.basicConfig(level="INFO")
vk = VK(access_token=<TOKEN>)

async def status_get():
    resp = await vk.api_request("status.get")
    print(resp)

if __name__ == "__main__":
    task_manager = TaskManager(vk.loop)
    task_manager.add_task(status_get)
    task_manager.run()

```

More examples [click](./examples)

## Features

- Rich high-level API.
- Fully asynchronous. Based on asyncio and aiohttp.
- Bot framework out of-the-box.
- Fully typed. Thanks to Pydantic.
- The fastest.


## Performance
The fastest Python library for access to VKAPI.

- Accept and handle event from LongPoll API in bot framework (with sending a message to the user): lower than 0.1s 
- Check 100 handlers and execute 100 filters in bot framework (without sending a message to the user): lower than 0.001s

## Alternatives

- Kutana. Bot engine for create bots in Telegram and VK.
- VKBottle. Bot framework for develop bots in VK.
- VK_API. Simple library for access to VKAPI.
And many others library`s...

## Author

👤 **prostomarkeloff**

* Twitter: [@prostomarkeloff](https://twitter.com/prostomarkeloff)
* Github: [@prostomarkeloff](https://github.com/prostomarkeloff)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/prostomarkeloff/vk.py/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [prostomarkeloff](https://github.com/prostomarkeloff).<br />
This project is [MIT](https://github.com/prostomarkeloff/vk.py/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
