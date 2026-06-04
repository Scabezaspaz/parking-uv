Feature: Facturacion de parqueadero ParkingUV
  Como gerente de ParkingUV S.A.S.
  Quiero calcular el cobro a los clientes
  Para facturar correctamente segun el tiempo estacionado

  Background:
    Given un cliente en el parqueadero

  @smoke
  Scenario: Cliente sale antes de 30 minutos gratis
    When el cliente estuvo estacionado 15 minutos
    Then la tarifa cobrada es 0 pesos

  @smoke
  Scenario: Cliente en el limite de la gratuidad
    When el cliente estuvo estacionado 30 minutos
    Then la tarifa cobrada es 0 pesos

  @critical
  Scenario: Cliente supera los 30 minutos gratis
    When el cliente estuvo estacionado 31 minutos
    Then la tarifa cobrada es 500 pesos

  @critical
  Scenario: Se aplica el tope diario maximo
    When el cliente estuvo estacionado 1440 minutos
    Then la tarifa cobrada es 12000 pesos

  @critical
  Scenario: Cliente VIP obtiene descuento del 20%
    Given un cliente VIP en el parqueadero
    When el cliente estuvo estacionado 1440 minutos
    Then la tarifa cobrada es 9600 pesos

  @regression
  Scenario Outline: Verificar tarifas segun tiempo estacionado
    When el cliente estuvo estacionado <minutos> minutos
    Then la tarifa cobrada es <tarifa> pesos

    Examples:
      | minutos | tarifa |
      | 15      | 0      |
      | 30      | 0      |
      | 31      | 500    |
      | 1500    | 12000  |