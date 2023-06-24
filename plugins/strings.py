from plugin import Plugin
from helpers import Helpers

class StringsPlugin(Plugin):
    name = "strings"

    def run(self,filename):
        result = Helpers.run_linux_command(f'strings \"{filename}\"')
        return result