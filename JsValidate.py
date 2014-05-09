#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

SETTINGS_FILE = 'JSValidate.sublime-settings'

class JsvalidateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings(SETTINGS_FILE)
    cmd = settings.get('esvalidate', 'esvalidate')

    filepath = self.view.file_name()
    packages = sublime.packages_path()
    args = {
      "cmd": [
        cmd,
        "--format=sublime",
        filepath
      ],
      'line_regex': settings.get('line_regex', r"(\d+),(\d+): (.*)$"),
      'file_regex': settings.get('file_regex', r"esvalidate: (.+)\]")
    }

    if sublime.platform() == "windows":
      args['cmd'][0] += ".cmd"
    elif sublime.platform() == "osx":
      args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"

    self.view.window().run_command('exec', args)


class JsvalidateOnSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    settings = sublime.load_settings(SETTINGS_FILE)
    if settings.get('run_on_save', False) == False:
      print 'false'
      return
    if re.search(settings.get('filename_filter'), view.file_name()):
      print 'true'
      view.window().run_command("jsvalidate")
      return

    print 'else'

