from qiskit import *
from qiskit_aer import Aer
import numpy as np

import cv2

from common_logic import *
from common_quantum import *

# //＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
class Provider:
    def __init__(self,shot_count=20000):
        self.shot_count = shot_count


    def append_rxBlur(self,theta):
        for i in range(self.n_qubits):
            self.qc.rx(theta,i)

    
    def appned_measure(self):
        self.qc.measure(range(self.n_qubits),range(self.n_qubits))


    def set_image(self,image):
        self.gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.width = len(self.gray_image[0])
        self.height = len(self.gray_image)
        self.w_qubits = get_qubit_counts(self.width)
        self.h_qubits = get_qubit_counts(self.height)
        self.n_qubits = self.w_qubits + self.h_qubits
        self.qc = self._init_quantum_circuit()


    def _init_quantum_circuit(self):
        probabilities = create_matrix(self.width,self.height)
        for y in range(self.height):
            for x in range(self.width):
                probabilities[y][x] = np.sqrt(self.gray_image[y][x]/np.sum(self.gray_image))

        self.address = gray_code_2d(self.width,self.height)
        state_init = convert_probability2statevector(probabilities,self.address)
        qc = create_QuantumCircuit_by_Statevector(state_init)
        return qc
    

    def execute_backend(self):
        backend = Aer.get_backend("qasm_simulator")
        result = backend.run(self.qc, shots=self.shot_count).result()
        return result


    def convert_count_to_image(self,counts):
        image_quantumOutput = create_matrix(self.width,self.height)
        for key,value in counts.items():
            x = gray_to_decimal(key[:self.w_qubits])
            y = gray_to_decimal(key[self.w_qubits:])
            val = clamp(float(np.sqrt(value*np.sum(self.gray_image)/(self.shot_count*255)))*255, 0, 255)
            if(x<self.width and y<self.height):
                image_quantumOutput[y][x] = val
        return image_quantumOutput