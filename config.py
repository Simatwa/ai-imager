from ai_imager import app_data_dir, error_handler, path
from shutil import copytree


@error_handler()
def install_web_files():
    """Copies the web contents to app's directory"""
    copytree("contents", path.join(app_data_dir, "contents"), dirs_exist_ok=True)


if __name__ == "__main__":
    install_web_files()
