
class CheckboxGroup:
    def __init__(self):
        self._checkboxes = []
    
    def add(self, checkbox):
        self._checkboxes.append(checkbox)
        checkbox.checkbox_group = self
        
    def handle_event(self, handled_checkbox):
        # If a checkbox is clicked, uncheck all others in the group
        if handled_checkbox.is_checked:
            for checkbox in self._checkboxes:
                if checkbox != handled_checkbox:
                    checkbox.is_checked = False
