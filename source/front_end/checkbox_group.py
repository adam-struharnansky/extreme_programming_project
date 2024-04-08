
class CheckboxGroup:
    def __init__(self):
        self._checkboxes = []
    
    def add(self, checkbox):
        self._checkboxes.append(checkbox)
        checkbox.group = self
        
    def handle_event(self, event, checkbox):  # todo: Preco je ako parameter event?
        # If a checkbox is clicked, uncheck all others in the group
        if checkbox.is_checked:
            for cb in self._checkboxes:
                if cb != checkbox:
                    cb.is_checked = False
