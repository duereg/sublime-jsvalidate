import sublime, sublime_plugin

class JsvalidateCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command('set_build_system', {
      'file': 'Packages/JS Validation using Esprima/JsValidate.sublime-build'
    })
    self.window.run_command('build')
