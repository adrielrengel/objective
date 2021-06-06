from escolhe import Escolhe


class JogoAdivinha:
    def __init__(self ,raiz):
        self.arvorebinaria = raiz

    def nova_comida(self, palpite):
        novo_prato = input("Qual é o nome da comida? ")
        novo_tipo = input(f"{novo_prato} é ____ mas {palpite.data} não é? ")
        return novo_prato, novo_tipo

    def adiciona_comida(self, arvorebinaria, prato, tipo):
        arvorebinaria.right = Escolhe(arvorebinaria.data)
        arvorebinaria.left = Escolhe(prato)
        arvorebinaria.data = tipo

    def testa_resposta(self):
        resposta = self.arvorebinaria
        while not resposta.inicia():
            if input(f"O prato que você pensou é {resposta.data}? (s/n)").lower() == "s":
                resposta = resposta.left
            else:
                resposta = resposta.right
        return resposta

    def inicia_jogo(self):
        joga = True
        while joga:
            input("Pense em um prato que gosta? digite enter")
            resposta = self.testa_resposta()
            acertou = input(f"O prato que você pensou é {resposta.data}? (s/n)").lower() == "s"

            if acertou:
                print("Acertei de novo!")
                continue
            prato, tipo = self.nova_comida(resposta)

            if not resposta.inicia():
                continue

            self.adiciona_comida(resposta, prato, tipo)


if __name__ == "__main__":

    inicio = Escolhe("Massa", Escolhe("Lasanha"), Escolhe("Bolo de Chocolate"))
    jogo = JogoAdivinha(inicio)
    jogo.inicia_jogo()




