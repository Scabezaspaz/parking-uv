class Parking:
    """Modulo de facturacion para ParkingUV S.A.S."""

    MINUTOS_GRATIS = 30
    TARIFA_POR_HORA = 500
    TOPE_DIARIO = 12000
    DESCUENTO_VIP = 0.20

    def __init__(self, vip: bool = False):
        """Inicializa el parqueadero.

        Args:
            vip: True si el cliente tiene membresia VIP.
        """
        self.vip = vip

    def calcular_tarifa(self, minutos: int) -> float:
        """Calcula la tarifa a cobrar segun los minutos estacionado.

        Args:
            minutos: Tiempo total estacionado en minutos.

        Returns:
            Tarifa a cobrar en pesos colombianos.
        """
        if minutos <= self.MINUTOS_GRATIS:
            return 0

        total = self._calcular_cobro_base(minutos)

        if self.vip:
            total = self._aplicar_descuento_vip(total)

        return min(total, self.TOPE_DIARIO)

    # ── Metodos privados ───────────────────────────
    def _calcular_cobro_base(self, minutos: int) -> float:
        """Calcula el cobro base sin descuentos ni tope."""
        minutos_cobrables = minutos - self.MINUTOS_GRATIS
        horas = -(-minutos_cobrables // 60)
        return horas * self.TARIFA_POR_HORA

    def _aplicar_descuento_vip(self, total: float) -> float:
        """Aplica el descuento VIP sobre el total."""
        return total * (1 - self.DESCUENTO_VIP)