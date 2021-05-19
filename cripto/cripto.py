from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    #gera length bytes pseudo-aleatorios
    tb: bytes = token_bytes(length)
    # convert esse bytes em uma cadeia de bits e a devolve
    return int.from_bytes(tb, "big")

def _test_xor():
    """Se os bits de dois números forem combinados com XOR,
    umr propriedade conveniente é que o produto (resultado)
    pode ser recombinado com um dos operandos para gerar o 
    outro operando.
    """
    A = 0b010010
    B = 0b011110
    C = A ^ B
    A1 = C ^ B
    B1 = A ^ C

    print(f"A         = {A:b}")
    print(f"B         = {B:b}")
    print(f"C (A ^ B) =  {C:b}")
    print(f"    C ^ B = {A1:b} == A")
    print(f"    A ^ C = {B1:b} == B")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted = key1 ^ key2 
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":

    _test_xor()

    key, encripted = encrypt('One Time Pad')
    print(f"{key:b}")
    print(f"{encripted:b}")
    result: str = decrypt(key, encripted)

    print(result)



