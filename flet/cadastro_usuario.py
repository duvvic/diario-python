import flet as ft 

lista_usuarios = []

def main(pagina:ft.Page):
    def cadastrar_usuario(event):

        valor_nome = nome.value
        lista_usuarios.append(valor_nome)
        
        resultados.value = lista_usuarios
        nome.value = ""


        pagina.add(ft.Text(f"Usuário {valor_nome} Cadastrado com sucesso!"))
       
        pagina.update()

    def listar_usuarios(event):
        resultados.value = ""
        
        for usuario in lista_usuarios:
            user = ft.Text(usuario)
            pagina.add(ft.Text(user.value))
            resultados.value = user.value 
        pagina.update()




    titulo = ft.Text("Formulário de Cadastro",size=50)
    pagina.add(titulo)

    nome = ft.TextField(hint_text="Digite seu nome:")
    pagina.add(nome)

    cadastrar = ft.ElevatedButton("Cadastrar",on_click=cadastrar_usuario)       
    pagina.add(cadastrar)
    
    listar = ft.ElevatedButton("listar usuários",on_click=listar_usuarios)   
    pagina.add(listar)

    
    resultados = ft.Text()
    pagina.add(resultados)
    
ft.app(target=main)