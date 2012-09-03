import sublime, sublime_plugin
from subprocess import Popen as execute
from os import path

class OpenTerminalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        p = execute([
            "gnome-terminal",
            "--working-directory",
            path.dirname(self.view.file_name()),
        ])
