'''
Siendo "s" la cadena a analizar, y "D" el diccionario de palabras válidas:
c[n] = {
    True    si n = 0 
    True    si existe i perteneciente a [0, n) tal que c[i] = True && s[i:n] pertenece a D 
    False   si no existe tal i
}
'''

def algoritmo(s, D):
    n = len(s)
    dp = [False] * (n + 1)
    prev = [-1] * (n + 1)  # para la reconstrucción

    dp[0] = True  # caso base

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in D:
                dp[i] = True
                prev[i] = j  # guardamos índice inicial de la palabra que marcamos válida
                break  # para no seguir cortando

    return reconstruccion(s, prev, n)

def reconstruccion(s, prev, i):
    palabras = []

    if prev[i] == -1:
        return []  # no se pudo

    while i > 0:
        j = prev[i]
        palabras.append(s[j:i])
        i = j

    palabras.reverse()
    return palabras