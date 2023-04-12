from . import logging, getExc, error_handler, openai
from io import BytesIO
from PIL import Image


class openai_handler:
    def __init__(self):
        pass

    def format_response(self,response:dict,action:str='PROMPT') -> list:
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
        return self.format_response(openai.Image.create(prompt=prompt, n=int(total_images), size=image_size))

    @error_handler()
    def create_edit(
        self,
        original_image_path: str,
        masked_image_path: str,
        prompt: str,
        total_images: int = 1,
        image_size: str = "512x512",
    ) -> list | str:
        """Edit image based on a reference image

        Args:
            original_image_path (str): Path to Image to original image
            masked_image_path (str): Path to Image to act as mask
            prompt (str): Description of action to be performed
            total_images (int, optional): Amount of Images to be generated. Defaults to 1.
            size (str, optional): Image resolution from [`256x256`, `512x512`, `1024x1024`]. Defaults to "512x512".
        """
        response = openai.Image.create_edit(
            image=self._get_image_bytes(original_image_path),
            mask=self._get_image_bytes(masked_image_path),
            prompt=prompt,
            n=int(total_images),
            size=image_size,
        )
        return self.format_response(response,'EDIT')

    @error_handler()
    def create_variation(
        self, path_to_image: str, total_images: int = 1, image_size: str = "512x512"
    ) -> list | str:
        response = openai.Image.create_variation(
            image=self._get_image_bytes(path_to_image),
            n=int(total_images),
            size=image_size,
        )
        
        return self.format_response(response,'VARIATION')

    def _get_image_bytes(
        self, path_to_image: str, image_resolution: int = 512
    ) -> bytes:
        """Get bytes of a squared mage file

        Args:
            path_to_image (str): Path to Image to be handled
            image_resolution (int, optional): Resolution of the image to be squared. Defaults to 512.
        """
        # Read the image file from disk and resize it
        image = Image.open(path_to_image)
        image = image.resize((image_resolution) * 2)
        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format="PNG")
        return byte_stream.getvalue()
