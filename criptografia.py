from Crypto.Cipher import AES
from Crypto.Hash  import SHA256
from unicodedata import normalize
#Biblioteca 

#input de entrada
senha = input("Digite a senha ")

# normalmente hash é padrão  diferente do sals fiz só para mostra que senha a pessoa pode escolher ;
# no arquivos de criptografia explica oque hash e sals 
#condifica com hash para tamanho fixo
hash_obj = SHA256.new(senha.encode('utf-8'))
hkey = hash_obj.digest()
cifra = AES.new(hkey)



#input de entrada
msg = input("Digite uma mensagem: ")
#remover simbolo com a tabela ascii
msgR = normalize('NFKD', msg).encode('ASCII','ignore').decode('ASCII')

#pad é para verificar se a palavra é do tamanho 16 for menor completa com '{'

def pad(s):
    return s + ((16 -len(s) % 16) * '{')

#encrypt vai pegar a msg verificada com tamanho    
def encrypt(plaintext):
    global cifra
    return cifra.encrypt(pad(plaintext))

#vai decriptografa com separado os { da palavra original
def decrypt(ciphertext):
    global cifra
    dec = cifra.decrypt(ciphertext).decode('utf-8')
    l = dec.count('{')
    return dec[:len(dec)-l]


#é oque o botão de encrypt e decrypty vai fazer 

a = encrypt(msgR)
b = decrypt(a) 

print(a)
print(b)