import sublime, sublime_plugin
import re
import urllib.request

a = re.compile("^10\\..+\/.+$")

class doi2bibCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()
        for sel in sels:
            if a.match(self.view.substr(sel)):
                url = "http://dx.doi.org/"+self.view.substr(sel)
                req = urllib.request.Request(url)
                req.add_header('Accept', 'application/x-bibtex; charset=utf-8')
                r = urllib.request.urlopen(req)
                self.view.replace(edit, sel, r.read().decode('utf-8'))