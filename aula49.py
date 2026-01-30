numero_str = input ("digite um numero que eu dobro ele : ")

try: 
    numero_float = float(numero_str)
    print("STR:" , numero_str)
    print("FLOAT" , numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.1f}')

except: 

    print("isso não é um numero")









#if numero_float : 
#    print(f'o dobro de {numero_str} é {numero_float * 2:.1f}')
#else: 
#    print("escreva algo ai po")
#lembrando que as chaves server para inserir valores dentro de strings sem fechar aspas toda hora , tambem serve para dados associados a string .
