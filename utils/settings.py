import flet as ft
from pages.home import ViewHome
from pages.horas import ViewHoras
from components.components import UpperBar, BottomBar


def layout(page):
    
     # Localidade e idioma da página
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale('pt', 'BR')], current_locale=ft.Locale('pt', 'BR'))

    # Tamanho da janela e posicionamento    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.maximizable = True
    page.window.resizable = True
    page.window.height = 600
    page.window.width = 390
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

        def __init__(self, rota, conteudo, **kwargs):
            self.rota = rota
            self.conteudo = conteudo

            super().__init__(
                route=self.rota,
                controls=[self.conteudo],
                padding=0,
                spacing=0,
                appbar=UpperBar(page=page),
                **kwargs
            )

    def mudar_rota(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(ViewsPage(rota=page.route, conteudo=ViewHome(page=page)))
        if page.route =="/horas":
            page.views.append(ViewsPage(rota=page.route, conteudo=ViewHoras(page=page), bottom_appbar=BottomBar(page=page)))

        page.update()


    page.on_route_change = mudar_rota
    page.go('/')
