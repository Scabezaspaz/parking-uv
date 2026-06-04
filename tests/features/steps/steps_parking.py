import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from pytest_bdd import given, when, then, parsers, scenarios
from parking import Parking

scenarios('../parking.feature')

@given('un cliente en el parqueadero', target_fixture='cliente')
def cliente_normal():
    return Parking()

@given('un cliente VIP en el parqueadero', target_fixture='cliente')
def cliente_vip():
    return Parking(vip=True)

@when(parsers.parse('el cliente estuvo estacionado {minutos:d} minutos'))
def estacionar(cliente, minutos):
    cliente._minutos = minutos

@then(parsers.parse('la tarifa cobrada es {tarifa:d} pesos'))
def verificar_tarifa(cliente, tarifa):
    assert cliente.calcular_tarifa(cliente._minutos) == tarifa