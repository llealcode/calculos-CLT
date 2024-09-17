import flet as ft

class UpperBar(ft.AppBar):
    
    def __init__(self, page):

        super().__init__(
            leading=ft.Icon(ft.icons.WALLET_TRAVEL),
            leading_width=40,
            title=ft.Text("Cálculos trabalhistas"),
            center_title=False,
            bgcolor=ft.colors.with_opacity(opacity=0.3, color=ft.colors.BLACK)
        )

class BottomBar(ft.BottomAppBar):
    
    def __init__(self, page):

        super().__init__(
            content=ft.Row(
                controls=[
                    BarButton(texto='Horas', icone=ft.icons.TIMER_ROUNDED, estado='ativo'),
                    BarButton(texto='Férias', icone=ft.icons.BEACH_ACCESS_ROUNDED, estado='inativo'),
                    BarButton(texto='Rescisão', icone=ft.icons.POWER_OFF_ROUNDED, estado='inativo'),
                    BarButton(texto='13º', icone=ft.icons.MONETIZATION_ON_ROUNDED, estado='inativo')
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
            bgcolor=ft.colors.BLACK45,
            height=page.height*0.12
        )

class BarButton(ft.IconButton):
    
    def __init__(self, texto, icone, estado):
        self.texto=texto
        self.icone=icone
        self.estado=estado

        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Icon(name=self.icone, color=ft.colors.WHITE if estado=='ativo' else ft.colors.GREY_800),
                    ft.Text(value=self.texto, color=ft.colors.WHITE)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

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
    
    def __init__(self, texto, prefix=None):
        self.texto = texto
        self.prefix = prefix

        super().__init__(
            controls=[
                ft.Text(value=self.texto, size=13, color=ft.colors.WHITE),
                ft.TextField(
                    height=45,
                    prefix_text=self.prefix,
                    content_padding=ft.padding.symmetric(horizontal=10),
                    border_radius=ft.border_radius.all(3),
                    border_width=0.5,
                    border_color=ft.colors.GREY_500,
                    focused_border_width=1,
                    focused_border_color=ft.colors.GREEN_400,
                    text_align=ft.TextAlign.START,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    cursor_color=ft.colors.GREY_300,
                    cursor_width=0.7
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
                bgcolor=ft.colors.GREEN,
                color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=370,
            height=45,
            on_click=calc
        )


class OptionButton(ft.ElevatedButton):

    def __init__(self, texto, icone, rota, page):
        self.texto = texto
        self.icone = icone
        self.rota = rota

        super().__init__(
            text=texto,
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