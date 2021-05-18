
def show(bit):
    print(f"{bit:b} {bit.bit_length()} bits")

bit_string: int = 1
show(bit_string)

bit_string <<= 2
show(bit_string)

bit_string <<= 2
bit_string |= 0b00
show(bit_string)

bit_string <<= 2
bit_string |= 0b01
show(bit_string)

bit_string <<= 2
bit_string |= 0b10
show(bit_string)

bit_string <<= 2
bit_string |= 0b11
show(bit_string)

print("volta")

bts = bit_string >> 0 & 0b11
show(bts)

bts = bit_string >> 2 & 0b11
show(bts)

bts = bit_string >> 4 & 0b11
show(bts)

bts = bit_string >> 6 & 0b11
show(bts)
