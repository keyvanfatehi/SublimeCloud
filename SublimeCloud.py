import sublime, sublime_plugin

from xml.etree import ElementTree as ET
from urllib import urlopen

GITHUB_REPO = r"http://github.com/username/"

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
