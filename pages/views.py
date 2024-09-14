import flet as ft

from pages import home
from pages import fgts
from pages import horas
from pages import rescisao
from pages import decimo


def mudar_rota(e, page):
    page.views.clear()
    rota = page.route

    match rota:
        case '/':
            conteudo = home.home()
        case '/horas':
            conteudo = horas.horas()
        case '/fgts':
            conteudo = fgts.fgts()
        case '/decimo3':
            conteudo = decimo.decimo()
        case '/rescisao':
            conteudo = rescisao.rescisao()
    
    page.views.append(
        ft.View(
            route=rota,
            padding=0,
            spacing=0,
            bgcolor=ft.colors.BLACK,
            controls=[conteudo],
        )
    )

    page.update()
