# ParkingUV S.A.S. — Módulo de Facturación

## Reglas de negocio
- Los primeros 30 minutos son gratuitos
- A partir del minuto 31 se cobra $500 por cada hora o fracción
- El cobro máximo por día (24 horas) es de $12.000
- Clientes VIP tienen 20% de descuento antes de aplicar el tope diario

## Tecnología
- **Lenguaje:** Python 3.13
- **Tests unitarios:** pytest
- **BDD:** pytest-bdd con Gherkin
- **Rendimiento:** Locust
- **CI/CD:** GitHub Actions

## Cómo correr cada tipo de prueba localmente

### Tests unitarios
```bash
pytest tests/test_parking.py -v
```

### Tests BDD
```bash
pytest tests/features/steps/steps_parking.py -v
```

### Tests de rendimiento
```bash
locust -f locustfile.py --headless -u 10 -r 2 --run-time 30s
```

### Tests de seguridad
```bash
pip install bandit
bandit -r src/
```

---

## Tabla de casos de prueba

### Partición de equivalencia y valores límite — Regla 1 (primeros 30 min gratis)

| ID | Partición | Minutos | Resultado esperado | Tipo |
|---|---|---|---|---|
| CP01 | Válida gratis | 15 | $0 | Positivo |
| CP02 | Válida gratis límite | 30 | $0 | Borde |
| CP03 | Válida cobro límite | 31 | $500 | Borde |
| CP04 | Válida cobro | 90 | $1000 | Positivo |

### Partición de equivalencia y valores límite — Regla 3 (tope diario $12.000)

| ID | Partición | Minutos | Resultado esperado | Tipo |
|---|---|---|---|---|
| CP05 | Válida bajo tope | 720 | $6000 | Positivo |
| CP06 | Válida en tope | 1440 | $12000 | Borde |
| CP07 | Válida sobre tope | 1500 | $12000 | Borde |
| CP08 | VIP con descuento | 1440 | $9600 | Positivo |