from .conftest import restaurante_fixture
import pytest
from components.cardapio.prato import Prato

def test_instanciacao_e_formatacao(restaurante_fixture):
    assert restaurante_fixture._nome == "Restaurante 1"
    assert restaurante_fixture._categoria == "TRADICIONAL"

def test_estado_inicial_e_propriedade_ativo(restaurante_fixture):
    assert restaurante_fixture._ativo == False
    assert restaurante_fixture.ativo == '❌'

def test_alternar_estado_para_ativo(restaurante_fixture):
    restaurante_fixture.alternar_estado()
    assert restaurante_fixture._ativo == True
    assert restaurante_fixture.ativo == '✅'

def test_alternar_estado_para_inativo(restaurante_fixture):
    restaurante_fixture._ativo = True 
    restaurante_fixture.alternar_estado()
    assert restaurante_fixture._ativo == False
    assert restaurante_fixture.ativo == '❌'

def test_calcular_media_avaliacoes_com_dados_mockados(restaurante_fixture):
    restaurante_fixture.calcular_media_avaliacoes()
    assert restaurante_fixture._avaliacoes.media == pytest.approx(3.0)

def test_calcular_media_avaliacoes_com_multiplos_dados(restaurante_fixture):
    restaurante_fixture._avaliacoes.avaliacoes_individuais.append({
        "rating": 5,
        "description": "Excelente"
    })
    
    restaurante_fixture.calcular_media_avaliacoes()
    assert restaurante_fixture._avaliacoes.media == pytest.approx(4.0)

def test_adicionar_prato_no_cardapio(restaurante_fixture):
    cardapio_inicial_len = len(restaurante_fixture._cardapio)
    novo_prato = Prato(nome="Salada", preco=30, descricao="Verdes")
    
    restaurante_fixture.adicionar_no_cardapio(novo_prato)
    
    assert len(restaurante_fixture._cardapio) == cardapio_inicial_len + 1
    assert restaurante_fixture._cardapio[-1]._nome == "Salada"

def test_processar_cardapio_cria_somente_prato_no_mock_atual(restaurante_fixture):
    cardapio = restaurante_fixture._cardapio
    assert len(cardapio) == 3 
    assert all(isinstance(item, Prato) for item in cardapio)