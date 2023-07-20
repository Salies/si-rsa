# Atividade 2 do 2o bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Biblioteca "Zane" para criação do RSA

# numpy APENAS para geração de números e cálculos
import numpy as np

RANDOM_SEED = 666

# Função principal
# Baseada em: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
# Retorna as chaves pública e privada
def rsa_keys():
    np.random.seed(RANDOM_SEED)
    primes = sieve(1000) # gera primos até 1k
    primes = primes[primes > 500] # pega só os maiores que 500
    # escolhe dois primos grandes aleatórios
    p, q = np.random.choice(primes, 2, replace=False)
    # calcula n
    n = p * q
    # calcula o totiente de Euler
    totient = int(phi(p, q))
    # calcula o expoente público
    # ele precisa ser coprimo com o totiente
    # e menor que o totiente
    while(True):
        e = np.random.randint(2, totient)
        if gcd(e, totient) == 1:
            break
    # calcula o expoente privado
    # ele precisa ser o inverso multiplicativo de e
    # módulo o totiente
    d = pow(e, -1, totient)
    # retorna as chaves pública e privada
    return (n, e), d

# Função genérica para o crivo de Eratóstenes
# (geração de primos)
def sieve(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0:2] = False
    p = 2

    while p * p <= limit:
        if sieve[p]:
            sieve[p * p::p] = False
        p += 1

    return np.nonzero(sieve)[0]

# Função de totiente de Euler
# O artigo da Wikipedia usa o totiente de Carmichael
# mas o paper do RSA usa o de Euler
def phi(p, q):
    return (p - 1) * (q - 1)

# Função de maior divisor comum, usada no lcm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a