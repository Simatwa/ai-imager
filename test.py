from ai_imager import web_interface as web
from os import getcwd, path

if __name__ == "__main__":
    web.app_data_dir = path.join(getcwd(), "contents")
    #web.API(host=True)
    web.start_server()
