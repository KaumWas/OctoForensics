from plugin import Plugin
from helpers import Helpers

class ExiftoolPlugin(Plugin):
    name = "exiftool"

    def run(self,filename):
        result = Helpers.run_linux_command(f'exiftool \"{filename}\"')
        return result