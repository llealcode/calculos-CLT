import flet as ft
from components.components import CalcButton, CampoTxt, Headers, Alert


class ViewHome(ft.Container):

    def __init__(self, page):

        self.resultado = Alert()
        self.salario = CampoTxt(texto='Salário bruto', prefix='R$ ')
        self.jornada = CampoTxt(texto= 'Jornada mensal')
        self.horas = CampoTxt(texto= 'Horas extras')
        self.adicional = CampoTxt(texto= '% adicional', prefix='% ')

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Row(controls=[Headers(texto='Cálculo de hora extra', tipo='Título')]),
                    ft.Row(controls=[Headers(texto='Cálculo de hora extra', tipo='Valor a recebe em extras ao final do mês')]),
                    ft.Container(content=self.salario, margin=ft.margin.only(top=40)),
                    ft.Container(content=self.jornada, margin=ft.margin.only(top=20)),
                    ft.Container(content=self.horas, margin=ft.margin.only(top=20)),
                    ft.Container(content=self.adicional, margin=ft.margin.only(top=20)),
                    ft.Row(controls=[btn:=ft.Container(content=CalcButton(), margin=ft.margin.only(top=30))], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(controls=[ft.Container(content=self.resultado, margin=ft.margin.only(top=50))], alignment=ft.MainAxisAlignment.CENTER)
                ],
                spacing=0
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.with_opacity(opacity=0.10, color=ft.colors.WHITE12),
            padding=ft.padding.symmetric(vertical=10, horizontal=20),
            height=page.height*0.88
        )
