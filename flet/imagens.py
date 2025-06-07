import flet as ft

def principal(page: ft.Page):
    page.title="Exemplo de imagem"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    image_url="https://images.app.goo.gl/WmdqsXawBJPjQ6Cd9"
    img=ft.Image(src=image_url, width=300, height=200)

    page.add(img)

ft.app(target=principal)