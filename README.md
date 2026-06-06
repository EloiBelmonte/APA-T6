# Expresiones Regulares

## Eloi Belmonte Alcalá

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Eloi Belmonte Alcalá

## Aviso Importante

> [!Caution]
> 
> El objetivo de esta tarea es aprender a usar las expresiones regulares. En concreto, su
> implementación en Python. A los profesores de la asignatura les importa un pimiento si
> usted conoce alguna biblioteca que hace el mismo trabajo de manera más sencilla y/o
> eficiente; su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
 
## Fecha de entrega: 7 de junio a medianoche

## Tratamiento de ficheros de notas

Con el final de curso llega la ardua tarea de evaluar las tareas realizadas por los alumnos durante el
mismo. Para facilitar esta tarea, se dispone de la clase `Alumno` que proporciona los datos
fundamentales de cada alumno: su número de identificación (`numIden`), su nombre completo 
(`nombre`) y la lista de notas obtenidas a lo largo del curso (`notas`). La clase también
proporciona métodos para añadir una nota al expediente del alumno (`__add__()`), para obtener
la representación *oficial* del mismo (`__repr__()`) y para obtener la representación
*bonita* (`__str__()`).

La definición de la clase `Alumno`, disponible en `alumno.py`, es:

```python
class Alumno:
    """
    Clase usada para el tratamiento de las notas de los alumnos. Cada uno
    incluye los atributos siguientes:

    numIden:   Número de identificación. Es un número entero que, en caso
               de no indicarse, toma el valor por defecto 'numIden=-1'.
    nombre:    Nombre completo del alumno.
    notas:     Lista de números reales con las distintas notas de cada alumno.
    """

    def __init__(self, nombre, numIden=-1, notas=[]):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = [nota for nota in notas]

    def __add__(self, other):
        """
        Devuelve un nuevo objeto 'Alumno' con una lista de notas ampliada con
        el valor pasado como argumento. De este modo, añadir una nota a un
        Alumno se realiza con la orden 'alumno += nota'.
        """
        return Alumno(self.nombre, self.numIden, self.notas + [other])

    def media(self):
        """
        Devuelve la nota media del alumno.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __repr__(self):
        """
        Devuelve la representación 'oficial' del alumno. A partir de copia
        y pega de la cadena obtenida es posible crear un nuevo Alumno idéntico.
        """
        return f'Alumno("{self.nombre}", {self.numIden!r}, {self.notas!r})'

    def __str__(self):
        """
        Devuelve la representación 'bonita' del alumno. Visualiza en tres
        columnas separas por tabulador el número de identificación, el nombre
        completo y la nota media del alumno con un decimal.
        """
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'
```

A menudo, las notas de los alumnos se almacenan en ficheros de texto en los que los datos de cada alumno
ocupan una línea con los distintos valores separados por espacios y/o tabuladores.

El ejemplo siguiente muestra un fichero típico con las notas de tres alumnos:

```text
171 Blanca Agirrebarrenetse 10  	9 	  9.5
23  Carles Balcell de Lara  5 	    5 	  4.5  	5.2
68  David Garcia Fuster 	7.75    5.25  8   
```

Añada al fichero `alumno.py` la función `leeAlumnos(ficAlum)` que lea un fichero de texto con los datos de 
todos los alumnos y devuelva un diccionario en el que la clave sea el nombre de cada alumno y su contenido 
el objeto `Alumno` correspondiente.

La función deberá cumplir los requisitos siguientes:

- Sólo debe realizar lo que se indica; es decir, debe leer el fichero de texto que se le pasa como único
  argumento y devolver un diccionario con los datos de los alumnos.
