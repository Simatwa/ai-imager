from setuptools import setup
from ai_imager import (
    __version__,
    __author__,
    __author_email__,
    __maintainer__,
    __maintainer_email__,
    __repo__,
)

setup(
    name="ai_imager",
    version=__version__,
    packages=["ai_imager"],
    author=__author__,
    author_email=__author_email__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url=__repo__,
    install_requires=[
        "Pillow==9.5.0",
        "openai==0.27.4",
    ],
    license="",
    python_requires=">=3.7",
    description="OpenAI Image-handler API",
    long_description=open("README.md", encoding="utf-8").read(),
    classifiers=[
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            ("ai-imager = ai_imager.web_interface:start_server"),
        ]
    },
)
