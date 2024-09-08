import hashlib
#Leer contraseña
contraseña = (input("Ingrese la contraseña: "))
# Crear un objeto hash SHA256
hash = hashlib.sha256()
# Agregar datos al objeto hash
hash.update(contraseña.encode('utf-8'))
# Obtener el valor de hash como una cadena hexadecimal
hash_hex = hash.hexdigest()
# Imprimir el valor de hash
print(hash_hex)
