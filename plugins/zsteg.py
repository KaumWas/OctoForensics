from plugin import Plugin
from helpers import Helpers

class ZstegPlugin(Plugin):
    name = "zsteg"

    def run(self,filename):
        return Helpers.run_linux_command(f'zsteg -q -s all \"{filename}\"')
    

