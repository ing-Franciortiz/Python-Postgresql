import psycopg2

print("🔄 Iniciando conexión...")

try:
    connection = psycopg2.connect(
        host='localhost',
        user='DB_USER',
        password='DB_PASSW',
        port=5432,
        database='test_db'
    )
    print("✅ Conectado correctamente a la base de datos.")

    with connection:
        with connection.cursor() as cursor:
            print("🧩 Cursor creado correctamente.")

            sentencia = "UPDATE Persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = [
                ("Juan Carlos", "Juarez", "jcjuarez@gmail.com", 1),
                ("Miguel", "Rodríguez", "pedro@gmail.com", 2)
            ]

            total_actualizados = 0
            for valor in valores:
                print("➡️ Ejecutando UPDATE con:", valor)
                cursor.execute(sentencia, valor)
                total_actualizados += cursor.rowcount
                print(f"   ↳ Afectó {cursor.rowcount} fila(s)")

            print(f"✅ Total de registros actualizados: {total_actualizados}")

except Exception as e:
    print(f"❌ Error detectado: {e}")

finally:
    if 'connection' in locals():
        connection.close()
        print("🔒 Conexión cerrada.")
