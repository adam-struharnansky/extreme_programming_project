
class CheckboxGroup:
    def __init__(self):
        self._checkboxes = []
    
    def add(self, checkbox):
        self._checkboxes.append(checkbox)
        checkbox.checkbox_group = self
        
    def handle_checkbox(self, handled_checkbox):
        # If a checkbox is clicked, uncheck all others in the group
        if handled_checkbox.is_checked:
            for checkbox in self._checkboxes:
                if checkbox != handled_checkbox:
                    checkbox.is_checked = False

    def handle_event(self, event):
        for checkbox in self._checkboxes:
            checkbox.handle_event(event)

    def get_value(self):
        for checkbox in self._checkboxes:
            if checkbox.is_checked:
                return checkbox.option
        return None

    def draw(self):
        for checkbox in self._checkboxes:
            checkbox.draw()

    def redraw_boxes(self):
        for checkbox in self._checkboxes:
            checkbox.redraw_box()
