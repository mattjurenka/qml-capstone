from qiskit import QuantumCircuit

#params must have a length of 4 * n_wires
def get_ansatz(n_wires: int, params: list[float]) -> QuantumCircuit:
    qc = QuantumCircuit(n_wires)
    for i in range(n_wires):
        qc.rx(params[i], i)
        qc.ry(params[i + n_wires], i)
        qc.rz(params[i + 2*n_wires], i)
    for i in range(n_wires):
        qc.crx(params[i + 3*n_wires], i, (i + 1) % n_wires)
    return qc
