class CompressedGene():
    def __init__(self, gene: str):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string: int = 1
        for nucleotideo in gene.upper():
            self.bit_string <<= 2
            if nucleotideo == "A":
                self.bit_string |= 0b00
            elif nucleotideo == "C":
                self.bit_string |= 0b01
            elif nucleotideo == "G":
                self.bit_string |= 0b10
            elif nucleotideo == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid nucleotideo: {nucleotideo}")

    def decompress(self) -> str :
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits : int = self.bit_string >> i & 0b11  #obtem apenas 2 bits relevantes
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalit bit: {bits:b}")
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGAAGGCCATGCTCGATAAATTCGCTAGTCGTAGTGCGCGGGCCCTTTATATTATATTCGCGCGGAGCGCGGATCGCTGATCGCTAGCTGCTGTGTTTCGGGAAAGCCCC" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed : CompressedGene = CompressedGene(original)
    print("compressed gene is {} bytes".format(getsizeof(compressed)))
    print("original == compressed", original == compressed.decompress())
