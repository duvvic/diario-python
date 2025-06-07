import flet as ft

def principal(page: ft.Page):
    checkbox = ft.Checkbox(label='Concorda com os termos"')
    page.add(checkbox)


ft.app(target=principal)