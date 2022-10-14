def compEdad(num):
    mensaje = "Es menor de edad"
    if(2022-num >= 18):
        mensaje= "Es mayor de edad"
    return mensaje

def main():
    ano=int(input("Acontinuación digite (en números) el año en que nacio: "))

    mensaje = compEdad(ano)

    print(mensaje)

if __name__ == "__main__":
    main()
