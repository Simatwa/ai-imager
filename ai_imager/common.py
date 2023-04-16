import json
import random
from datetime import datetime
from . import error_handler as exception_handler
from os import path, makedirs


class history:
    def __init__(self, app_data_dir: str):
        self.dir = path.join(app_data_dir, "configs")
        self.create_dir_required = self._create_dir()
        self.get_file_path = lambda cookie: path.join(self.dir, cookie + ".json")

    @exception_handler()
    def _create_dir(self):
        if not path.isdir(self.dir):
            makedirs(self.dir)

    @exception_handler(False,{"data": []})
    def get_contents(self, cookie: str):
        fnm = self.get_file_path(cookie)
        if path.isfile(fnm):
            with open(fnm, encoding="utf-8") as fh:
                return json.load(fh)
        else:
            return {"data": []}

    @exception_handler()
    def add_new(self, prompt: str, category: str, links: list, cookie: str):
        if not cookie:
            return
        current_data = self.get_contents(cookie)
        new_data = [
            {
                "category": category,
                "prompt": prompt,
                "urls": links,
                "time": datetime.today().strftime("%d-%b-%Y %H:%M:%S"),
            }
        ]
        data = {"data": current_data["data"] + new_data}
        with open(self.get_file_path(cookie), "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=4)


class generator:
    def __init__(self):
        self.abc = [0,1,2,3,4,5,6,7,8,9]
        for x in range(65, 91):
            self.abc.append(chr(x))
        for x in range(97, 123):
            self.abc.append(chr(x))

    def new_cookie(self, lenght: int = 14):
        return "".join(random.sample(self.abc, lenght))
