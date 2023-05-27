import time

def menu():
    peso = float(input('Insert your weight (kg): '))
    estatura = float(input('insert your height: '))
    
    return peso / (estatura ** 2)

def barra_progreso(segmento, total,longitud):
    porcentaje = segmento / total
    restante = longitud - segmento
    barra = f"[{'#' * segmento}{'.' * restante}] {porcentaje:.2%}"
    
    return barra
    
total = 40  

def main():
    
    promedio = menu()
    for e in range(total + 1):
        time.sleep(0.05)
        if e < total:
            print(barra_progreso(e, total, 40), end = '\r')
        else:
            print(barra_progreso(e,total,40))
    
    print('Your IMC is:', round(promedio , 3))
        
        
    

if __name__ == '__main__':
    main()