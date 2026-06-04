class Parking:

    def __init__(self, vip=False):
        self.vip = vip

    def calcular_tarifa(self, minutos):
        if minutos <= 30:
            return 0

        minutos_cobrables = minutos - 30
        horas = -(-minutos_cobrables // 60)
        total = horas * 500

        if self.vip:
            total = total * 0.80
            return min(total, 12000)

        return min(total, 12000)