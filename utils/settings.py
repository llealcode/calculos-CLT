import flet as ft
from pages.home import ViewHome
from pages import telas
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
    # page.window.center()
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
					bottom_bar = BottomBar(page)

        if page.route == "/":
            view = ViewsPage(rota=page.route, conteudo=ViewHome(page=page))
        if page.route == "/horas":
            view = ViewsPage(rota=page.route, conteudo=telas.CorpoHoras(page=page), bottom_appbar=BottomBar(page=page))
					if page.route = "/ferias":
								view = ViewsPage(rota=page.route, conteudo=telas.CorpoFerias(page=page), bottom_appbar=bottom_bar)
					if page.route = "/rescisao":
								view = ViewsPage(rota=page.route, conteudo=telas.CorpoRescisao(page=page, bottom_appbar=bottom_bar)
					if page.route = "/decimo_terceiro":
								view = ViewsPage(rota=page.route, conteudo=telas.CorpoDecimo(page=page), bottom_appbar=bottom_bar)
					if page.route = "/adicional_noturno":
								view = ViewsPage(rota=page.route, conteudo=telas.CorpoNoturno(page=page), bottom_appbar=bottom_bar)

					for nome_botao, botao in bottom_bar.botoes.items():
            botao.mudar_estado('ativo' if nome_botao == page.route[1:] else 'inativo')

        page.views.append(view)
        page.update()


    page.on_route_change = mudar_rota
    page.go('/horas')
