import flet as ft

#establesemos los parametros principales de la app
def main(page: ft.page):
    page.title = "tablero trello"
    page.padding = 20
    page.theme_mode = "light"
    page.bgcolor = ft.colors.BLUE_GREY_800
    
    # definimos los estilos
    def create_note(text):
        return ft.Container(
            content=ft.TextField(value=text, multiline=True),
            width=200,
            height=200,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius= 10,
            padding= 10,
            
        )
    
    # creamos la grilla
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10
        #horizontal=False,
    )
    
    #creamos la lista
    notes = [
        
        "Nota 1",
        "Nota 2",
        "Nota 3",
       
        
    ]
    
    for note in notes:
        grid.controls.append(create_note(note))
        
    #agregamos el grid a la pagina(pantalla)    
    page.add(grid)
    
    
    
    
    
    


ft.app(target=main)