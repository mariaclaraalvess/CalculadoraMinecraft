
def calcular_recursos():
    print("==========================================")
    print("   BEM-VINDO À CALCULADORA DE MINECRAFT!   ")
    print("==========================================")

#Pergunta o que o jogador quer construir
    projeto = input("\nO que você vai construir hoje? (Ex: Casa, Torre, Apartamento): ")

#Pede as dimensões em blocos
    try:
        largura = int(input("Qual é a largura em blocos? "))
        altura = int(input("Qual é a altura em blocos? "))
        comprimento = int(input("Qual é o comprimento em blocos? "))

        if largura <= 0 or altura <= 0 or comprimento <= 0:
            print("\n[Erro] As medidas devem ser maiores que zero.")
            return

    except ValueError:
        print("\n[Erro] Opa! Digite apenas números inteiros para as medidas.")
        return

#Calcula o total de blocos necessários
    piso_e_teto = 2 * (largura * comprimento)
    perimetro = 2 * (largura + comprimento)
    paredes = (perimetro - 4) * altura
    total_blocos = piso_e_teto + paredes

    # Convertendo para packs de 64
    packs = total_blocos // 64
    blocos_soltos = total_blocos % 64

    print("\n--- RESUMO DA CONSTRUÇÃO ---")
    print(f"🏠 Projeto: {projeto}")
    print(f"🧱 Chão e teto: {piso_e_teto} blocos")
    print(f"🧱 Paredes: {paredes} blocos")
    print(f"📦 Total de blocos: {total_blocos}")
    print("\n--- RESUMO PARA O INVENTÁRIO ---")
    print(f"📦 Packs completos (64 blocos): {packs}")
    print(f"🧱 Blocos avulsos sobressalentes: {blocos_soltos}")


#Loop para o programa rodar quantas vezes o jogador quiser
continuar = "s"

while continuar.lower() == "s":
    calcular_recursos()
    continuar = input("\nQuer calcular outro projeto? (s/n): ")

print("\nBom jogo e boa sorte nas construções! Tchau!")
