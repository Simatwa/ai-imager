from . import logging, getExc, error_handler, openai
from io import BytesIO
from PIL import Image
import contextlib
import json
from .bing import ImageGen
from math import ceil


class openai_handler:
    def __init__(self, args: object):
        self.U = self.setup_bing(args)
        self.bing = ImageGen(self.U, quiet=True)

    @error_handler()
    def setup_bing(self, args):
        """Get cookie value"""
        if not args.cookie_file:
            return
        with contextlib.suppress(Exception):
            with open(args.cookie_file, encoding="utf-8") as file:
                cookie_json = json.load(file)
                for cookie in cookie_json:
                    if cookie.get("name") == "_U":
                        return cookie.get("value")
        raise Exception("Cookie-file can't be found from " + args.cookie_file)

    def format_response(self, response: dict, action: str = "PROMPT") -> list:
        resp = []
        for value in response["data"]:
            resp.append(value["url"])
        logging.debug(f"{action} : Response received : {resp}")
        return resp

    @error_handler()
    def create_from_prompt(
        self, prompt: str, total_images: int = 2, image_size: str = "512x512"
    ):
        """Create Image based on description

        Args:
            prompt (str): Description of the desired image
            total_images (int, optional): Images to be generated. Defaults to 1.
            image_size (str, optional): Resolution of image from [`256x256`, `512x512`, `1024x1024`] . Defaults to "512x512".

        Returns:
            list|str: List of urls or error report
        """
        return self.format_response(
            openai.Image.create(prompt=prompt, n=int(total_images), size=image_size)
        )

    @error_handler()
    def create_edit(
        self,
        original_image_path: str,
        masked_image_path: str,
        prompt: str,
        total_images: int = 1,
        image_size: str = "512x512",
        path_to_image=None,
    ) -> list:
        """Edit image based on a reference image

        Args:
            original_image_path (str): Path to Image to original image
            masked_image_path (str): Path to Image to act as mask
            prompt (str): Description of action to be performed
            total_images (int, optional): Amount of Images to be generated. Defaults to 1.
            size (str, optional): Image resolution from [`256x256`, `512x512`, `1024x1024`]. Defaults to "512x512".
        """
        response = openai.Image.create_edit(
            image=self._get_image_bytes(original_image_path, no_mods=True),
            mask=self._get_image_bytes(masked_image_path, no_mods=True),
            prompt=prompt,
            n=int(total_images),
            size=image_size,
        )
        return self.format_response(response, "EDIT")

    @error_handler()
    def create_variation(
        self, path_to_image: str, total_images: int = 1, image_size: str = "512x512"
    ) -> list:
        response = openai.Image.create_variation(
            image=self._get_image_bytes(path_to_image),
            n=int(total_images),
            size=image_size,
        )

        return self.format_response(response, "VARIATION")

    @error_handler()
    def create_with_bing(self, prompt: str, total_images: int = 2,image_size:str=None) -> list:
        resp = []
        total_images = int(total_images)
        for x in range(ceil(total_images / 4)):
            resp.extend(self.bing.get_images(prompt))
        if len(resp) > total_images:
            resp = resp[0:total_images]
        return resp

    def _get_image_bytes(
        self, path_to_image: str, image_resolution: int = 512, no_mods: bool = False
    ) -> bytes:
        """Get bytes of a squared mage file

        Args:
            path_to_image (str): Path to Image to be handled
            image_resolution (int, optional): Resolution of the image to be squared. Defaults to 512.
        """
        # Read the image file from disk and resize it
        if no_mods:
            return open(path_to_image, "r+b")
        image = Image.open(path_to_image)
        image = image.resize((image_resolution, image_resolution))
        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format="PNG")
        return byte_stream.getvalue()
