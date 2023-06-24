import os
import shutil

class Plugin:
    name: str
    output_path: str
    
    def __init__(self) -> None:
        self.output_path = f'/tmp/octo/{self.name}'
        self.ensure_output_path()
        
    def run(self, filename) -> str:
        return ''

    def ensure_output_path(self) -> None:
        if os.path.exists(self.output_path):
            shutil.rmtree(self.output_path)
        os.makedirs(self.output_path, exist_ok=False)
