from utils import settings
import flet as ft

def main(page: ft.Page):

    settings.layout(page=page)

ft.app(target=main)

