from helpers import Helpers
from plugins.strings import StringsPlugin

class OctoForensics:
    def get_filetype(self, filename):
        filetype = Helpers.get_filetype(filename)
        return filetype
    
    def get_plugins_for_filetype(self,filetype):
        plugins_to_run = []
        if filetype == "JPEG image data":
            strings_plugin = StringsPlugin()
            plugins_to_run.append(strings_plugin)
        return plugins_to_run


    def start(self, filename):
        filetype = self.get_filetype(filename)
        plugins_to_run = self.get_plugins_for_filetype(filetype)
        for plugin in plugins_to_run:
            print(plugin.name)
            plugin_result = plugin.run(filename)
            print(" >", plugin_result)


if __name__ == '__main__':
    app = OctoForensics()
    app.start("testing/test.jpeg")
