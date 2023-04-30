import subprocess

class Helpers:
    @staticmethod
    def run_linux_command(command:str):
        proc = subprocess.Popen('wsl.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        stdout, stderr = proc.communicate(bytes(command, "utf8"))
        output = str(stdout, "utf8")
        return output

    @staticmethod
    def get_filetype(filename):
        output = Helpers.run_linux_command(f"file {filename}")
        output = output[len(filename)+2:]
        output = output.strip()
        output = output.split(",")
        output = output[0]
        return output

if __name__ == '__main__':
    print(Helpers.get_filetype("main.py"))
    print(Helpers.get_filetype("testing/test.jpeg"))
