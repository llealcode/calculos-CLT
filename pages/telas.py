import flet as ft
from components import components

class CorpoHoras(ft.Column):

    def __init__(self, page):

        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                components.CampoTxt(texto="Salário base", prefix_text='R$ '),
                                components.CampoTxt(texto="Jornada"),
                                components.CampoTxt(texto="Horas trabalhadas"),
                                components.CampoTxt(texto="Taxa adicional", prefix_text='% '),
                                ft.Container(content=ft.Row(controls=[components.CalcButton()]), margin=ft.margin.only(top=10))
                            ], 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                )
            ]
            
        )


class CorpoFerias(ft.Column):

    def __init__(self, page):

        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                components.CampoTxt(texto="Salário", prefix_text='R$ '),
                                ft.Container(content=ft.Row(controls=[components.CalcButton()]), margin=ft.margin.only(top=10))
                            ], 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                )
            ]
            
        )


class CorpoRescisao(ft.Column):

    def __init__(self, page):

        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.ElevatedButton(text="Rescisão comum", color=ft.colors.WHITE),
                                ft.ElevatedButton(text="Rescisão voluntária", color=ft.colors.WHITE),
                                ft.ElevatedButton(text="Justa causa", color=ft.colors.WHITE),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=60, 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                ),
            ]            
        )


class CorpoDecimo(ft.Column):

    def __init__(self, page):

        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                components.CampoTxt(texto="Salário"),
                                components.CampoTxt(texto="Meses trabalhados"),
                                ft.Container(content=ft.Row(controls=[components.CalcButton()]), margin=ft.margin.only(top=10))
                            ], 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                )
            ]
            
        )


class CorpoAdicional(ft.Column):

    def __init__(self, page):

        super().__init__(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                components.CampoTxt(texto="Salário base", prefix_text='R$ '),
                                components.CampoTxt(texto="Horas trabalhadas"),
                                components.CampoTxt(texto="Taxa", prefix_text='% '),
                                ft.Container(content=ft.Row(controls=[components.CalcButton()]), margin=ft.margin.only(top=10))
                            ], 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                )
            ]
            
        )