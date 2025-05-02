'''
Siendo:
- "s" la cadena a analizar
- "c[n]" un booleano que indica si la subcadena s[0:n] puede segmentarse completamente en palabras válidas
- "D" el diccionario de palabras válidas

c[n] = {
    True    si n = 0 
    True    si existe i perteneciente a [0, n) tal que c[i] = True && s[i:n] pertenece a D 
    False   si no existe tal i
}
'''

def algoritmo(s, D):
    n = len(s)
    c = [False] * (n + 1)
    indices = [-1] * (n + 1)  # para la reconstrucción

    c[0] = True  # caso base

    for i in range(1, n + 1):
        for j in range(i):
            
            if c[j] and s[j:i] in D:
                c[i] = True
                indices[i] = j  # guardamos índice inicial de la palabra que marcamos válida
                break  # para no seguir cortando

    return reconstruccion(s, indices, n)

def reconstruccion(s, indices, i):
    palabras = []

    if indices[i] == -1:
        return []  # no se pudo

    while i > 0:
        j = indices[i]
        palabras.append(s[j:i])
        i = j

    palabras.reverse()
    return palabras