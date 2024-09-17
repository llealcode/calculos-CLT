import flet as ft
from components.components import CalcButton
from components.components import CampoTxt
from components.components import Headers
from components.components import Alert
from components.components import OptionButton
from components.components import HomePageMessage


class ViewHome(ft.Container):

    def __init__(self, page):

        self.resultado = Alert()
        self.mensagem = HomePageMessage()
        self.horas = OptionButton(texto='Horas extras', icone=ft.icons.TIMER_ROUNDED, rota="/horas", page=page)
        self.ferias = OptionButton(texto='Férias', icone=ft.icons.BEACH_ACCESS_ROUNDED, rota="/ferias", page=page)
        self.rescisao = OptionButton(texto='Rescisão', icone=ft.icons.POWER_OFF_ROUNDED, rota="/rescisao", page=page)
        self.decimo_terceiro = OptionButton(texto='Décimo terceiro', icone=ft.icons.MONETIZATION_ON_ROUNDED, rota="decimo_terceiro", page=page)
        self.adicional_noturno = OptionButton(texto='Adicional Noturno', icone=ft.icons.MODE_NIGHT, rota="adiciona_noturno", page=page)

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[Headers(texto='Bem-vindo!', tipo='Título')], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(content=self.mensagem, margin=ft.margin.only(top=40)),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                self.horas,
                                self.ferias,
                                self.rescisao,
                                self.decimo_terceiro,
                                self.adicional_noturno
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20
                        ),
                        margin=ft.margin.only(top=20)
                    ),
                    ft.Row(controls=[ft.Container(content=self.resultado, margin=ft.margin.only(top=50))], alignment=ft.MainAxisAlignment.CENTER)
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.with_opacity(opacity=0.10, color=ft.colors.WHITE12),
            padding=ft.padding.symmetric(vertical=10, horizontal=20),
            height=page.height*0.88
        )
