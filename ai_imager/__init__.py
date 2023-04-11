__version__ = "0.0.1"
__repo__ = "https://github.com/Simatwa/ai-imager"
__author__,__author_email__,__maintainer__,__maintainer_email__=("",)*4

import logging
import openai
from appdirs import AppDirs
from os import path,makedirs

__all__=[
    "imager",
    "web_interface",
]

app_data_dir = AppDirs("Smartwa","ai-imager").user_data_dir

if not path.isdir(app_data_dir):
    try:
        makedirs(app_data_dir)
    except Exception as e:
        print(f"Error while creating data-dir : {e.args[1] or e}")

logging.basicConfig(
    format="%(asctime)s - %(levelname)s : %(message)s",
    datefmt="%d-%b-%Y %H:%M:S",
    level=logging.INFO,
)



def getExc(e: object):
    """Get exact error message

    Args:
        e (object): Exception object

    Returns:
        _type_: str
    """
    return e.args[1] or str(e)


def error_handler(log: bool = True):
    """Decorator for appending exception handler"""

    def decorator(func: object):
        def main(*args, **kwargs):
            try:
                if log:
                    logging.debug(f"Function executing - {func.__name__}")
                resp = func(*args, **kwargs)
            except openai.error.OpenAIError as e:
                resp = f"{e.http_status} : {e.error}"
                logging.error(resp)
                return resp
            except Exception as e:
                logging.error(getExc(e))
            else:
                return resp

        return main

    return decorator
