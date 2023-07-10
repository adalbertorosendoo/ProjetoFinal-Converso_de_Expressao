from Converso import *
import string
import time, os

Expressao = ConversorExpressao()

while True:
    print('================ Menu ================')
    print('(p) Converter para pós-fixa')
    print('(i) Converter para pré-fixa')
    print('(a) Associar valores aos operandos')
    print('(e) Executar expressão')
    print('(s) Sair')
    print('======================================')

    escolha = input('Escolha: ')
    if escolha.lower() == 'p':
        digitado=input('Digite a expressão na forma infixa: ')
        resposta=input('Quer vê o passo a passo S/N: ')
        try:
            if Expressao.validacao(digitado):
                print('OK: expressão valida!')
                Expressao.conversorPosFixa(digitado)
                if resposta.lower() == 's':
                    Expressao.mostraPassos()
                    print('Expressão Pós-Fixada {}'.format(Expressao))
                    print()

                elif resposta.lower() == 'n':
                    print('Expressao Pós-fixada {}'.format(Expressao))
                    print()

                else:
                    print('Resposta invalida. A resposta deve ser "S" ou "N".')
                    print()
            
            else:
                print('Expressao invalida, tente novamente.')
                digitado=input('Digite a expressão na forma infixa: ')
                while Expressao.validacao(digitado) == False:
                    print('Expressao invalida, tente novamente.')
                    print()
                    digitado=input('Digite a expressão na forma infixa: ')
                Expressao.conversorPosFixa(digitado)
                if resposta.lower() == 's':
                    Expressao.mostraPassos()
                    print('Expressão Pós-fixada {}'.format(Expressao))
                    print()

                elif resposta.lower() == 'n':
                    print('Expressão Pós-fixada {}'.format(Expressao))
                    print()

                else:
                    print('Resposta Invalida. A resposta deve ser "S" ou "N".')
        except validaException as ve:
            print('validaException: ', str(ve))
            print()

    elif escolha.lower() == 'i':
        digitado=input('Digite a expressão na forma infixa: ')
        resposta=input('Quer vê o passo a passo S/N: ')
        try:
            if Expressao.validacao(digitado):
                print('OK. Expressão valida!')
                Expressao.conversorPreFixa(digitado)
                if resposta.lower() == 's':
                    Expressao.mostraPassosPreFixa()
                    print('Expressão Pré-fixada {}'.format(Expressao))
                    print()

                elif resposta.lower() == 'n':
                    print('Expressão Pré-fixada {}'.format(Expressao))
                    print()

                else:
                    print('Resposta invalida. A resposta deve ser "S" ou "N".')
                    print()
            else:
                print('Expressao invalida, tente novamente.')
                digitado=input('Digite a expressão na forma infixa: ')
                while Expressao.validacao(digitado) == False:
                    print('Expressao Invalida tente novamente')
                    print()
                    digitado=input('Digite a expressão na forma infixa: ')
                Expressao.conversorPreFixa(digitado)
                if resposta.lower() == 's':
                    Expressao.mostraPassosPreFixa()
                    print('Expressão Pré-fixada {}'.format(Expressao))
                    print()
        
                elif resposta.lower() == 'n':
                    print('Expressão Pré-fixada {}'.format(Expressao))
                    print()

                else:
                    print('Resposta invalida. A resposta deve ser "S" ou "N".')
                    print()
        except validaException as ve:
            print('validaException: ', str(ve))
            print()

    elif escolha.lower() == 'a':
        try:
            if len(Expressao._ConversorExpressao__expressaoAtual) == 0:
                raise ExpressaoVaziaException("A expressão está vazia.")
            for variavel in Expressao._ConversorExpressao__expressaoAtual:
                if variavel in string.ascii_lowercase:
                    while True:
                        valor = input(f'{variavel} = ')
                        try:
                            valor =float(valor)
                            break                        
                        except ValueError:
                            print('Valor inválido. Só será permitido valores numéricos.')
                    Expressao.adicionarValor(variavel, float(valor))
        except validaException as ve:
            print('validaException:', str(ve))
            print()
        except ExpressaoVaziaException as eve:
            print('ExpressaoVaziaException:', str(eve))
            print()
        

    elif escolha.lower() == 'e':
        try:
            resultado = Expressao.executarExpressao()
            print('Resultado: {}'.format(resultado))
            print()

        except validaException as ve:
            print('validaException: ', str(ve))

    elif escolha.lower() == 's':
        print('Encerrando o programa em 5 segundos...\nAté a próxima interação.')
        time.sleep(5)
        os.system('cls')
        break

    else:
        print('Opção invalida. Escolha uma das opções do menu.')
        print()
        continue 
