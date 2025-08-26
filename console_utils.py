import subprocess
import os
import sys

from vendor.pythonutils.enities.command_response import CommandResponse

# Fix import system_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from system_utils import *
from generic_utils import str_is_empty
from enities.command_info import CommandInfo
from file_utils import is_file, is_dir

class ConsoleUtils:
    def __log_command(self, command_info: CommandInfo):
        if command_info is not None and command_info.verbose:
            print(">>> " + command_info.command)

    def exec_real_time(self, command_info: CommandInfo):
        self.__log_command(command_info)
        if command_info.use_shell:
            if is_windows():
                subprocess.run(["powershell", "-Command", command_info.command], env=command_info.env, cwd=command_info.cwd)
            else:
                subprocess.run(command_info.command, shell=True, env=command_info.env, cwd=command_info.cwd)
        else:
            if is_windows():
                subprocess.run(command_info.command, shell=True, env=command_info.env, cwd=command_info.cwd)
            else:
                subprocess.run(command_info.command, env=command_info.env, cwd=command_info.cwd)

    def exec(self, command_info: CommandInfo) -> CommandResponse:
        self.__log_command(command_info)
        output = None
        if command_info.use_shell:
            if is_windows():
                output = subprocess.run(["powershell", "-Command", command_info.command], env=command_info.env, capture_output=True, text=True, cwd=command_info.cwd)
            else:
                cmd = ["bash", "-c", command_info.command]
                if is_file(command_info.command):
                    cmd = ["bash", command_info.command]
                output = subprocess.run(cmd, env=command_info.env, capture_output=True, text=True, cwd=command_info.cwd)
        else:
            if is_windows():
                output = subprocess.run(command_info.command, shell=True, env=command_info.env, capture_output=True, text=True, cwd=command_info.cwd)
            else:
                output = subprocess.run(command_info.command, env=command_info.env, capture_output=True, text=True, cwd=command_info.cwd)

        response = CommandResponse()
        if output is not None:
            response = CommandResponse(output.stdout.strip(), output.stderr.strip(), output.returncode)
        return response

    def pause(self, message: str = ''):
        if str_is_empty(message):
            message = "Press Enter to continue..."
        input(message)
