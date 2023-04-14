from flask import *
from . import app_data_dir, logging, getExc, __version__, openai
from . import error_handler as exception_handler
from .imager import openai_handler
from os import path

app_data_dir = path.join(
    app_data_dir, "contents"
)  #'/home/smartwa/git/ai-imager/contents'


class local_config:
    def __init__(self):
        self.auth_cookie_key = "openai_api_key"
        self.upload_path = self.get_path("uploads")
        self.incomplete_form_msg = "Kindly fill all the fields"

    def get_path(self, *args):
        return path.join(app_data_dir, "/".join(args))

    @classmethod
    def get_cookie(self, key):
        """Gets cookie from user
        Args:
            key (_type_): Cookie name

        Returns:
            str|None: Value | None
        """
        return request.cookies.get(key)

    @classmethod
    def get_from_form(self, *keys, resp: dict = {}):
        for key in keys:
            resp[key] = request.form.get(key)
        return resp

    # @classmethod
    def get_from_file(self, *keys, resp: dict = {}):
        """Retrieve files from form

        Args:
            resp (dict, optional): Dictionary to add the response. Defaults to {}.
            keys (str): Name of the files


        Returns:
            dict: name and filepath
        """
        for key in keys:
            file = request.files.get(key)
            if file:
                filepath = path.join(self.upload_path, file.filename)
                file.save(filepath)
                resp[key] = filepath
            else:
                resp[key] = None
        return resp

    @classmethod
    def format_response(self, resp: list, http_code: int = 200, error: bool = None):
        """Format response to be handled by API

        Args:
            resp (str | list): Response
            error (bool, optional): Specifies to handle resp as error . Defaults to False.

        Returns:
            json: Respnse formatted for API
        """
        if not isinstance(resp, list):
            error = True
            http_code = 501 if http_code == 200 else http_code
        api_data = {
            "url": resp if not error else None,
            "error": None if not error else resp,
        }

        return jsonify(api_data), http_code

    @classmethod
    def imager_error_handler(self):
        """Exception handler at API level"""

        def decorator(func):
            def main(*args, **kwargs):
                try:
                    return func(*args, **args)
                except Exception as e:
                    return jsonify({"error": self.format_response(getExc(e))})

            return main

        return decorator


def API(port: int = 8000, debug: bool = True, host: bool = False):
    """Start the web app

    Args:
        port (int, optional): Port for web to listen. Defaults to 8000.
        debug (bool, optional): Start the app in debug mode. Defaults to True.
        host (bool | str, optional): Host the web on LAN. Defaults to False.

    Returns:
        None: None
    """
    api_config = local_config()
    openai = openai_handler()
    app = Flask(
        __name__,
        static_folder=api_config.get_path("static"),
        template_folder=api_config.get_path("templates"),
    )

    @local_config.imager_error_handler()
    @app.route("/")
    def index():
        """Landing page"""
        return render_template("index.html")

    @local_config.imager_error_handler()
    @app.route("/v1/image/<action>", methods=["GET"])
    def imager(action):
        """Handle v1 routings"""
        if not action in ("prompt", "variation", "mask"):
            action = "prompt"
        return render_template(
            "form.html", category=action, action=f"/v1/image/{action}/generate"
        )

    @local_config.imager_error_handler()
    @app.route("/v1/image/prompt/generate", methods=["POST"])
    def create_from_prompt():
        """Generate image from text"""
        form_data = api_config.get_from_form("prompt", "total_images", "image_size")
        if all(list(form_data.values())):
            resp = openai.create_from_prompt(**form_data)
            return local_config.format_response(resp)
        else:
            return local_config.format_response(
                api_config.incomplete_form_msg, http_code=400
            )

    @local_config.imager_error_handler()
    @app.route("/v1/image/mask/generate", methods=["POST"])
    def edit_with_mask():
        """Edit image with mask"""
        files = api_config.get_from_file("original_image_path", "masked_image_path")
        texts = api_config.get_from_form("prompt", "total_images", "image_size")
        files.update(texts)
        if all(list(files.values())):
            resp = openai.create_edit(**files)
            return local_config.format_response(resp)
        else:
            return api_config.format_response(
                api_config.incomplete_form_msg, http_code=400
            )

    @local_config.imager_error_handler()
    @app.route("/v1/image/variation/generate", methods=["POST"])
    def get_variation():
        """Get another image like same"""
        files = api_config.get_from_file("path_to_image")
        texts = api_config.get_from_form("total_images", "image_size")
        files.update(texts)
        if all(list(files.values())):
            resp = openai.create_variation(**files)
            return local_config.format_response(resp)
        else:
            return api_config.format_response(
                api_config.incomplete_form_msg, http_code=400
            )

    launch_configs = {
        "port": port,
        "debug": debug,
        "threaded": True,
    }
    if host:
        launch_configs["host"] = "0.0.0.0"

    app.run(**launch_configs)

@exception_handler(log=False)
def start_server():
    """Server entry"""
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Manipulate images with OpenAI's model",
        epilog="This script has no official relation with OpenAI.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "port", nargs="*", type=int, help="Port to start the server", default=8000
    )
    parser.add_argument("-k", "--key", help="OpenAI's API key")
    parser.add_argument(
        "-kp", "--key-path", help="Path to OpenAI-API-KEY path", metavar="PATH"
    )
    parser.add_argument(
        "-l",
        "--logging-level",
        type=int,
        help="Log level of the app",
        choices=[10, 20, 30, 40, 50],
        metavar="10-50",
        default=20,
    )
    parser.add_argument("-o", "--output", help="Filepath to log to", metavar="PATH")
    parser.add_argument("--host", action="store_true", help="Host the site on LAN")
    parser.add_argument(
        "--debug", action="store_true", help="Start as debugging server"
    )
    args = parser.parse_args()
    if args.key:
        openai.api_key = args.key

    if args.key_path:
        openai.api_key_path = args.key_path

    if any([args.logging_level, args.output]):
        log_config = {
            "format": "%(asctime)s - %(levelname)s : %(message)s %(module)s:%(lineno)s",
            "datefmt": "%d-%b-%Y %H:%M:%S",
            "level": args.logging_level,
        }
        if args.output:
            log_config["filename"] = args.output
        logging.basicConfig(**log_config)
    API(args.port, args.debug, args.host)
