#!/bin/python
from circuits.basis_encoding import get_basis_encoding
from circuits.ansatz import get_ansatz

from sys import argv

encoding = get_basis_encoding(int(argv[1]))
ansatz = get_ansatz(4)

print(encoding, ansatz)
