import flet as ft
from components import components

class ViewHoras(ft.Column):

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