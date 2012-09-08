import sublime, sublime_plugin

from urllib import urlopen
import json

class SublimeCloudSettings
  def __init__(self)
    settings_file = open(os.path.expanduser('~/.sublime_cloud'))
    data = json.load(json_data)
    settings_file.close()
    self.repo = data["github_repository"]

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")

class GoogleAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        elements = ET.parse(
                        urlopen(GOOGLE_AC % prefix)
                    ).getroot().findall("./CompleteSuggestion/suggestion")

        sugs = [(x.attrib["data"],) * 2 for x in elements]

        return sugs
