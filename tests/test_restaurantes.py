from .conftest import restaurantes_object_fixture
from components.restaurante import Restaurante

def teste_obter_restaurantes(restaurantes_object_fixture):
    lista_restaurantes = restaurantes_object_fixture._lista_de_restaurantes

    assert len(lista_restaurantes) == 2

    assert all(isinstance(r, Restaurante) for r in lista_restaurantes)

    restaurante_a = lista_restaurantes[0]
    restaurante_b = lista_restaurantes[1]

    assert restaurante_a._nome == "Restaurante 1"
    assert restaurante_b._nome == "Restaurante 2"