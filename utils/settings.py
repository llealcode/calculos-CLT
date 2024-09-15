import flet as ft
from pages.home import ViewHome
from components.components import UpperBar, BottomBar


def layout(page):
    
     # Localidade e idioma da página
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale('pt', 'BR')], current_locale=ft.Locale('pt', 'BR'))

    # Tamanho da janela e posicionamento    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.maximizable = False
    page.window.resizable = True
    page.window.center()
    page.update()

    # Comportamento, espaçamento e margins
    page.padding = 0
    page.spacing = 0

    # Temas, cores e layout
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.bgcolor = ft.colors.WHITE
    page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.colors.BLUE_800))

    # Fontes
    page.fonts={}

    # Rotas
    class ViewsPage(ft.View):

        def __init__(self, rota, conteudo):
            self.rota = rota
            self.conteudo = conteudo

            super().__init__(
                route=self.rota,
                controls=[self.conteudo],
                padding=0,
                spacing=0,
                bottom_appbar=BottomBar(page=page),
                appbar=UpperBar(page=page)
            )

    def mudar_rota(e):
        page.views.clear()
        page.views.append(ViewsPage(rota=page.route, conteudo=ViewHome(page=page)))

        page.update()


    page.on_route_change = mudar_rota
    page.go('/')