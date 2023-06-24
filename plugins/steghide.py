from plugin import Plugin
from helpers import Helpers

class SteghidePlugin(Plugin):
    name = "steghide"

    def run(self, filename):
        args = [
            "--quiet",
            "--force",
            "--passphrase \"\""
        ]

        command = f"steghide extract {' '.join(args)} --stegofile \"{filename}\""
        Helpers.run_linux_command(command, cwd=self.output_path)
        output = Helpers.run_linux_command(f'cat *', cwd=self.output_path)
        return output
