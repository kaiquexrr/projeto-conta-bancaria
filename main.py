from services.banco import Banco
from ui.menu import menu_principal

if __name__ == '__main__':
    banco = Banco()
    menu_principal(banco)