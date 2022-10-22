print("LISTAS")
print("----------------------")
#Lista
print("Creación de una lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
print(materias)
print("----------------------")
materias = list(("Cálculo", "Álgebra Lineal", "Química"))
#Cambiar elemento de la lista
print("Cambiar un elemento de la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias[2]="Fundamentos de programación"
print(materias)
print("----------------------")
#Agregar un alemento a las lista
print("1. Agregar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.append("Fundamentos de programación")
print(materias)
print("2. Agregar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.insert(0,"Fundamentos de programación")
print(materias)
print("3. Agregar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias2 = ["Fundamentos de programación","Cátedra UIS","Taller de Lenguaje", 1, 2, 3, 4]
materias.extend(materias2)
print(materias)
print("4. Agregar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
tupla_materias = ("Fundamentosde programación", )
materias.extend(tupla_materias)
print(materias)
print("----------------------")
#Eliminar un elemento de la lista
print("1. Eliminar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.remove("Cálculo")
print(materias)
print("2. Eliminar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.pop(1)
print(materias)
print("3. Eliminar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.pop()
print(materias)
print("4. Eliminar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
del materias[0]
print(materias)
print("5. Eliminar un elemento a la lista")
materias = ["Cálculo", "Álgebra Lineal", "Química"]
materias.clear()
print(materias)