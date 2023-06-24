from plugin import Plugin
from helpers import Helpers
import os

class ForemostPlugin(Plugin):
    name = "foremost"
    
    def run(self, filename: str) -> str:
        Helpers.run_linux_command(f'foremost -Q -i \"{filename}\" -v', cwd=self.output_path)
        
        output_path = f"{self.output_path}/output"
        output = os.listdir(output_path)
        out_dirs = [fn for fn in output if os.path.isdir(f"{output_path}/{fn}")]

        for filetype in out_dirs:
            if filetype in ['png', 'jpeg', 'jpg', 'gif']:
                image_files = [f"{output_path}/{filetype}/{x}" for x in os.listdir(f"{output_path}/{filetype}")]
                return f"$$$OCR$$${'$'.join(image_files)}"
            if filetype in 'txt':
                return Helpers.run_linux_command(f'cat {output_path}/{filetype}/*', cwd=self.output_path)
        
        return ""
