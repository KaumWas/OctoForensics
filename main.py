from __future__ import annotations
from typing import Dict, List

import os

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from helpers import Helpers

from plugin import Plugin
from plugins.strings import StringsPlugin
from plugins.exiftool import ExiftoolPlugin
from plugins.zsteg import ZstegPlugin
from plugins.foremost import ForemostPlugin
from plugins.steghide import SteghidePlugin

from postprocessor import IPostProcessor, FilterPostProcessor, OCRPostProcessor

from commandline import OctoArgs, CommandLine

class OctoForensics:
    args: OctoArgs

    def __init__(self, args: OctoArgs) -> None:
        self.args = args

        colorama_init()

    def get_filetype(self):
        filetype = Helpers.get_filetype(self.args.path)
        return filetype
    
    def get_plugins_for_filetype(self, filetype: str) -> List[Plugin]:
        filetype_plugins: Dict[str, List[Plugin]] = {
            "JPEG image data": [
                StringsPlugin(),
                ExiftoolPlugin(),
                ZstegPlugin(),
                ForemostPlugin(),
                SteghidePlugin()
            ],
            "PNG image data": [
                StringsPlugin(),
                ZstegPlugin(),
                ForemostPlugin()
            ]
        }
        
        return filetype_plugins[filetype]


    def start(self):
        filetype = self.get_filetype()
        print(f"Analyzing: {os.path.basename(self.args.path)}")
        print(f"Filetype: {filetype}\n")
        plugins_to_run = self.get_plugins_for_filetype(filetype)
        for plugin in plugins_to_run:
            print(f"{Fore.CYAN}Running {plugin.name}.. {Fore.RESET}")
            plugin_result = plugin.run(self.args.path)
            
            if plugin_result.startswith("$$$OCR$$$"):
                plugin_result = plugin_result.replace("$$$OCR$$$", "")
                post_processor: IPostProcessor = OCRPostProcessor("C:\\Program Files\\Tesseract-OCR\\tesseract.exe")
            else:
                post_processor: IPostProcessor = FilterPostProcessor(self.args.filter)
            
            search_result = post_processor.process(plugin_result)
            if search_result.success == True:
                print(f" > {Fore.GREEN}{search_result.result} {Fore.RESET}")
            else:
                print(f" > {Style.DIM}No results found. Output written to {plugin.output_path} {Style.RESET_ALL}")
                f = open(plugin.output_path + "/output.txt", "w")
                f.write(plugin_result)
                f.close()

if __name__ == '__main__':
    cmd = CommandLine()
    args = cmd.parse()

    app = OctoForensics(args)
    app.start()
