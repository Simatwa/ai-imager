from flask import *
from . import app_data_dir,logging,getExc
from . import error_handler as exception_handler
from os import path
class config:
    def __init__(self):
        self.auth_cookie_key = "openai_api_key"

    def get_path(self,*args):
        return path.join(app_data_dir,"/".join(args))

    @exception_handler
    def get_cookie(self,key):
        """Gets cookie from user
        Args:
            key (_type_): Cookie name

        Returns:
            str|None: Value | None
        """
        return request.cookies.get(key)

    @exception_handler()
    def get_from_form(self,key:str):
        return request.form.get(key)

class API(Flask,config):
    """Main web interface 
    """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.route("/")(self.index)
        self.route("/image/v1",methods=["POST"])(self.imager)
        self.route("/image/v1/prompt",methods=["POST"])(self.create_from_prompt)
        self.route("/image/v1/mask",methods=["POST"])(self.edit_with_mask)
        self.route("/image/v1/variation",methods=["POST"])(self.get_variation)

    #@app.route("/")
    def index(self):
        """Landing page"""
        #return render_template('index.html')
        if self.get_cookie(self.auth_cookie_key):
            resp = render_template("index.html")
        else:
            resp = render_template("login_pop.html")
        return resp

    #@app.route("/image/v1",methods=["POST"])
    def imager(self):
        """Handle v1 routings"""
        action = self.get_from_form('action')#create
        if action in ('create_from_prompt'):
            resp = 'create_from_prompt'
        elif action in ("edit_with_mask"):
            resp = 'edit_with_mask'
        else:
            resp = 'get_variation'
        return redirect(url_for(resp))

    #@app.route("/image/v1/prompt",methods=["POST"])
    def create_from_prompt(self):
        """Generate image from text"""
        pass

    #@app.route("/image/v1/mask",methods=["POST"])
    def edit_with_mask(self):
        """Edit image with mask"""
        pass

    #@app.route("/image/v1/variation",methods=["POST"])
    def get_variation(self):
        """Get another image like same """
        pass


def main():
    configs=config()
    app=API(
        __name__,
        template_folder="/home/smartwa/git/ai-imager/static/templates",#configs.get_path("static","template"),
        static_folder="/home/smartwa/git/ai-imager/static"#config.get_path("static")
    )
    app.run(port=8000,debug=True)

if __name__=="__main__":
    main()