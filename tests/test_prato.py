from .conftest import prato_fixture

def teste_aplicar_desconto_prato(prato_fixture):
    prato = prato_fixture
    prato.aplicar_desconto()

    assert prato._preco == 76