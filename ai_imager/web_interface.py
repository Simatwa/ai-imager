from flask import *
from . import app_data_dir,logging,getExc
from . import error_handler as exception_handler
from .imager import openai_handler 
from os import path

app_data_dir='/home/smartwa/git/ai-imager/contents'

class local_config:
    def __init__(self):
        self.auth_cookie_key = "openai_api_key"
        self.upload_path = self.get_path("uploads")
        self.incomplete_form_msg="Kindly fill all the fields"

    def get_path(self,*args):
        return path.join(app_data_dir,"/".join(args))

    @classmethod
    def get_cookie(self,key):
        """Gets cookie from user
        Args:
            key (_type_): Cookie name

        Returns:
            str|None: Value | None
        """
        return request.cookies.get(key)

    @classmethod
    def get_from_form(self,*keys,resp:dict={}):
        for key in keys:
            resp[key]=request.form.get(key)
        return
    
    @classmethod
    def get_from_file(self,*keys,resp:dict={}):
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
                filepath = path.join(self.upload_path,file.filename)
                file.save(filepath)
                resp[key]=filepath
            else:
                resp[key]=None
        return resp

    @classmethod
    def format_response(self,resp:str|list,http_code:int=200,error:bool=None):
        """Format response to be handled by API

        Args:
            resp (str | list): Response
            error (bool, optional): Specifies to handle resp as error . Defaults to False.

        Returns:
            json: Respnse formatted for API
        """
        if not isinstance(resp,list):
            error = True
            http_code = 501 if http_code == 200 else http_code
        api_data = {
            'url':resp if not error else None,
            'error':None if not error else resp,
        }

        return jsonify(api_data),http_code

    @classmethod
    def imager_error_handler(self):
        """Exception handler at API level
        """
        def decorator(func):
            def main(*args,**kwargs):
                try:
                    return func(*args,**args)
                except Exception as e:
                    return self.format_response(getExc(e))
            return main
        return decorator

def API(port:int=8000,debug:bool=True,host:bool|str=False):
    """Start the web app

    Args:
        port (int, optional): Port for web to listen. Defaults to 8000.
        debug (bool, optional): Start the app in debug mode. Defaults to True.
        host (bool | str, optional): Host the web on LAN. Defaults to False.

    Returns:
        None: None
    """
    api_config=local_config()
    openai = openai_handler()
    app=Flask(
        __name__,
        static_folder=api_config.get_path('static'),
        template_folder=api_config.get_path("templates")
    )
    @app.route("/")
    def index():
        """Landing page"""
        return render_template('index.html')

    @app.route("/v1/image/<action>",methods=["GET"])
    def imager(self,action):
        """Handle v1 routings"""
        return render_template('form.html',category=action)

    @app.route("/v1/image/prompt/generate",methods=["POST"])
    #@local_config.imager_error_handler()
    def create_from_prompt(self):
        """Generate image from text"""
        form_data = local_config.get_from_form('prompt',"total_images","image_size")
        if all(list(form_data.values())):
            resp = openai.create_from_prompt(**form_data)
            resp = local_config.format_response(resp)
        else:
            return local_config.format_response(api_config.incomplete_form_msg,http_code=400)

    @app.route("/v1/image/mask/generate",methods=["POST"])
    #@local_config.imager_error_handler()
    def edit_with_mask(self):
        """Edit image with mask"""
        files = local_config.get_from_file("original_image_path","masked_image_path")
        texts = local_config.get_from_form("prompt","total_images","image_size")
        files.update(texts)
        if all(list(files.values())):
            return openai.create_edit(**files)
        else:
            return api_config.format_response(api_config.incomplete_form_msg,http_code=400)

    @app.route("/v1/image/variation/generate",methods=["POST"])
    #@local_config.imager_error_handler()
    def get_variation(self):
        """Get another image like same """
        files = local_config.get_from_file("path_to_image")
        texts = local_config.get_from_form("total_images","image_size")
        files.update(texts)
        if all(list(files.values())):
            return openai.create_variation(**files)
        else:
            api_config.format_response(api_config.incomplete_form_msg,http_code=400)
        
    launch_configs = {
        "port":port,
        "debug":debug,
        }
    if host:
        launch_configs["host"]="0.0.0.0"

    app.run(**launch_configs)

if __name__=="__main__":
    API()