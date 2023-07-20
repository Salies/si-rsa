# Atividade 2 do 2o bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Função principal

from zane import rsa_keys, encrypt, decrypt

def main():
    # aqui passo uma seed, apenas para consistência nos testes
    pub_key, priv_key = rsa_keys(666)
    print("Chave pública (n ,e): ", pub_key)
    print("Chave privada (n, d): ", priv_key)

    msg = "Fulminus"

    print("Mensagem original: ", msg)

    # codifica a mensagem
    enc_msg = encrypt(msg, pub_key)
    print("Mensagem codificada: ", enc_msg)

    # decodifica a mensagem
    dec_msg = decrypt(enc_msg, priv_key)
    print("Mensagem decodificada: ", dec_msg)

if __name__ == "__main__":
    main()