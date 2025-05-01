saldo = 100.0
debito = 50.0
credito = 200.0

print(f'daldo atual: R$ {saldo}')

#atualizando o saldo
saldo = saldo - debito + credito
print(f'saldo atual: R$ {saldo}')

if saldo <0:
    print('conta estourada!')
    print(f'saldo atual: R$ {saldo}')
else:
    print('conta ok!')