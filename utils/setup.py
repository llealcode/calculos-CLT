import flet as ft

from pages.views import mudar_rota


def layout(page):
    
     # Localidade e idioma da página
    page.locale_configuration = ft.LocaleConfiguration(supported_locales=[ft.Locale('pt', 'BR')], current_locale=ft.Locale('pt', 'BR'))

    # Tamanho da janela e posicionamento    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.window.maximizable = False
#     page.window.resizable = False
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

    # BottomBar e Botão flutuante
    # page.bottom_appbar
    # page.floating_action_button

    # Rotas
    page.on_route_change = lambda e : mudar_rota(e, page=page)
    page.go('/horas')
