from clases.mago import Mago


merlin = Mago("Merlin", ["Rayo", "Bola de fuego"]) 
colombres = Mago("Colombres", ["Detener Tiempo", "Acabar con todo"]) 

print(merlin) # devuelve el metodo __str__ que habiamos generado
print(len(merlin))  # devuelve el mertodo __len__ que habiamos generado

print(colombres)
print(len(colombres))

print(merlin == colombres)

copia_merlin= Mago("Merlin", ["Rayo", "Bola de fuego"])

print (merlin == copia_merlin) # devuelve una comparacion usando los criterios que definimos en el metodo __eq__


mago_combinado = merlin + colombres
print(mago_combinado)