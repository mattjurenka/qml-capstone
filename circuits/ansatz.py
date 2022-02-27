from qiskit import QuantumCircuit

def get_ansatz(n_wires: int) -> QuantumCircuit:
    qc = QuantumCircuit(n_wires)
    return qc
