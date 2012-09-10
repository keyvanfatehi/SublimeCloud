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

  def ensure_userdir_is_repo(self):
    output = self.shellcmd(['git', 'status'])
    if not re.compile('On branch master').search(output):
      self.shellcmd(['git', 'init'])
      uri = self.remote_uri()
      if uri:
        self.shellcmd(['git', 'remote', 'add', 'origin', uri])

  def remote_uri(self):
    settings = sublime.load_settings("Preferences.sublime-settings")
    key = "sublime_cloud_git"
    if settings.has(key):
        return settings.get(key)
    else:
        sublime.error_message('Define "sublime_cloud_git" in your settings!')
        return None

  def push(self):
    self.ensure_userdir_is_repo()
    uri = self.remote_uri()
    if uri and sublime.ok_cancel_dialog("Push settings to "+uri+"?", "Push!"):
      sublime.status_message("SublimeCloud: pushing settings to "+uri+"...")
      self.shellcmd(['git', 'add', '.'])
      self.shellcmd(['git', 'commit', '-am', '"SublimeCloud Autocommit"'])
      self.shellcmd(['git', 'push', '-f', 'origin', 'master'])
      sublime.status_message("SublimeCloud: push complete!")

  def pull(self):
    self.ensure_userdir_is_repo()
    uri = self.remote_uri()
    if uri and sublime.ok_cancel_dialog("Pull settings from "+uri+"?", "Pull!"):
      sublime.status_message("SublimeCloud: pulling settings from "+uri+"...")
      self.shellcmd(['git', 'fetch', '--all'])
      self.shellcmd(['git', 'reset', '--hard', 'origin/master'])
      self.shellcmd(['git', 'pull', 'origin', 'master'])
      sublime.status_message("SublimeCloud: pull complete!")

class SublimeCloudPush(sublime_plugin.ApplicationCommand):
  def run(self):
    SublimeCloud().push()

class SublimeCloudPull(sublime_plugin.ApplicationCommand):
  def run(self):
    SublimeCloud().pull()
