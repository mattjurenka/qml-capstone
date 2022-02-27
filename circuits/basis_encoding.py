from qiskit import QuantumCircuit


def get_basis_encoding(x: int) -> QuantumCircuit:
    circuits = len(bin(x))
    initial = [0,1]
    qc = QuantumCircuit(circuits - 2)
    for i in range(0, circuits - 2):
        qc.initialize(initial, i)
    return qc
