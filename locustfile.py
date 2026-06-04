import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from locust import HttpUser, task, between
from parking import Parking

class ParkingUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost"

    @task(3)
    def calcular_tarifa_normal(self):
        start = time.time()
        parking = Parking()
        parking.calcular_tarifa(90)
        elapsed = (time.time() - start) * 1000
        assert elapsed < 300, f"P95 excede 300ms: {elapsed}ms"

    @task(1)
    def calcular_tarifa_vip(self):
        start = time.time()
        parking = Parking(vip=True)
        parking.calcular_tarifa(1440)
        elapsed = (time.time() - start) * 1000
        assert elapsed < 300, f"P95 excede 300ms: {elapsed}ms"

    @task(1)
    def calcular_tope_diario(self):
        start = time.time()
        parking = Parking()
        parking.calcular_tarifa(1500)
        elapsed = (time.time() - start) * 1000
        assert elapsed < 300, f"P95 excede 300ms: {elapsed}ms"