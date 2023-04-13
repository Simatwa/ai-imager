from ai_imager import app_data_dir,error_handler
from shutil import copytree
@error_handler()
def install_web_files():
    """Copies the web contents to app's directory
    """
    copytree('contents',app_data_dir)
if __name__=='__main__':
    print(app_data_dir)
    install_web_files()
