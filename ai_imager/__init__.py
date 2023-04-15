__version__ = "0.0.5"
__repo__ = "https://github.com/Simatwa/ai-imager"
__author__, __author_email__, __maintainer__, __maintainer_email__ = (
    "Smartwa Caleb",
    "smartwacaleb@gmail.com",
) * 2

import logging
import openai
from appdirs import AppDirs
from os import path, makedirs

__all__ = [
    "imager",
    "web_interface",
]

app_data_dir = AppDirs("ai-imager", "Smartwa", __version__).user_data_dir

if not path.isdir(app_data_dir):
    try:
        makedirs(app_data_dir)
    except Exception as e:
        from sys import exit

        exit(f"Error while creating data-dir : {e.args[1] or e}")


def getExc(e: object):
    """Get exact error message

    Args:
        e (object): Exception object

    Returns:
        _type_: str
    """
    return e.args[1] if len(e.args) > 1 else str(e)


def error_handler(log: bool = True):
    """Decorator for appending exception handler"""

    def decorator(func: object):
        def main(*args, **kwargs):
            try:
                if log:
                    logging.debug(f"Function executing - {func.__name__}")
                resp = func(*args, **kwargs)
            except openai.error.OpenAIError as e:
                print(e)
                if not all([e.http_status, e.error]):
                    resp = "Server is missing OPENAI-API-KEY"
                else:
                    resp = e.error
                    logging.error(resp)
                return resp
            except Exception as e:
                resp = getExc(e)
                logging.error(f"Function : {func.__name__} - {resp}")
            else:
                return resp

        return main

    return decorator
