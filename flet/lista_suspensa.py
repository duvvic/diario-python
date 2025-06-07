import flet as ft

def principal(page: ft.Page):
    dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Opção 1"),
            ft.dropdown.Option("Opção 2"),
            ft.dropdown.Option("Opção 3"),
        ]
    )
    page.add(dropdown)

ft.app(target=principal)