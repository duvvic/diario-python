import flet as ft

def principal(page: ft.Page):
    # Cria um campo de texto para entrada de dados
    campo_nome = ft.TextField(label="Digite seu nome")

    def mostrar_mensagem(evento):
        # Pegando o nome digitado
        nome = campo_nome.value
        # Criando a mensagem
        mensagem = ft.Text(f"Olá, {nome}!")
        # Adicionando a mensagem à página
        page.add(mensagem)
       
    # Botão para enviar o nome
    botao = ft.ElevatedButton(text="Enviar", on_click=mostrar_mensagem)

    # Adicionar os elementos á pagina
    page.add(campo_nome, botao)

ft.app(target=principal)