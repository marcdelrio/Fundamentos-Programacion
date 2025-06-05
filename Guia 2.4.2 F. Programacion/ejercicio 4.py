estado = True
while estado:
    try:
        print("Regístrate para continuar")
        usuario = input("Registra tu correo electrónico: ")
        arroba = 0
        contador = 0

        while contador < len(usuario):
            if usuario[contador] == '@':
                arroba += 1
            contador  += 1

        if arroba == 0 or arroba > 1:
            raise ValueError("El correo no es valido.")
        
        password = input("Ingrese una clave entre 10 a 20 caracteres: ")

        while len(password) < 10 or len(password) > 20:
            print("La contraseña no es válida.")
            password = input("Ingrese una clave entre 10 a 20 caracteres: ")

        user = usuario
        clave = password

        print("***************************************************") 
        print("Loguéate para continuar")
        usuario = input("Ingresa tu usuario: ")
        password = input("Ingresa tu contraseña: ")

        if usuario != user and password != clave:
            print(" Bienvenid@!!")
        else:
            print("El usuario o la clave no están registrado")
            
        
        estado = False

    except ValueError:
        print("Los valores ingresados no son válidos.")
    finally:
        print("Gracias por utilizar nuestra App.")