from py2flowchart import pyfile2flowchart


prim_30 = 6.03
sec_90 = 6.19
sig_80 = 6.78
resto = 7.24

consumo_kw = int(input("Ingrese el consumo (KW) en el mes \n"))

consumo_acum = 0

while consumo_kw > 0:
    if ( consumo_kw < 30):
        consumo_acum = consumo_kw * prim_30
        consumo_kw = 0
        break
    if ( consumo_kw < 120):
        consumo_parcial =  consumo_kw - 30 
        consumo_acum = ( 30 * prim_30 ) + ( consumo_parcial *  6.19 )
        consumo_kw = 0
        break
    if ( consumo_kw < 200):
        consumo_parcial =  consumo_kw - 120
        consumo_acum = ( 30 * prim_30 ) + ( 90 * sec_90 ) + ( consumo_parcial *  6.78 )
        consumo_kw = 0
        break
    else:
        consumo_parcial =  consumo_kw - 200
        consumo_acum = ( 30 * prim_30 ) + ( 90 * sec_90 ) + ( 80 * sig_80 ) + ( consumo_parcial *  resto )
        consumo_kw = 0


print (consumo_acum)



