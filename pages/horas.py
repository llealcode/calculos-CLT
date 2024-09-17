import flet as ft
from components.components import CampoTxt
from components.components import BottomBar

class ViewHoras(ft.Container):

    def __init__(self, page):

        super().__init__(
            content=ft.Column(
                controls=[
                    CampoTxt(texto="Salário base"),
                    CampoTxt(texto="Jornada"),
                    CampoTxt(texto="Horas trabalhadas"),
                    CampoTxt(texto="Taxa adicional"),
                    ft.ElevatedButton("Voltar", on_click=lambda _: self.page.go("/")),
                    BottomBar(page=page)
                ]
            )
        )