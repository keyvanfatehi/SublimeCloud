import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = self.view.settings()
    key = "sublime_cloud_git"
    if settings.has(key):
        output = settings.get(key)
    else:
        output = 'Add "sublime_cloud_git" to your settings!'
    self.view.insert(edit, 0, output)
