import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vk.py",
    version="0.1.0",
    author="prostomarkeloff",
    description="VK.py its a pretty and fully asynchronous API wrapper for VK API based on asyncio and aiohttp.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prostomarkeloff/vk.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)