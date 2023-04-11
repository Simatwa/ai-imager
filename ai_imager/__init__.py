__version__ = "0.0.1"
__repo__ = "https://github.com/Simatwa/ai-imager"
import logging
import openai

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

    def decorator(func: function):
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
