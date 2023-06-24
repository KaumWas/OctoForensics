import os
import argparse

from helpers import Helpers

class OctoArgs:
    path: str
    filter: str

    def __init__(self, path: str, filter: str) -> None:
        base_path = Helpers.run_linux_command("pwd")
        self.path = os.path.join(base_path.strip(), path.strip()).replace("\\", "/").replace("//", "/")

        self.filter = filter

class CommandLine:
    def parse(self):
        parser = argparse.ArgumentParser(
            prog='OctoForensics',
            description='A little CTF helper with tentacles.',
            epilog='This tool currently only supports image files.\nFilenames can be deceiving!'
        )
        
        parser.add_argument('filename', help="the path to the file to analyze")
        parser.add_argument('-f', '--format', 
                            help="the flag format to look for (regex)",
                            default='flag{.*?}')

        args = parser.parse_args()
        return OctoArgs(args.filename, args.format)
