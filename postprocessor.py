import re
from PIL import Image
import pytesseract

class ProcessingResult:
    success: bool
    result: str

    def __init__(self, success,result):
        self.success = success
        self.result = result


class IPostProcessor:
    def process(self, data: str) -> ProcessingResult:
        return ProcessingResult(False, "")


class FilterPostProcessor(IPostProcessor):
    search_string: str 

    def __init__(self, search_string: str):
        self.search_string = search_string

    def process(self, data: str) -> ProcessingResult:
        matches = re.findall(self.search_string,data)
        if len(matches) == 0:
            return ProcessingResult(False, data)
          
        else:
            matches = list(set(matches))
            combined = ', '.join(matches)
            return ProcessingResult(True, combined)


class OCRPostProcessor(IPostProcessor):
    def __init__(self, tesseract_path: str) -> None:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def process(self, data: str) -> ProcessingResult:
        text = ""
        for image_fn in data.split("$"):
            text +=  pytesseract.image_to_string(Image.open(image_fn)) + "\n"
        return ProcessingResult(len(text.strip()) > 0, text.strip())
