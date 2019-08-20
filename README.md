# Welcome to vk.py 👋

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000) [ ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ](https://github.com/prostomarkeloff/vk.py/blob/master/LICENSE) [![Twitter: prostomarkeloff](https://img.shields.io/twitter/follow/prostomarkeloff.svg?style=social)](https://twitter.com/prostomarkeloff)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cac2f27aab0a41f993660a525c054bb5)](https://app.codacy.com/app/prostomarkeloff/vk.py?utm_source=github.com&utm_medium=referral&utm_content=prostomarkeloff/vk.py&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/prostomarkeloff/vk.py.svg?branch=master)](https://travis-ci.org/prostomarkeloff/vk.py)

> VK.py its a pretty and fully asynchronous API wrapper for VK API based on asyncio and aiohttp.



### 🏠 [Homepage](github.com/prostomarkeloff/vk.py)


This library implemented all VK methods and types, based on PyDantic models.

## Install

```sh
pip install https://github.com/prostomarkeloff/vk.py/archive/master.zip —upgrade
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

## Philosophy and Features
- ***k the low level API. Set async/await in your code and it will work beautifully and quickly!
  
- All typed. All objects and responses which represents API (vk.com/dev) is in library. This helps IDE`s and help you save time.
  
- All fast. VK.py uses [orjson](https://github.com/ijl/orjson) as JSON serialize/deserealize driver and [uvloop](https://github.com/MagicStack/uvloop) as event loop. This help you write effective code.

- Easily debugging. All places in code logged. Set logger level as "DEBUG" and debug your code!
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
