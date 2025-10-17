import psycopg2


   
connection = psycopg2.connect(host='localhost',user='DB_USER',password='DB_PASSW',port=5432,database='test_db')


try:
    with connection:
        with connection.cursor() as cursor:
           sentencia = "INSERT INTO Persona(nombre, apellido, email) VALUES(%s, %s, %s)"
           valores = (
              ("Carlos", "Lara", "clara@.gmail.com"),
              ("Jose", "Manuel", "jmanuel@gmail.com"),
              ("marcos", "Cantu", "cmarcos@gamil.com")
           )
           cursor.executemany(sentencia, valores)
           registros_insertados = cursor.rowcount
           print(f"Registros Insertados: {registros_insertados}")

except Exception as e:
    print(f"Ocurrio un error {e}")
finally:
    connection.close()
