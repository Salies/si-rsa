# Atividade 2 do 2o bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Função principal

from zane import rsa_keys

def main():
    pub_key, priv_key = rsa_keys()
    print("Chave pública: ", pub_key)
    print("Chave privada: ", priv_key)

if __name__ == "__main__":
    main()