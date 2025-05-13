import sys
from views.interface_usuario import InterfaceUsuario

def main():
    """
    Função principal que inicia o sistema.
    """
    interface = InterfaceUsuario()
    interface.iniciar()

if __name__ == "__main__":
    main()
