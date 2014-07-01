import sublime
import sublime_plugin
# Source from: https://www.sublimetext.com/forum/viewtopic.php?f=4&t=12967

class GotoPositionCommand(sublime_plugin.WindowCommand):
    def run(self):
        window = self.window
        view = window.active_view()
        self.original_cursors = []
        for cursor in view.sel():
            self.original_cursors.append(cursor)
        window.show_input_panel("Byte Position", "", self.location_update, self.location_update, self.on_cancel)


    def location_update(self, input_text):
        print(input_text)
        window = self.window
        view = window.active_view()
        try:
            location = int(input_text)
        except:
            return

        cursors = view.sel()
        cursors.clear()
        cursors.add(sublime.Region(location, location))
        view.show_at_center(location)

    def on_cancel(self):
        window = self.window
        view = window.active_view()
        view.sel().clear()
        view.sel().add_all(self.original_cursors)
        view.show(view.sel())

