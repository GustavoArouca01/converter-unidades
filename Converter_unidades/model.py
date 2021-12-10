def conversão():
    print("Este programa realiza conversão de unidades.")
    print("Insira o valor a ser convertido:")
    x= float(input("Digite o valor em milímetros para ser convertido:"))
    m = x/1000
    cm = x/10
    pol = x / 25,4
    pes = x / 304,8
    jar = x / 914,4 
    print("A medida de milímetros corresponde a:")
    print("    {}Metros".format(m,))
    print("    {}Centimetros ".format(cm))
    print("    {}Polegadas".format(pol))
    print("    {}Pés".format(pes))
    print("    {}Jardas".format(jar))

def instruções():
    print("Este programa realiza conversão de unidades.")
    print("")
    print("Digite em milímetros e ele irá converter para metros, cm, polegadas, jardas e pes.")
    print("")
    print("Sua funcionalidade é muito simples. Obrigado.")

