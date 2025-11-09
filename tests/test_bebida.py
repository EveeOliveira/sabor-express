from .conftest import bebida_fixture

def teste_aplicar_desconto_bebidade(bebida_fixture):
    bebida = bebida_fixture
    bebida.aplicar_desconto()

    assert bebida._preco == 9.2