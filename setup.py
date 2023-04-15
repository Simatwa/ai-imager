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
    install_requires=open("requirements.txt", encoding="utf-8").readlines(),
    license="",
    python_requires=">=3.7",
    description="OpenAI based image generator and manipulator API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Customer Service",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            ("ai-imager = ai_imager.web_interface:start_server"),
        ]
    },
)