- El análisis de cada línea de texto se realizará usando expresiones regulares.
- La función `leeAlumnos()` debe incluir, en su cadena de documentación, la prueba unitaria siguiente según
  el formato de la biblioteca `doctest`, donde el fichero `'alumnos.txt'` es el fichero mostrado como ejemplo
  al principio de este enunciado:

  ```python
  >>> alumnos = leeAlumnos('alumnos.txt')
  >>> for alumno in alumnos:
  ...     print(alumnos[alumno])
  ...
  171     Blanca Agirrebarrenetse 9.5
  23      Carles Balcells de Lara 4.9
  68      David Garcia Fuster     7.0
  ```

  - Evidentemente, es responsabilidad del autor comprobar que la prueba unitaria se pasa satisfactoriamente
    antes de la entrega de la tarea.

  - Para evitar que diferencias debidas a espacios en blanco o tabuladores den lugar a error, se recomienda
    efectuar las pruebas unitarias con la opción `doctest.NORMALIZE_WHITESPACE`. Por ejemplo,
    `doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)`.


## Análisis de expresiones horarias

En casi todos los idiomas más habituales, cualquier hora puede reducirse al formato estándar HH:MM, donde HH es 
un número de dos dígitos, que representa la hora y está comprendido entre 00 y 23, y MM es otro número de dos 
dígitos, que representa el minuto y está comprendido entre 00 y 59.

No obstante, en el lenguaje hablado, es raro usar este formato estándar. En el caso del castellano, existe una
gran variedad de formatos. La lista siguiente alguna de las posibilidades más frecuentes, aunque existen bastantes
más:

- **08:27**

  Es el formato estándar. Cuando la hora es menor que 10, es posible representarla con
  dos dígitos (08:27), o sólo uno (8:27). Los minutos se representan siempre con dos (8:05).

- **8h27m**

  Las horas o minutos menores que 10 pueden representarse usando uno o dos dígitos. Las horas
  *en punto* pueden indicarse sin minutos (8h).

- **8 en punto**

  Las horas exactas suelen indicarse con la partícula *'en punto'*. En ese caso, es
  habitual omitir la letra *h* después de la cifra.

  Otras alternativas semejantes son las *'8 y cuarto'*, las *'8 y media'* o las *'8 menos cuarto'*.

  En todos estos casos, el reloj empleado será de 12 horas y empezando en 1 (de 1 a 12). El
  resultado será ambiguo, ya que no sabremos si una cierta hora es AM o PM, pero así es cómo
  se suele hablar (la gente queda a *'las 11 en punto'* para ir a una fiesta, no a las
  *'las 23 en punto'*). El resultado se devolverá siempre en el rango de 00:00 a 11:59.

- **... de la mañana**

  Las expresiones horarias entre las 4 y las 12 pueden ir seguidas de la partícula *'de la mañana'*.

  Análogamente, las horas entre las 12 y las 3 pueden ir seguidas de *'del mediodía'*, las horas entre
  las 3 y las 8 pueden serlo de *'de la tarde'*, entre 8 y 4 de *'de la noche'* y entre 1 y
  6 de *'de la madrugada'*.

  En estos casos, el reloj empleado es siempre de 12 horas (nunca se dice *'las 18 de la tarde'*, sino
  *'las 6 de la tarde'*). Además la hora no puede ser cero, sino que, en ese caso, se usaría 12.

### Tarea: normalización de las expresiones horarias de un texto

Escriba el fichero `horas.py` con la función `normalizaHoras(ficText, ficNorm)`, que lee el fichero de
texto `ficText`, lo analiza en busca de expresiones horarias y escribe el fichero `ficNorm` en el que
éstas se expresan según el formato normalizado, con las horas y los minutos indicados por dos dígitos
y separados por dos puntos (08:27).

Cada línea del fichero puede contener, o no, una o más expresiones horarias, pero éstas nunca aparecerán
partidas en más de una línea.

Las horas con expresión incorrecta, por ejemplo, *'17:5'* (en la expresión normalizada deben usarse dos
dígitos para expresar los minutos) u *'11 de la tarde'* (la tarde nunca llega hasta esa hora), deben
dejarse tal cual.

Para la evaluación de la tarea se usará un texto con unas cien expresiones horarias, que incluirán tanto
expresiones correctas como incorrectas. Una parte de la nota dependerá de la precisión en su normalización.

