import flet as ft

from utils.settings import layout


def main(page: ft.Page):
    
    layout(page=page)

    page.window.always_on_top = True

ft.app(target=main, assets_dir='assets')
