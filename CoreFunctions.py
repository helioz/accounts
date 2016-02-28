


def clientPays(clientId,amount,notes):
    updateClientBalance(clientId)
    insertToClientTransactions(clientId,amount,notes)

def servicesPaid(serviceId,clientId,amount):
    
