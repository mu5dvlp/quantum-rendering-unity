import numpy as np
from qiskit import *

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def get_qubit_counts(length):
    return (length-1).bit_length()


def create_QuantumCircuit_by_Statevector(sv):
    n_qubits = int(np.log2(len(sv)))
    qc = QuantumCircuit(n_qubits,n_qubits)
    qc.initialize(sv,range(n_qubits))
    return qc


def convert_probability2statevector(probabilities,address):
    width = len(probabilities[0])
    height = len(probabilities)
    n_qubits = get_qubit_counts(width) + get_qubit_counts(height)
    statevector = np.zeros(2**n_qubits)
    for y in range(height):
        for x in range(width):
            index = int(address[y][x],2)
            statevector[index] = probabilities[y][x]
    return statevector