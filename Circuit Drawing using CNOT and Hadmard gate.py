circuits = q.QuantumCircuit(5,5)  # 2 qbits, 2 classical bits.
circuits.h(0) # Hadamard gate, puts qubit 0 into superposition
circuits.cx(0, 1) #cnot, controlled not, Flips 2nd qubit's value if first qubit is 1
circuits.measure([0,1], [0,1])
