def load(file):
    return open(file, "r").readlines()[0].strip()

def hex_to_binary( hex_code ):
    b =  bin(int(hex_code, 16))[2:]
    padding = 4 * len(hex_code) - len(b)
    return '0'*padding + b

def get_packet_version(packet):
    return int(packet[:3], 2)

def get_packet_type(packet):
    return int(packet[3:6], 2)

def get_literal(packet):
    v = packet[6:]
    r = ""
    i = 0
    while True:
        s = v[i*5:i*5+5]
        r += s[1:]
        if s[0] == "0":
            return int(r, 2), v[i*5+5:]
        i += 1

def get_literal_only(packet):
    return get_literal(packet)[0]

bin_number = hex_to_binary("D2FE28")
assert bin_number == "110100101111111000101000"
assert get_packet_version(bin_number) == 6
assert get_packet_type(bin_number) == 4
literal, leftover = get_literal(bin_number)
assert literal == 2021

assert hex_to_binary("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"
assert get_packet_version(hex_to_binary("38006F45291200")) == 1
assert get_packet_type(hex_to_binary("38006F45291200")) == 6

def array_prod(array):
    produit = 1
    for element in array:
        produit = produit*element
    return produit

operations = {
    0: ("somme", sum),
    1: ("produit", array_prod),
    2: ("min", min),
    3: ("max", max),
    5: ("plus grand", lambda x: 1 if x[0] > x[1] else 0),
    6: ("plus petit", lambda x: 1 if x[0] < x[1] else 0),
    7: ("egal", lambda x: 1 if x[0] == x[1] else 0)
}

def evaluate(list, operation):
    return operations[operation][1](list)


def parse_packet(packet, packets = [], version = 0, inc = -1):
    inc += 1
    version += get_packet_version(packet)
    type_id = get_packet_type(packet)

    packets.append(packet)

    if type_id == 4:
        value, leftover = get_literal(packet)
        return packets, leftover, version, value
    else:
        sub_packets_values = []
        if packet[6] == "0": # length type 0, number of bits in subpackets
            subpackets_length = int(packet[7:22], 2)
            
            l = packet[22:22 + subpackets_length]
            r = packet[22 + subpackets_length:]
            while len(l) > 10 :
                packets, l, version, v = parse_packet(l, packets, version, inc)
                sub_packets_values.append(v)
            return packets, r, version, evaluate(sub_packets_values, get_packet_type(packet))
        else:                # length type 1, number of subpackets
            subpackets_nb = int(packet[7:18], 2)
             
            l = packet[18:]
            for i in range(subpackets_nb):
                packets, l, version, v = parse_packet(l, packets, version, inc)
                sub_packets_values.append(v)
            
            return packets, l, version, evaluate(sub_packets_values, get_packet_type(packet))

def ex1(string):
    result = parse_packet(hex_to_binary(string), [])
    return result[2]


def ex2(string):
    result = parse_packet(hex_to_binary(string), [])
    return result[3]


input = load("input.txt")
assert ex1("38006F45291200") == 9
assert ex1("EE00D40C823060") == 14
assert ex1("8A004A801A8002F478") == 16
assert ex1("620080001611562C8802118E34") == 12
assert ex1("C0015000016115A2E0802F182340") == 23
assert ex1("A0016C880162017C3686B18A3D4780") == 31
print("ex1 : %d" % ex1(input))

assert ex2("C200B40A82") == 3
assert ex2("04005AC33890") == 54
assert ex2("880086C3E88112") == 7
assert ex2("CE00C43D881120") == 9
assert ex2("D8005AC2A8F0") == 1
assert ex2("F600BC2D8F") == 0
assert ex2("9C005AC2F8F0") == 0
assert ex2("9C0141080250320F1802104A08") == 1
print("ex2 : %d" % ex2(input))
