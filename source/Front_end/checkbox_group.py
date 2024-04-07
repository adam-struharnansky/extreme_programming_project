
class CheckboxGroup:
    def __init__(self):
        self.checkboxes = []
    
    def add(self, checkbox):
        self.checkboxes.append(checkbox)
        checkbox.group = self
        
    def handle_event(self, event, checkbox):
        # If a checkbox is clicked, uncheck all others in the group
        if checkbox.is_checked:
            for cb in self.checkboxes:
                if cb != checkbox:
                    cb.is_checked = False