# Solicita ao usuário que digite um número e armazena esse valor na variável 'numero'.
# A função 'int()' é usada para converter a entrada, que é recebida como uma string, para um inteiro.
numero = int(input("Insira um Número:" ))

# Inicializa a variável 'primo' com o valor True.
# Esta variável será usada como um indicador para determinar se o número é primo ou não.
primo = True

# Utiliza um laço 'for' para iterar sobre uma sequência de números de 2 até 'numero'.
# A função 'range(2, numero)' gera essa sequência, começando em 2 e indo até 'numero' (exclusivo),
# pois um número primo é um número maior que 1 que não é divisível 
# por qualquer outro número que não seja 1 e ele mesmo.
for i in range(2, numero):

    # Verifica se 'numero' é divisível por 'i'.
    # O operador '%' retorna o resto da divisão de 'numero' por 'i'.
    # Se o resto é 0, então 'numero' é divisível por 'i', e não é um número primo.
    if numero % i == 0:

        # Define 'primo' como False indicando que 'numero' não é um número primo.
        primo = False

        # Sai do laço imediatamente, pois não é necessário continuar as verificações.
        break

# Após o laço, verifica o valor da variável 'primo'.
# Se 'primo' ainda é True, então o número passou pelo laço sem encontrar divisores além de 1 e ele mesmo.
if primo: 

    # Imprime que o número é primo.
    print(f"O Número {numero} é Primo")

else:

    # Se 'primo' é False, então o número é divisível por algum número além de 1 e ele mesmo, portanto, não é primo.
    print(f"O Número {numero} não é Primo")
