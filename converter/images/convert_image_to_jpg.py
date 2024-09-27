from PIL import Image
import os
import logging
import io
from typing import Union

# Setting up logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)


def convert_image_to_jpg(
    input_data: Union[str, bytes, Image.Image],
    output_path: str,
    quality: int = 85,
    return_image: bool = False,
    overwrite: bool = False,
) -> Union[Image.Image, None]:
    """Converts an image to JPG format with specified quality.

    Arguments:
        input_data: Path to the input image (string), binary data (bytes), or PIL.Image object.
        output_path: Path for saving the converted image.
        quality: Quality of the output image (0-100).
        return_image: If True, returns the PIL.Image object.
        overwrite: If True, overwrites the existing file.

    Returns:
        PIL.Image.Image: The converted image (if return_image=True).
    """

    # Handling different types of input data
    if isinstance(input_data, bytes):
        # If binary data is provided, create an Image object
        image = Image.open(io.BytesIO(input_data))
    elif isinstance(input_data, Image.Image):
        # If a PIL.Image object is provided
        image = input_data
    elif isinstance(input_data, str):
        # If a file path is provided
        if not os.path.isfile(input_data):
            logging.error(f"File not found: {input_data}")
            raise FileNotFoundError(f"File not found: {input_data}")
        image = Image.open(input_data)
    else:
        logging.error(
            "Invalid type for input_data. Must be str, bytes, or PIL.Image object."
        )
        raise TypeError("Invalid type for input_data.")

    # Check the format and save the image
    _, input_extension = os.path.splitext(output_path)
    input_extension = input_extension.lower()

    if input_extension in ['.jpg', '.jpeg']:
        logging.info(
            f"File {output_path} is already in JPG format. Copying..."
        )
        if not overwrite and os.path.exists(output_path):
            logging.error(
                f"File {output_path} already exists. Set overwrite=True to overwrite."
            )
            raise FileExistsError(f"File {output_path} already exists.")

        image.save(output_path, "JPEG", quality=quality)
        return image if return_image else None

    logging.info(f"Converting to {output_path}...")
    try:
        image = image.convert("RGB")
        image.save(output_path, "JPEG", quality=quality)
        logging.info(f"Conversion completed: {output_path}")
        return image if return_image else None
    except Exception as e:
        logging.error(f"Error during conversion: {e}")
