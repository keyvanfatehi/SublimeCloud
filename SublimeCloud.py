import sublime, sublime_plugin
import subprocess
import os
import re

class SublimeCloud(object):
  def shellcmd(self, arr):
    prev_dir = os.getcwd()
    os.chdir(self.userdir())
    proc = subprocess.Popen(arr, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    os.chdir(prev_dir)
    return proc.stdout.read()

  def userdir(self):
    return os.path.join(sublime.packages_path(), 'User')

  def check_userdir_is_repo(self):
    output = self.shellcmd(['git', 'status'])
    goodmsg = re.compile('On branch master')
    print os.getcwd()
    return True if goodmsg.search(output) else False

  def remote_uri(self):
    settings = self.view.settings()
    key = "sublime_cloud_git"
    if settings.has(key):
        output = settings.get(key)
    else:
        output = 'Add "sublime_cloud_git" to your settings!'

  def push(self):
    pass

  def pull(self):
    pass

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    self.view.insert(edit, 0, output)

class SublimeCloudPush(sublime_plugin.ApplicationCommand):
  def run(self):
    print SublimeCloud().check_userdir_is_repo()

class SublimeCloudPull(sublime_plugin.ApplicationCommand):
  def run(self):
    pass
