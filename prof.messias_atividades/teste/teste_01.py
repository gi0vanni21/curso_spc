import time
from loguru import logger

# criando um menu para meus códigos
print('---Iniciando o progeama---')

# menu
while True:
    print('1 - cadastra o nome')
    print('2 - altera o nome')
    print('3 - sair')
    opcao =int(input('digite a opção desejada: '))

    match opcao:
        case 1:
            logger.info('o nome foi cadastrado!')
        case 2:
            logger.info('o nome foi alterado!')
        case 3:
            logger.warning('saindo do programa') 
            break
 
    logger.info('menu finalizado')