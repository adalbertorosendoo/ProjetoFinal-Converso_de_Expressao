import string

class validaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class ExpressaoVaziaException(Exception):
    def _init_(self,msg):
        super()._init_(msg)

class ConversorExpressao:
    __operadores = {'(':0,')':0,'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def __init__(self):
        self.__expressaoConvertida = []
        self.__passoAPasso = []
        self.__Valores = {}
        self.__expressaoAtual = ''

    def prioridade(self, operador):
        return self.__operadores.get(operador, 0)
    
    def __estaVazia(self,pilha:list)->bool:
        return len(pilha) == 0
    
    def Buscar_Operando(self,operando:str)->bool:
        for caractere in range(len(self.__expressaoConvertida)):
            if caractere == operando:
                return True
            else:
                return False
    
    def validacao(self,infixa)->bool :
        return self.__validarTamanho(infixa) and self.__validaParenteses(infixa) and self.__validaExpressao(infixa) and self.__validaIguais(infixa)

    def __validaIguais(self,infixa:str)->bool:
        expressao = list(infixa)
        repetidos = []
        for caractere in expressao:
            if caractere in string.ascii_lowercase:
                if caractere in repetidos:
                    raise validaException('Expressão com operando iguais')
                repetidos.append(caractere)
        return True 
          
    def __validaExpressao(self, infixa: str) -> bool:
        expressao = infixa.lower()
        tamanho = len(expressao)

        if expressao[0] in self.__operadores and expressao[0] != '(':
            raise validaException('Expressão não pode começar com operador')

        if expressao[-1] in self.__operadores and expressao[-1] != ')':
            raise validaException('Expressão não pode terminar com operador')

        for caractere in range(tamanho - 1):
            if expressao[caractere] in string.ascii_lowercase and expressao[caractere + 1] in string.ascii_lowercase:
                raise validaException('Expressão na forma infixa não pode conter operandos juntos')
        
            if expressao[caractere] in self.__operadores and expressao[caractere] != ')' and expressao[caractere +1] in self.__operadores and expressao[caractere + 1] != '(':
                raise validaException('Expressão não pode conter operadores juntos') 

            if expressao[caractere] in self.__operadores and expressao[caractere] != '(' and expressao[caractere -1]  in self.__operadores and expressao[caractere -1] != ')':
                raise validaException('Expressão não pode conter operadores juntos')

        return True


    def __validarTamanho(self, infixa:str)-> bool:
        expressao=(infixa.lower())
        return len(expressao) >= 3
        
    def __validaParenteses(self, infixa:str)->bool:
        expressao=(infixa.lower())
        for caractere in expressao:
            if caractere in string.ascii_lowercase:
                continue

            elif caractere  == '(':
                contador_parenteseAbrir = 1

                for c in expressao[expressao.index(caractere)+1:]:
                    if c == '(':
                        contador_parenteseAbrir += 1

                    elif c == ')':
                        contador_parenteseAbrir -= 1

                if contador_parenteseAbrir != 0:
                    raise validaException('Parantese de abertura encontrado sem fechamento')
                    
            elif caractere == ')':
                contador_parenteseFechar = 0
                for c in expressao:
                    if c == ')':
                        contador_parenteseFechar += 1
                    
                    elif c == '(':
                        contador_parenteseFechar -= 1

                if contador_parenteseFechar != 0:
                    raise validaException('Parantese de fechamento encontrado sem abertura')
 
            elif caractere in self.__operadores:
                continue

            else: 
                return False
        
        return True
    
    def adicionarValor (self,variavel, valor):
        variavel = variavel.strip().lower()
        if variavel in self.__expressaoAtual:
            self.__Valores[variavel] = valor
        
    def executarExpressao(self) -> float:
        if not self.__expressaoAtual:
            raise validaException('Não há expressão para executar')
        pilha = []
        for caractere in self.__expressaoAtual:
            if caractere in self.__operadores:
                operando2 = pilha.pop()
                operando1 = pilha.pop()

                if caractere == '+':
                    resultado = operando1 + operando2
                elif caractere == '-':
                    resultado = operando1 - operando2
                elif caractere == '*':
                    resultado = operando1 * operando2
                elif caractere == '/':
                    resultado = operando1 / operando2
                elif caractere == '^':
                    resultado = operando1 ** operando2

                pilha.append(resultado)
            else:
                valor = self.__Valores.get(caractere)
                if valor is not None:
                    pilha.append(valor)
                else:
                    raise validaException(f"Valor não encontrado para a variável '{caractere}'")

        return pilha[0]
        
    def mostraPassos(self):
        print('Simbolo    Pilha             Saída')
        print('-------    -----------       --------- ')
        for passo in self.__passoAPasso:
            simbolo = passo[0]
            pilha = passo[1]
            saida = passo[2]
            pilha_str = ''.join(pilha)
            saida_str = ''.join(saida)
            print('{:<10} {:<20} {:<10}'.format(simbolo, pilha_str, saida_str))
            input()
        print('-------    -----------       ---------')

    def mostraPassosPreFixa(self):
        print('Simbolo    Pilha             Saída')
        print('-------    -----------       --------- ')
        for passo in self.__passoAPasso:
            simbolo = passo[0]
            pilha = passo[1]
            saida = passo[2]
            pilha_str = ''.join(pilha)
            saida_str = ''.join(saida)
            print('{:<10} {:<20} {:<10}'.format(simbolo, pilha_str, saida_str))
            input()
        print('-------    ----------       ----------')

    def conversorPosFixa(self,expressao:str):
        self.__expressaoConvertida = []
        self.__passoAPasso = []
        pilha = []
        string=list(expressao)
        for caractere in string:
            if caractere in self.__operadores:
                if self.__estaVazia(pilha):
                    pilha.append(caractere)
                    self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
                
                elif caractere == '(':
                    pilha.append(caractere)
                    self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))

                elif caractere == ')':
                    while not self.__estaVazia(pilha) and (pilha[-1]) != '(':
                        self.__expressaoConvertida.append(pilha.pop())
                    if not self.__estaVazia(pilha) and pilha[-1] == '(':
                        pilha.pop()
                    self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
                
                else:
                    if pilha[-1] == '(':
                        pilha.append(caractere)
                        self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
                    
                    elif self.prioridade(pilha[-1]) < self.prioridade(caractere):
                        pilha.append(caractere)
                        self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
                    
                    else:
                        while not self.__estaVazia(pilha) and self.prioridade(pilha[-1]) >= self.prioridade(caractere):
                            self.__expressaoConvertida.append(pilha.pop())
                        
                        pilha.append(caractere)
                        self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
                                
            else: 
                self.__expressaoConvertida.append(caractere)
                self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))

        while len(pilha) != 0:
            self.__expressaoConvertida.append(pilha.pop())
            self.__passoAPasso.append((caractere, pilha.copy(), self.__expressaoConvertida.copy()))
        self.__expressaoAtual = ''.join(self.__expressaoConvertida)

    def conversorPreFixa(self, expressao: str):
        self.__expressaoConvertida = []
        self.__passoAPasso = []
        pilha = []
        posFixa = ConversorExpressao()
        posFixa.conversorPosFixa(expressao)
        self.__expressaoAtual = resultado = str(posFixa)
        for caractere in range(len(resultado) - 1, -1, -1):
            self.__expressaoConvertida.append(resultado[caractere])
            if caractere in self.__operadores:
                if self.__estaVazia(pilha):
                    while not self.__estaVazia(pilha) and self.prioridade(pilha[-1]) >= self.prioridade(caractere):
                        pilha.pop()
                            
                else:    
                    pilha.append(resultado[caractere])
            self.__passoAPasso.append((resultado[caractere], pilha.copy(), self.__expressaoConvertida.copy()))

    def __str__(self) -> str:
        return ''.join(self.__expressaoConvertida)