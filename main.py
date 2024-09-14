import flet as ft

from utils.setup import layout


def main(page: ft.Page):
    
    layout(page=page)


ft.app(target=main, assets_dir='assets')
