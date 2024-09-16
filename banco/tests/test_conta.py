import pytest
from ..models.conta import Conta

@pytest.fixture
def conta_valida():
    return Conta(333,666)
    
def test_validando_atributo_conta(conta_valida):
    assert conta_valida.numero_conta == 333
