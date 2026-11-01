class CalculadoraDescontoTDD:
    def calcular_valor_final(self, valor_itens, vip):
        if valor_itens > 1000:
            return valor_itens * 0.80

        if valor_itens > 500:
            return valor_itens * 0.90

        return valor_itens
