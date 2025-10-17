import psycopg2


   
connection = psycopg2.connect(host='localhost',user='DB_USER',password='DB_PASSW',port=5432,database='test_db')


try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = "UPDATE Persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = ("Juan Carlos", "Juarez", "jcjuarez@gmail.com", 1)
            cursor.execute(sentencia, valores)
            registro_actualizados = cursor.rowcount
            print(f"Registros Actualizados: {registro_actualizados}")
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:
    connection.close()
