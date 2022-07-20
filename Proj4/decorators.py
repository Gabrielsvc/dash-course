
# Conceito de decoradores
def soma_um(numero):
    return numero + 1

# Variável como função
f1 = soma_um
a = f1(1)
print(f1, a)

# Definindo funções dentro de outras
def soma_dois(numero):
    def divide_dois(numero):
        return numero/2
    return numero+2
soma_dois(4)

# Funções como argumentos
def soma_um(numero):
    return numero+1

def function_call(function):
    numero_adicionado = 10
    return function(numero_adicionado)

function_call(soma_um)

# Funções podem retornar funções
def fun1():
    def fun2():
        return "oi"
    return fun2
oi = fun1()
oi()

# Decorador
def decorador_maiusculo(function):
    cria_maiuscula = function().upper()
    return cria_maiuscula

def diga_oi():
    return 'oiiii'

decorador_maiusculo(diga_oi)

# Ou podemos fazer isso
@decorador_maiusculo
def diga_oi():
    return 'ola ola'
diga_oi
