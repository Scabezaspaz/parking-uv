import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from parking import Parking

@pytest.fixture
def parking():
    return Parking()

@pytest.fixture
def parking_vip():
    return Parking(vip=True)

# ── Regla 1: Primeros 30 min gratis ───────────────
def test_15_minutos_gratis(parking):
    assert parking.calcular_tarifa(15) == 0

def test_30_minutos_gratis(parking):
    assert parking.calcular_tarifa(30) == 0

def test_31_minutos_cobra(parking):
    assert parking.calcular_tarifa(31) == 500

def test_90_minutos_cobra(parking):
    assert parking.calcular_tarifa(90) == 1000

# ── Regla 2: $500 por hora o fracción ─────────────
def test_60_minutos_despues_de_gratis(parking):
    assert parking.calcular_tarifa(91) == 1500

def test_fraccion_de_hora_cobra_completa(parking):
    assert parking.calcular_tarifa(61) == 1000

# ── Regla 3: Tope diario $12.000 ──────────────────
def test_tope_diario(parking):
    assert parking.calcular_tarifa(1440) == 12000

def test_sobre_tope_diario(parking):
    assert parking.calcular_tarifa(1500) == 12000

# ── Regla 4: VIP 20% descuento ────────────────────
def test_vip_descuento(parking_vip):
    assert parking_vip.calcular_tarifa(1440) == 9600

def test_vip_bajo_tope(parking_vip):
    assert parking_vip.calcular_tarifa(90) == 800