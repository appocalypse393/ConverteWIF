import hashlib
import base58


def convert_to_wif(private_key_hex):
    # Passo 1: Adiciona prefixo para chave privada
    prefix = '80' + private_key_hex

    # Passo 2: Adiciona 0x01 para compactar
    prefix_compact = prefix + '01'

    # Passo 3: Cria o checksum
    hash1 = hashlib.sha256(bytes.fromhex(prefix_compact)).hexdigest()
    hash2 = hashlib.sha256(bytes.fromhex(hash1)).hexdigest()
    checksum = hash2[:8]

    # Passo 4: Cria o WIF completo
    wif = prefix_compact + checksum

    # Passo 5: Codifica em Base58
    wif_encoded = base58.b58encode(bytes.fromhex(wif)).decode('utf-8')

    return wif_encoded


# Exemplo de uso
private_key_hex = 'Insira sua chave privada aqui'
wif_key = convert_to_wif(private_key_hex)
print("Chave WIF compactada:", wif_key)
