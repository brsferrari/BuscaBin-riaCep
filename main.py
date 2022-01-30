import struct
import sys
import os

cepprocurado = input("Entre com o CEP que deseja encontrar: ")
print(f"O cep que você está procurando: {cepprocurado}")

#Estrutura do meu arquivo de dados
registroCEP = struct.Struct("72s72s72s72s2s8s2s")

#Abrindo o arquivo para leitura como f
with open("cep_ordenado.dat","rb") as f:
    #Anda com o curso do começo ao fim do arquivo e retorna seu tamanho
    f.seek(0,os.SEEK_END)
    tamanho = f.tell()
    print( f"O tamanho do arquivo: {tamanho}")

    #Tamanho dos registros
    print (f"Tamanho da Estrutura: {registroCEP.size}")

    #Pegando o tamanho do arquivo e divindo pelo tamanho de cada registro para saber a qtd de registros
    n = tamanho // registroCEP.size
    print( f"A quantidade de registros: {n}")

    #Busca Binária
    primeiro = 0
    ultimo = n-1
    while primeiro <= ultimo:
        meio = (primeiro+ultimo) // 2
        f.seek(meio * registroCEP.size)
        line = f.read(registroCEP.size)
        if len(line) == registroCEP.size:
            registro = registroCEP.unpack(line)
            cep = registro[5].decode()
        if cep == cepprocurado:
            print(f"Você encontrou seu cep! Ele está na posição {meio}")
            break
        else :
            if cepprocurado < cep:
                ultimo = meio - 1
            else :
                primeiro = meio + 1
