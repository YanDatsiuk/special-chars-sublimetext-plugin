import sublime
import sublime_plugin


class EscapeAngleBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		#get content of a current opened file
		content = self.view.substr(sublime.Region(0, self.view.size()))

		#replace angle brackets
		content = content.replace("<", "&lt;")
		content = content.replace(">", "&gt;")

		#apply changes in the opened file
		self.view.replace(edit, sublime.Region(0, self.view.size()), content)