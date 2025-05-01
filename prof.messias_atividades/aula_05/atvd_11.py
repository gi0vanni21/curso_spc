quant_max = 1000
quant_min = 100

quant_real = 497

quant_media = (quant_max + quant_min) / 2

if quant_real < quant_media:
    print("realize uma compra para o estoque!")
else:
    print("não é necessaria uma compra!")