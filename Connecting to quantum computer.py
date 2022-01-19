from qiskit import IBMQ
IBMQ.save_account("TOKEN HERE")
#output:Credentials already present. Set overwrite=True to overwrite.
#This saves on your actual machine, so you only need to do this once ever (unless your token changes), which is why I am getting the "Credentials already present" message.
#From then on, you can just do:
IBMQ.load_account()
#output:<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>
IBMQ.providers()
#[<AccountProvider for IBMQ(hub='ibm-q', group='open', project='main')>]
