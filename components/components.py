import flet as ft
from utils import settings

class UpperBar(ft.AppBar):
    
    def __init__(self, page):

        super().__init__(
            leading=ft.Icon(ft.icons.WALLET_TRAVEL),
            leading_width=40,
            title=ft.Text("Cálculos trabalhistas"),
            center_title=False,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text='Como cálcular?'),
                        ft.PopupMenuItem(text='Como cálcular?'),
                        ft.PopupMenuItem(text='Como cálcular?'),
                        ft.PopupMenuItem(text='Como cálcular?')
                    ]
                )
            ]
            bgcolor=ft.colors.with_opacity(opacity=0.3, color=ft.colors.BLACK)
        )

class BottomBar(ft.BottomAppBar):
    
    def __init__(self, page):

        self.botoes = {
            'horas': BarButton(texto='Horas', icone=ft.icons.TIMER_ROUNDED, estado='inativo', page=page, rota="/horas"),
            'ferias': BarButton(texto='Férias', icone=ft.icons.BEACH_ACCESS_ROUNDED, estado='inativo', page=page, rota="/ferias"),
            'rescisao': BarButton(texto='Rescisão', icone=ft.icons.POWER_OFF_ROUNDED, estado='inativo', page=page, rota="/rescisao"),
            'decimo_terceiro': BarButton(texto='13º', icone=ft.icons.MONETIZATION_ON_ROUNDED, estado='inativo', page=page, rota="/decimo_terceiro"),
            'adicional_noturno': BarButton(texto='Adicional', icone=ft.icons.MODE_NIGHT, estado='inativo', page=page, rota="/adicional_noturno")
        }

        super().__init__(
            content=ft.Row(
                controls=list(self.botoes.values()),
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            bgcolor=ft.colors.BLACK45,
            height=page.height*0.12
        )


class BarButton(ft.Container):
    
    def __init__(self, texto, icone, estado, page, rota):
        self.estado = estado
        self.page = page
        self.rota = rota
        self.texto = ft.Text(value=texto, color=self._definir_cor())
        self.icone = ft.Icon(name=icone, color=self._definir_cor())

        super().__init__(
            content=ft.Container(
               content= ft.Column(
                    controls=[
                        self.icone,
                        self.texto
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            on_click=self.navegar
        )
    
    def navegar(self, _):
        self.page.go(self.rota)

    def _definir_cor(self):
        return ft.colors.WHITE if self.estado == 'ativo' else ft.colors.GREY_800
    
    def mudar_estado(self, novo_estado):

        self.estado = novo_estado
        self.icone.color = self._definir_cor()
        self.texto.color = self._definir_cor()

        if self.page is not None:
            self.update()

    def navegar(self, page):
        self.page.go(self.rota)

class Alert(ft.Text):
    
    def __init__(self, valor=0):

        super().__init__(
            value=valor,
            size=30,
            color=ft.colors.TRANSPARENT,
            weight=ft.FontWeight.BOLD
        )

        self.valor=valor

class Headers(ft.Text):
    
    def __init__(self, texto: str, tipo):
        self.texto = texto
        super().__init__(
            value=self.texto,
            weight=ft.FontWeight.BOLD,
            size=20 if tipo=='Título' else 12,
            color=ft.colors.with_opacity(opacity=0.70, color=ft.colors.WHITE)
        )

class CampoTxt(ft.Column):
    
    def __init__(self, texto, **kwargs):
        self.texto = texto

        super().__init__(
            controls=[
                ft.Text(value=self.texto, size=13, color=ft.colors.WHITE),
                ft.TextField(
                    height=45,
                    content_padding=ft.padding.symmetric(horizontal=10),
                    border_radius=ft.border_radius.all(3),
                    border_width=0.5,
                    border_color=ft.colors.GREY_500,
                    focused_border_width=1,
                    focused_border_color=ft.colors.GREEN_400,
                    text_align=ft.TextAlign.START,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    cursor_color=ft.colors.GREY_300,
                    cursor_width=0.7,
                    **kwargs
                )
            ],
            spacing=7
        )

class CalcButton(ft.ElevatedButton):
    
    def __init__(self):

        def calc(e):
            pass

        super().__init__(
            text='Calcular',
            icon=ft.icons.CALCULATE_ROUNDED,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN_800,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            height=45,
            expand=True,
            on_click=calc
        )


class OptionButton(ft.IconButton):

    def __init__(self, texto, icone, rota, page):
        self.texto = texto
        self.icone = icone
        self.rota = rota

        super().__init__(
            icon=icone,
            style=ft.ButtonStyle(
                overlay_color=ft.colors.GREY_700,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=200,
            height=45,
            on_click=lambda _: page.go(self.rota)
            )


class HomePageMessage(ft.Text):

    def __init__(self):

        super().__init__(
            value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
            max_lines=6
        )
