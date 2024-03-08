"""
AC4: CLI(command-line interface)

"""
def calcular_media(ap1, ap2, as_, ac):
    if not (0 <= ap1 <= 10) or not (0 <= ap2 <= 10) or not (0 <= as_ <= 10) or not (0 <= ac <= 10):
        print("Notas inválidas. As notas devem estar entre 0 e 10.")
        return None

    if as_ < ap1 or ap2:
        media = ((ap1 + ap2) * 0.4 + ac * 0.2)
    else:
        media = (((ap1 + ap2) - min(ap1, ap2) + as_) * 0.4 + ac * 0.2)

    return media

def verificar_aprovacao(media):
    if media is None:
        return "Reprovado"
    elif media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def ler_notas():
    ap1 = float(input("Digite a nota da AP1: "))
    ap2 = float(input("Digite a nota da AP2: "))
    as_ = float(input("Digite a nota da AS: "))
    ac = float(input("Digite a nota da AC: "))

    return ap1, ap2, as_, ac

def main():
    nome = input("Digite seu nome: ")
    if nome.strip() == "":
        print("Nome não pode ser vazio.")
        return

    ap1, ap2, as_, ac = ler_notas()
    media = calcular_media(ap1, ap2, as_, ac)

    if media is not None:
        print(f"A média final de {nome} é: {media:.2f}")
        situacao = verificar_aprovacao(media)
        print(f"Situação: {situacao}")

if __name__ == "__main__":
    main()