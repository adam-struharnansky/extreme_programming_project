import pygame.event


from source.front_end import CheckBox


class CheckboxGroup:
    def __init__(self):
        self._checkboxes: list[CheckBox] = []
    
    def add(self, checkbox: CheckBox) -> None:
        self._checkboxes.append(checkbox)
        checkbox.checkbox_group = self

    def uncheck_others(self, primary_checkbox: CheckBox) -> None:
        for checkbox in self._checkboxes:
            if checkbox != primary_checkbox:
                checkbox.is_checked = False

    def handle_event(self, event: pygame.event.Event) -> None:
        for checkbox in self._checkboxes:
            checkbox.handle_event(event)

    def get_value(self) -> any:
        for checkbox in self._checkboxes:
            if checkbox.is_checked:
                return checkbox.option
        return None

    def draw_checkbox_group(self) -> None:
        for checkbox in self._checkboxes:
            checkbox.draw_check_box()
