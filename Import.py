#The tools we need
import qiskit as q
%matplotlib inline
#Qiskit allow us to make beautiful plots
from qiskit.visualization import plot_histogram
# simulator framework from qiskit
from qiskit import Aer
# will create a statevector of possibilities. 
sim_backend = Aer.get_backend('qasm_simulator')

