import flet as ft       

lista = []

def main(pagina: ft.Page):
    def adicionar_tarefa(event):
        tarefa = tarefa_input.value
        if tarefa:
            lista.append(tarefa)
            tarefa_input.value = ""
            atualizar_lista()
            pagina.update()

    def atualizar_lista():
        lista_tarefas.controls.clear()
        for tarefa in lista:
            lista_tarefas.controls.append(ft.Text(tarefa))
        pagina.update()

    titulo = ft.Text("Lista de Tarefas", size=30)
    pagina.add(titulo)

    tarefa_input = ft.TextField(hint_text="Digite uma tarefa")
    pagina.add(tarefa_input)

    adicionar_botao = ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa)
    pagina.add(adicionar_botao)

    lista_tarefas = ft.Column()
    pagina.add(lista_tarefas)

    atualizar_lista()

ft.app(target=main)
