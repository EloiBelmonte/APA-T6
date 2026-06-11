"""
Práctica de Expresiones Regulares
Autor: Eloi Belmonte Alcalá

Este fichero contiene la función normalizaHoras(), encargada de buscar
diferentes expresiones horarias en un texto y normalizarlas al formato 
estándar HH:MM, siguiendo las reglas de la guía de estilo PEP 8.
"""

import re


def calcular_hora_periodo(hora, periodo):
    """
    Función auxiliar para validar y ajustar la hora según el periodo del día.
    Devuelve la hora en formato 24h (0-23) o None si la combinación es incorrecta.
    """
    # 1. Validar periodos según las reglas del enunciado
    if periodo == 'de la mañana' and not (4 <= hora <= 12):
        return None
    if periodo == 'del mediodía':
        if hora != 12 and not (1 <= hora <= 3):
            return None
    if periodo == 'de la tarde' and not (3 <= hora <= 8):
        return None
    if periodo == 'de la noche' and (hora != 12 and not (1 <= hora <= 4) and not (8 <= hora <= 11)):
        return None
    if periodo == 'de la madrugada' and not (1 <= hora <= 6):
        return None

    # 2. Ajuste de formato 12h a 24h
    if periodo == 'de la noche' and hora == 12:
        return 0  # 12 de la noche son las 00:00 estrictas
    
    if periodo in ['de la tarde', 'de la noche', 'del mediodía']:
        if hora < 12:
            hora += 12
            
    return hora


def procesar_linea(linea):
    """
    Analiza una línea de texto y reemplaza las expresiones horarias válidas.
    """
    # -------------------------------------------------------------------------
    # CASO 1: Formato estándar ya existente (HH:MM) -> Ej: 18:30 o 4:45
    # -------------------------------------------------------------------------
    patron_estandar = r'\b([0-1]?\d|2[0-3]):([0-5]\d)\b'
    
    def repl_estandar(match):
        h = int(match.group(1))
        m = int(match.group(2))
        return f"{h:02d}:{m:02d}"
    
    linea = re.sub(patron_estandar, repl_estandar, linea)

    # -------------------------------------------------------------------------
    # CASO 2: Formatos con franja del día (Ej: 4 y media de la tarde, 5 menos cuarto)
    # Corregido el orden: primero 1[0-2] y luego [1-9]
    # -------------------------------------------------------------------------
    patron_media = r'\b(1[0-2]|[1-9])\s+y\s+media\s+(de la mañana|del mediodía|de la tarde|de la noche|de la madrugada)\b'
    def repl_media(match):
        h = int(match.group(1))
        periodo = match.group(2)
        h_ajustada = calcular_hora_periodo(h, periodo)
        return f"{h_ajustada:02d}:30" if h_ajustada is not None else match.group(0)
    linea = re.sub(patron_media, repl_media, linea)

    patron_menos_cuarto = r'\b(1[0-2]|[1-9])\s+menos\s+cuarto\b'
    def repl_menos_cuarto(match):
        h = int(match.group(1))
        h_real = 12 if h == 1 else h - 1
        return f"{h_real:02d}:45"
    linea = re.sub(patron_menos_cuarto, repl_menos_cuarto, linea)

    # -------------------------------------------------------------------------
    # CASO 3: Formato XhYm o Xh (Ej: 8h27m, 8h)
    # -------------------------------------------------------------------------
    patron_hm = r'\b([0-1]?\d|2[0-3])h([0-5]?\d)m\b'
    def repl_hm(match):
        h = int(match.group(1))
        m = int(match.group(2))
        return f"{h:02d}:{m:02d}"
    linea = re.sub(patron_hm, repl_hm, linea)

    # Corregido el espacio final cambiando \b por un lookahead (?=\s|$) para respetar la 'y'
    patron_h_sola = r'\b([0-1]?\d|2[0-3])h(?:\s+(de la mañana|del mediodía|de la tarde|de la noche|de la madrugada))?(?=\s|$)'
    def repl_h_sola(match):
        h = int(match.group(1))
        periodo = match.group(2)
        if periodo:
            h_ajustada = calcular_hora_periodo(h, periodo)
            return f"{h_ajustada:02d}:00" if h_ajustada is not None else match.group(0)
        return f"{h:02d}:00"
    linea = re.sub(patron_h_sola, repl_h_sola, linea)

    # -------------------------------------------------------------------------
    # CASO 4: Formato "X en punto" o "X de la ..." (Ej: 12 de la noche)
    # Corregido el orden a (1[0-2]|[1-9])
    # -------------------------------------------------------------------------
    patron_palabras = r'\b(1[0-2]|[1-9]|2[0-3])\s+(en punto|de la mañana|del mediodía|de la tarde|de la noche|de la madrugada)\b'
    def repl_palabras(match):
        h = int(match.group(1))
        complemento = match.group(2)
        
        if complemento == "en punto":
            if h > 12:
                return match.group(0)
            return f"{h:02d}:00"
        else:
            h_ajustada = calcular_hora_periodo(h, complemento)
            return f"{h_ajustada:02d}:00" if h_ajustada is not None else match.group(0)
            
    linea = re.sub(patron_palabras, repl_palabras, linea)

    return linea


def normalizaHoras(ficText, ficNorm):
    """
    Lee el fichero ficText, busca expresiones horarias, las normaliza
    y escribe el resultado en ficNorm.
    """
    f_entrada = open(ficText, 'r', encoding='utf-8')
    f_salida = open(ficNorm, 'w', encoding='utf-8')

    for linea in f_entrada:
        linea_normalizada = procesar_linea(linea)
        f_salida.write(linea_normalizada)

    if linea_normalizada and not linea_normalizada.endswith('\n'): # Para que haya un espacio después de que termine de imprimir el archivo por pantalla
        f_salida.write('\n')
        
    f_entrada.close()
    f_salida.close()


if __name__ == '__main__':
    import sys  # Importamos sys para poder capturar el '-h'
    
    # Si el usuario escribe '-h' en la terminal de Linux
    if len(sys.argv) > 1 and sys.argv[1] == '-h':
        print(__doc__)  # Muestra tu nombre y la descripción del ejercicio 2
        
    else:
        # Si no pone '-h', el programa funciona de manera normal y procesa el archivo
        print("Normalizando el fichero 'horas.txt'...")
        try:
            normalizaHoras('horas.txt', 'horas_norm.txt')
            print("¡Fichero normalizado con éxito! Guardado en 'horas_norm.txt'")
        except FileNotFoundError:
            print("Error: No se encuentra el archivo 'horas.txt' para hacer la prueba.")