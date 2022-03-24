circuits=q.QuantumCircuit(5,5) #5 qubit,5 classical bits
circuits.x(0) #"x" is a not gate which flips the value,so here our first value is 0 which will flipped to 1
circuits.cx(0,1) #"cx" is a cnot gate which flips 2nd qubit if first qubit is 1
circuits.measure([0,1], [0,1])# ([qbitregister], [classicalbitregister]) Measure qubit 0 and 1 to classical bits 0 and 1
