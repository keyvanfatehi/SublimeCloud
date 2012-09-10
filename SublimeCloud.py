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
    return True if goodmsg.search(output) else False

  def remote_uri(self):
    settings = sublime.load_settings("Preferences.sublime-settings")
    key = "sublime_cloud_git"
    if settings.has(key):
        return settings.get(key)
    else:
        sublime.error_message('Define "sublime_cloud_git" in your settings!')
        return None

  def push(self):
    self.check_userdir_is_repo()
    print "Ready to push"

  def pull(self):
    self.check_userdir_is_repo()
    print "Ready to pull"

class SublimeCloudPush(sublime_plugin.ApplicationCommand):
  def run(self):
    repo = SublimeCloud().remote_uri()
    SublimeCloud().push() if repo else None

class SublimeCloudPull(sublime_plugin.ApplicationCommand):
  def run(self):
    pass
