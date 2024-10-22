import flet as ft

def main(page: ft.Page):
    
    # Configuración inicial de la ventana
    page.window_width = 600
    page.window_height = 400 
    page.title = "Lista para Supermercado" # Titulo principal de arriba en la aplicacion
    
    tasks = []  # Lista para almacenar las tareas
    
    # Mostrar mensaje de bienvenida al cargar la página
    def show_welcome_message():
        page.snack_bar = ft.SnackBar(ft.Text("¡Bienvenido Jose Oviedo!"), open=True)
        page.update()
    
    # Función para añadir tarea
    def add_task(e):
        if new_task.value.strip() != "":  # Si hay contenido en el campo de texto
            new_checkbox = ft.Checkbox(label=new_task.value)  # Crear un checkbox con la tarea
            tasks.append(new_checkbox)  # Agregarlo a la lista de tareas
            task_list.controls.append(new_checkbox)  # Mostrarlo en la página
            new_task.value = ""  # Limpiar el campo de texto
            new_task.focus()  # Enfocar de nuevo
            page.update()  # Actualizar la página
    
    # Función para eliminar la tarea seleccionada
    def delete_task(e):
        for task in tasks:
            if task.value:  # Si el checkbox está seleccionado
                tasks.remove(task)  # Eliminar de la lista de tareas
                task_list.controls.remove(task)  # Eliminar de la interfaz
                new_task.value = ""  # Limpiar el campo de texto
                page.update()  # Actualizar la página
                break

    # Encabezado y logo
    logo = ft.Image(src=r"../img/cochino.png", width=125, height=125)  # Ruta absoluta
    header_text = ft.Text("Lista de Compras", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    header_welcome = ft.Text("Estamos listos para anotar", size=15, text_align=ft.TextAlign.CENTER)
    
    header = ft.Column(
        [logo, header_text, header_welcome],
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    )
    centered_header = ft.Container(
        content=header,
        alignment=ft.alignment.center  
    )
    
    # Campo de texto para escribir tareas
    new_task = ft.TextField(hint_text="¿Cuales son las compras pendientes?", width=300)
    
    # Contenedor donde se mostrarán las tareas
    task_list = ft.Column()  # Columna que contendrá las tareas en formato Checkbox
    
    # Botones
    add_button = ft.ElevatedButton("Agregar", on_click=add_task)
    delete_button = ft.ElevatedButton("Eliminar", on_click=delete_task)
    
    # Contenido de la página
    page.add(
        centered_header,
        ft.Divider(height=20),
        ft.Row([new_task, add_button, delete_button], alignment=ft.MainAxisAlignment.CENTER),
        task_list  # Aquí aparecerán las tareas
    )
    
    # Llamar a la función para mostrar el mensaje de bienvenida
    show_welcome_message()

ft.app(main)
