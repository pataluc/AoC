def load(file):
    return open(file, "r").readlines()[0].strip()

def hex_to_binary( hex_code ):
    b =  bin(int(hex_code, 16))[2:]
    padding = (4-len(b)%4)%4
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

sample = load("sample.txt")
input = load("input.txt")

bin_number = hex_to_binary("D2FE28")
assert bin_number == "110100101111111000101000"
assert get_packet_version(bin_number) == 6
assert get_packet_type(bin_number) == 4
literal, leftover = get_literal(bin_number)
assert literal == 2021


bin_number = hex_to_binary("38006F45291200")
assert bin_number == "00111000000000000110111101000101001010010001001000000000"
assert get_packet_version(bin_number) == 1
assert get_packet_type(bin_number) == 6

def parse_packet(packet, packets = []):
    version = get_packet_version(packet)
    type_id = get_packet_type(packet)

    packets.append(packet)

    if type_id == 4:
        value, leftover = get_literal(packet)
        #print("-------- packet literal: %s, version: %d, type_id: %d, value: %d, leftover: %s" % (packet, version, type_id, value, leftover))
        return packets, leftover
    else:
        if packet[6] == "0": # length type 0, number of bits in subpackets
            subpackets_length = int(packet[7:22], 2)
            #print("########\npacket operator: %s, version: %d, type_id: %d, %s bits of subpackets" 
            #    % (packet, version, type_id, subpackets_length))
            
            l = packet[22:22 + subpackets_length]
            r = packet[22 + subpackets_length:]
            while len(l) > 10 :
                #print("--------------- %s" % l)
                packets, l = parse_packet(l, packets)
            return packets, r
        else:                # length type 1, number of subpackets
            subpackets_nb = int(packet[7:18], 2)
            #print("########\npacket operator: %s, version: %d, type_id: %d, %s subpackets embedded" 
            #    % (packet, version, type_id, subpackets_nb))
            
            l = packet[18:]
            for i in range(subpackets_nb):
                #print("-------------%d-- %s" % (i, l))
                packets, l = parse_packet(l, packets)
                
            return packets, l

def ex1(string):
    #print("\n\n\n%s" % string)
    packets = parse_packet(hex_to_binary(string), [])

    #print("#####\nresult")

    #print(list(map(lambda p: (p, get_packet_version(p)), packets[0])))
    #print(sum(map(get_packet_version, packets[0])))

    return sum(map(get_packet_version, packets[0]))

#type 0
assert ex1("38006F45291200") == 9
#type 1
assert ex1("EE00D40C823060") == 14


assert ex1("8A004A801A8002F478") == 16
assert ex1("620080001611562C8802118E34") == 12
assert ex1("C0015000016115A2E0802F182340") == 23
assert ex1("A0016C880162017C3686B18A3D4780") == 31


print("ex1 : %d" % ex1(input))
exit()


assert method(sample, 5) == 315
#print("ex2 : %d" % method(input, 5))