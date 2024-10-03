import flet as ft
from components import components

class ViewHoras(ft.Column):

    def __init__(self, page):

        self.salario = components.CampoTxt(texto="Salário base", prefix_text='R$ ')
        self.jornada = components.CampoTxt(texto="Jornada")
        self.horas = components.CampoTxt(texto="Horas trabalhadas")
        self.taxa = components.CampoTxt(texto="Taxa adicional", prefix_text='% ')
        self.btn_calcular = components.CalcButton(page=page)

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
                                self.salario,
                                self.jornada,
                                self.horas,
                                self.taxa,
                                ft.Container(content=ft.Row(controls=[self.btn_calcular]), margin=ft.margin.only(top=10))
                            ], 
                            # xs -> 0 a 575, sm -> 576 a 767, md -> 768 a 991, lg -> 992 a 1199, xl -> 1200 a 1399, xs -> maior que 1400
                            col={'xs':11, 'sm':7, 'md':5, 'lg':4, 'xl':3}
                        )
                    ]
                )
            ]  
        )

        def click(e):

            alerta = components.AlertHoras(
                page=page, 
                salario=self.salario.controls[1].value,
                jornada=self.jornada.controls[1].value,
                horas=self.horas.controls[1].value,
                taxa=self.taxa.controls[1].value
            )
            
            page.overlay.append(alerta)
            page.overlay[0].open = True
            page.update()
        
        self.btn_calcular.on_click = click