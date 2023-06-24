from __future__ import annotations
from typing import Optional

import subprocess

class Helpers:
    @staticmethod
    def run_linux_command(command: str, cwd: Optional[str] = None):
        proc = subprocess.Popen('wsl.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = cwd)
        stdout, stderr = proc.communicate(bytes(command, "utf8"))
        output = str(stdout, "utf8")
        return output

    @staticmethod
    def get_filetype(filename):
        cmd = f"file \"{filename}\""
        output = Helpers.run_linux_command(cmd)
        output = output[len(filename)+2:]
        output = output.strip()
        output = output.split(",")
        output = output[0]
        return output

if __name__ == '__main__':
    print(Helpers.get_filetype("main.py"))
    print(Helpers.get_filetype("testing/test.jpeg"))