Se recomienda empezar normalizando textos que sólo contengan expresiones correctas del tipo más sencillo;
es decir, con la forma *'18h45m'*. La consecución de este objetivo garantiza una nota mínima de notable
bajo (7). La extensión al resto de formatos indicados y la detección de expresiones incorrectas serán
necesarias para alcanzar la nota máxima (10).

La tabla siguiente muestra un ejemplo de texto antes y después de su normalización, incluyendo tanto
expresiones horarias **correctas** como <span style="color:red">**incorrectas**</span>.

### Ejemplo de normalización de las expresiones horarias de un texto

Las líneas siguientes muestran ejemplos de expresiones horarias, tanto correctas como incorrectas. Las
mismas expresiones se encuentran en el fichero `horas.txt`, que puede usar para comprobar el correcto
funcionamiento de su función.

#### Expresiones válidas

> - La llegada del tren está prevista a las **18:30**
> - La llegada del tren está prevista a las **18:30**

> - Tenía su clase entre las **8h** y las **10h30m**
> - Tenía su clase entre las **08:00** y las **10:30**

> - Se acaba a las **4 y media de la tarde**
> - Se acaba a las **16:30**

> - Empieza a trabajar a las **7h de la mañana**
> - Empieza a trabajar a las **07:00**

> - Es lo mismo **5 menos cuarto** que **4:45**
> - Es lo mismo **04:45** que **04:45**

> - Tenemos descanso hasta las **17h5m**
> - Tenemos descanso hasta las **17:05**

> - Las campanadas son a las **12 de la noche**
> - Las campanadas son a las **00:00**

#### Expresiones incorrectas

> - Son exactamente las $\textbf{\color{red}17:5}$
> - Son exactamente las $\textbf{\color{red}17:5}$

> - Cuando llegó, ya eran las $\textbf{\color{red}11 de la tarde}$
> - Cuando llegó, ya eran las $\textbf{\color{red}11 de la tarde}$

> - El examen es a las $\textbf{\color{red}17 de la tarde}$
> - El examen es a las $\textbf{\color{red}17 de la tarde}$

> - Cenamos en las $\textbf{\color{red}7}$ puertas
> - Cenamos en las $\textbf{\color{red}7}$ puertas

> - No llegará antes de las $\textbf{\color{red}1h78m}$
> - No llegará antes de las $\textbf{\color{red}1h78m}$

> - *Corrió* la maratón en $\textbf{\color{red}32h31m}$, pero no ganó
> - *Corrió* la maratón en $\textbf{\color{red}32h31m}$, pero no ganó

> - Quedamos a las $\textbf{\color{red}23 en punto}$
> - Quedamos a las $\textbf{\color{red}23 en punto}$


#### Entrega

##### Ficheros `alumno.py` y `horas.py`

- Ambos ficheros deben incluir una cadena de documentación con el nombre del alumno o alumnos
  y una descripción de su contenido.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

##### Ejecución de los tests unitarios de `alumno.py`

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `alumno.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.

![Ejecución de tests](TEST_ALUMNOS2.png)

<br>

##### Ejecución de `horas.py` en el terminal (extra)

![Ejecución de tests](TEST_HORAS.png)

<br>

##### Código desarrollado

Inserte a continuación los códigos fuente desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).

##### Código python.py
```python
"""
Práctica de Expresiones Regulares
Autor: Eloi Belmonte Alcalá

Este fichero contiene la definición de la clase Alumno y la función
leeAlumnos(), la cual permite leer un archivo de texto con notas de alumnos
utilizando expresiones regulares y volcar los datos en un diccionario.
"""

import re

