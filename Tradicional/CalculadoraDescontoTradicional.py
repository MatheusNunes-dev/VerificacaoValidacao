
class CalculadoraDescontoTradicional:

    def calcular_valor_final(self, valor_itens, vip):

        if valor_itens <= 0:
            raise ValueError("O valor dos itens deve ser maior que zero.")

        valor_final = valor_itens

        if valor_itens > 1000:
            valor_final *= 0.80
        elif valor_itens > 500:
            valor_final *= 0.90

        if vip:
            valor_final *= 0.95

        if valor_final < 100:
            valor_final += 15

        return round(valor_final, 2)
