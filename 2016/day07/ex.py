from os import path
from sys import argv
import re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def has_abba(ip_chunk: str):
    for i in range(len(ip_chunk) - 3):
        dprint(ip_chunk[i], ip_chunk[i+1], ip_chunk[i+2], ip_chunk[i+3])
        if ip_chunk[i] == ip_chunk[i+3] and ip_chunk[i+1] == ip_chunk[i+2] and ip_chunk[i] != ip_chunk[i+1]:
            return True
    return False

def finds_aba(ip_chunk: str):
    abas = []
    for i in range(len(ip_chunk) - 2):
        if ip_chunk[i] == ip_chunk[i+2] and ip_chunk[i] != ip_chunk[i+1]:
            abas.append(ip_chunk[i:i+3])
    return abas


def supports_tls(ip: str):
    insides = '|'.join(re.findall(r'\[(\w*)\]', ip))
    outsides = re.sub(r'\[(\w*)\]', ',', ip)

    return not has_abba(insides) and has_abba(outsides)

def supports_ssl(ip: str):
    insides = '|'.join(re.findall(r'\[(\w*)\]', ip))
    outsides = re.sub(r'\[(\w*)\]', ',', ip)

    for aba in finds_aba(insides):
        if aba[1]+aba[0]+aba[1] in outsides:
            return True
    return False


def ex1(data):
    lines = data.split('\n')
    return len(list(filter(supports_tls, lines)))


def ex2(data):
    lines = data.split('\n')
    return len(list(filter(supports_ssl, lines)))


assert supports_tls('abba[mnop]qrst')
assert not supports_tls('abcd[bddb]xyyx')
assert not supports_tls('aaaa[qwer]tyui')
assert supports_tls('ioxxoj[asdfgh]zxcvbn')
print("ex1 : %s" % ex1(load("input.txt")))

assert supports_ssl('aba[bab]xyz')
assert not supports_ssl('xyx[xyx]xyx')
assert supports_ssl('aaa[kek]eke')
assert supports_ssl('zazbz[bzb]cd')
print("ex2 : %s" % ex2(load("input.txt")))