class Alumno:
    """
    Clase usada para el tratamiento de las notas de los alumnos. Cada uno
    incluye los atributos siguientes:

    numIden:   Número de identificación. Es un número entero que, en caso
               de no indicarse, toma el valor por defecto 'numIden=-1'.
    nombre:    Nombre completo del alumno.
    notas:     Lista de números reales con las distintas notas de cada alumno.
    """

    def __init__(self, nombre, numIden=-1, notas=[]):
        self.numIden = numIden
        self.nombre = nombre
        self.notas = [nota for nota in notas]

    def __add__(self, other):
        """
        Devuelve un nuevo objeto 'Alumno' con una lista de notas ampliada con
        el valor pasado como argumento. De este modo, añadir una nota a un
        Alumno se realiza con la orden 'alumno += nota'.
        """
        return Alumno(self.nombre, self.numIden, self.notas + [other])

    def media(self):
        """
        Devuelve la nota media del alumno.
        """
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __repr__(self):
        """
        Devuelve la representación 'oficial' del alumno. A partir de copia
        y pega de la cadena obtenida es posible crear un nuevo Alumno idéntico.
        """
        return f'Alumno("{self.nombre}", {self.numIden!r}, {self.notas!r})'

    def __str__(self):
        """
        Devuelve la representación 'bonita' del alumno. Visualiza en tres
        columnas separas por tabulador el número de identificación, el nombre
        completo y la nota media del alumno con un decimal.
        """
        return f'{self.numIden}\t{self.nombre}\t{self.media():.1f}'

# ENTREGA

import re

def leeAlumnos(ficAlum):
    """
    Lee un fichero de texto con los datos de los alumnos y devuelve
    un diccionario con los objetos Alumno.

    >>> alumnos = leeAlumnos('alumnos.txt')
    >>> for alumno in alumnos:
    ...     print(alumnos[alumno])
    171\tBlanca Agirrebarrenetse\t9.5
    23\tCarles Balcells de Lara\t4.9
    68\tDavid Garcia Fuster\t7.0

    """
    diccionario_alumnos = {}
    
    # Abrimos el archivo para leerlo línea por línea
    fichero = open(ficAlum, 'r', encoding='utf-8')
    
    for linea in fichero:
        linea = linea.strip() # Quitamos saltos de línea al final
        if not linea: 
            continue # Si la línea está vacía, nos la saltamos
            
        # Expresión regular para separar: ID, Nombre, y el bloque de notas
        patron = r'^(\d+)\s+(.+?)\s+([\d.\s]+)$'
        busqueda = re.match(patron, linea)
        
        if busqueda:
            id_alumno = int(busqueda.group(1))
            nombre_alumno = busqueda.group(2).strip()
            bloque_notas = busqueda.group(3)
            
            # Ahora usamos otra expresión regular para sacar todas las notas de ese bloque
            notas_texto = re.findall(r'\d+\.\d+|\d+', bloque_notas)
            
            # Convertimos las notas de texto a números reales (float)
            lista_notas = []
            for nota in notas_texto:
                lista_notas.append(float(nota))
            
            # Creamos el objeto Alumno y lo guardamos en el diccionario
            nuevo_alumno = Alumno(nombre_alumno, id_alumno, lista_notas)
            diccionario_alumnos[nombre_alumno] = nuevo_alumno
            
    fichero.close()
    return diccionario_alumnos 
import sys  # Importamos esto para poder leer la terminal

if __name__ == '__main__':
    # IMPRIMIMOS LA DESCRIPCIÓN DEL PRINCIPIO DEL ARCHIVO
    print(__doc__)
    print("=" * 40)
    
    import doctest
    # 1. Esto ejecuta la prueba del profesor en silencio
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
    
    # 2. Esto imprimirá el contenido de tu fichero en la terminal
    print("--- CONTENIDO DEL FICHERO DE ALUMNOS ---")
    diccionario = leeAlumnos('alumnos.txt')
    for nombre in diccionario:
        print(diccionario[nombre])
    
```

##### Código horas.py
```python
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
```


##### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.

##### Y NADA MÁS

Sólo se corregirá el contenido de este fichero `README.md` y los códigos fuente `alumno.py`
y `horas.py`. No incluya otros ficheros con código fuente, notebooks de Jupyter o explicaciones
adicionales; simplemente, no se tendrán en cuenta para la evaluación de la tarea. Evidentemente,
sí puede añadir ficheros con las imágenes solicitadas en el enunciado, pero éstas deberán ser
visualizadas correctamente desde este mismo fichero al acceder al repositorio de la tarea.
