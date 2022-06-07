import this #importando da bibliotca
import Operacoes # acessando aclasse operações
this.opcao = 0 #declaração de variavel global
this.num1 = 0
this.num2 = 0


def mostrarMenu():
    while(this.opcao != 0):
        print('Escolha uma das opções abaixo:\n' +
              '1. Soma\n'                        +
              '2. Subtrção\n'                    +
              '3. Multiplicação\n'               +
              '4. Divisão\n'                     +
              '0. Sair\n\n')
        this.opcao = int(input()) #entrada de dados.

    def coletarNum1():
        print ('Informe o primeiro número:')
        this.num1= float(input()) #convertendo texto em número com vírgula.

    def coletarNum2():
        print('Informe o segundo número:')
        this.num2 = float(input())  # convertendo texto em número com vírgula.

    def executar():
        mostrarMenu() #Chamando o método que mostra as opções para o suario.

        if this.opcao == 1:
            coletarNum1() #Pegando o primeiro número.
            coletarNum2() #Pegando o segundo número.
            print('A soma entre {} e {} é igual a {}'.format(this.num1, this.num2, Operacoes.soma(this.num1, this.num2)))

        elif this.opcao == 2:
            coletarNum1()
            coletarNum2()
            print('A subtrção entre {} e {} é igual a {}'.format(this.num1, this.num2, Operacoes.subtrair(this.num1, this.num2)))

        elif this.opcao == 3:
            coletarNum1()
            coletarNum2()
            print('A Multiplicação entre {} e {} é igual a {}'.format(this.num1, this.num2, Operacoes.multiplicar(this.num1, this.num2)))

        elif this.opcao == 4:
            coletarNum1()
            coletarNum2()
            print('A divisão entre {} e {} é iguala {}'.format(this.num1, this.num2, Operacoes.dividir(this.num1, this.num2)))

        else:
            print('Obrigado!')
            this.opcao = 0



