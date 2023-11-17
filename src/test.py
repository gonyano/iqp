"""
Ref.
Sampler: https://qiskit.org/ecosystem/ibm-runtime/migrate/migrate-sampler.html#b-new-use-the-reference-sampler-or-aer-sampler-primitive
IQP: https://github.com/Qiskit/qiskit/blob/main/qiskit/circuit/library/iqp.py#L31
"""

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

from qiskit.circuit.library import IQP

A = [[6, 5, 3], [5, 4, 5], [3, 5, 1]]
circuit = IQP(A)
circuit.measure_all() # measurement!
circuit.decompose().draw('mpl', filename='./file.pdf')

sampler = Sampler()

result = sampler.run(circuit).result()
quasi_dists = result.quasi_dists

print("result: ", result)
print("quasi_dists: ", quasi_dists)
