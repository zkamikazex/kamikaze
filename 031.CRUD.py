import os #
import time #
import mysql.connector #conectar con base de datos

#crear conexion a la BD

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="0796",
    database="tiendaperu"
)

#para recorrer una tabla crearemos un objeto de tipo cursor

mycursor=mydb.cursor()

#creamos nuestro frontend
while True:
    print('-----MENU DEL SISTEMA ----'
    '\n1. Agregar un producto'
    '\n2. Eliminar un producto'
    '\n3. Buscar un producto'
    '\n4. Actualizar un producto'
    '\n5. Mostrar el catalogo del produtcto'
    '\n6. Salir del Sistema.')
    option=int(input('elige una opcion: '))

    #ahora programamos nuestro back end
    if option==1: #create (insertando datos en la tabla) 
        clave=input('Ingresa la clave del producto: ')
        nombre=input('Ingrese el nombre del producto: ')

        #crearemos la instruccion sql para insertar datos

        sql='INSERT INTO productos (clave, nombre) VALUES(%s,%s)'
        #guardamos los datos a insertar

        val=(clave,nombre)
        #listos para ejecutar la instruccion

        mycursor.execute(sql,val)

        #se realizaran cambios en la base de datos

        mydb.commit()

        #avisamos al usuario
        print(mycursor.rowcount, 'Registro modificado')

        #pausa de dos segundos
        time.sleep(2)
        #limpiamos pantalla
        os.system('cls')#linux o mac 'clear'
    elif option==2: #Delete (eliminar un registro en la tabla)
        clave=input('ingresa la clave del producto a eliminar: ')
        sql='DELETE FROM productos WHERE clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, 'Registro Eliminado')
        time.sleep(2)
        os.system('cls')

    elif option==3:
        clave=input('Ingresa la clave del producto que deseas buscar: ')
        sql='SELECT * FROM productos WHERE clave=%s'
        val=(clave,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        if myresult:
            print(f'El producto existe en la base de datos, Nombre: {myresult[1]}')
        else:
            print('El producto no existe en la base de datos')
        time.sleep(2)
        os.system('cls')
    elif option==4:
        clave=input('Ingresa la clave del producto a modificar: ')
        nombre=input('Ingresa el nuevo nombre del producto a modificar: ')
        sql='UPDATE productos SET nombre=%s WHERE clave=%s'
        val=(nombre,clave)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,'Regisro modificado')
        time.sleep(2)
        os.system('cls')
    elif option==5:
        mycursor.execute('SELECT * FROM productos')
        myresult=mycursor.fetchall()
        print('El catalogo de productos es:')
        for x in myresult:
            print(x)
            time.sleep(3)
        os.system('cls')
    elif option==6: #Salir
        respuesta=input('Estas seguro? (S/N): ')
        if respuesta.upper()=='S':
            print('Saliendo del sistema...')
            time.sleep(2)
            os.system('cls')
            
            break
            time.sleep(2)
            os.system('cls')
        else: #si escribe cualquier opcion que no sea de la 1 a la 6
                print('opción no válida, intenta de nuevo...')
                time.sleep(2)
                os.system('cls')
            #cerrar la conexion
mydb.close()

            




