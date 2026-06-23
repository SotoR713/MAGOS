# M.A.G.O.S.

### *Maestros Arcanos Guiados por la Onceava Senda*

Un RPG roguelike por turnos para la terminal, hecho en Python puro. Recorre una senda de bifurcaciones, enfréntate a magos rivales, abre cofres traicioneros y derrota a los Guardianes que custodian el camino.

> *Tu nombre define tu senda. La senda recuerda tus decisiones.*

---

## ¿Qué es M.A.G.O.S.?

Eres un mago que avanza por una travesía lineal llena de bifurcaciones. En cada paso eliges entre dos caminos, cada uno con un evento visible antes de decidir: un combate, un cofre, una fuente de curación... o, cada cierto tramo, un **Guardián** que cierra el paso. El objetivo es llegar lo más lejos posible antes de caer.

Lo que distingue a M.A.G.O.S. es que **es completamente determinista**: la aventura nace de tu nombre. El mismo nombre genera siempre la misma travesía, así que dos jugadores con el mismo nombre viven exactamente la misma historia. No se usa ninguna librería de azar — toda la "aleatoriedad" se calcula a mano.

---

## Características

- **Aventura determinista por nombre.** Tu nombre se convierte en una semilla numérica que alimenta un generador pseudoaleatorio propio. Mismo nombre, misma senda.
- **Generador congruencial propio.** Sin `import random`: la aleatoriedad se produce con un generador lineal congruencial escrito desde cero.
- **Combate por turnos con ventaja elemental.** Cinco elementos (Agua, Fuego, Planta, Tierra, Neutral) girando en una rueda donde cada uno es fuerte y débil contra otro.
- **Crítico y esquiva.** El jugador obtiene crítico y evasión según su ventaja de velocidad sobre el rival; los enemigos los tienen como probabilidad fija.
- **Sistema de niveles.** Al vencer subes de nivel y repartes puntos en tus estadísticas como tú quieras.
- **Eventos variados.** Rivales, Guardianes, cofres (con sorpresas buenas y malas) y fuentes de curación.
- **Mapa visual ASCII.** La senda se dibuja con símbolos que recuerdan cada decisión y cada batalla del recorrido.
- **Pantallas con arte ASCII.** Título, derrota y victoria sobre Guardián.
- **Balance centralizado.** Todas las "perillas" del juego viven en un solo archivo de configuración, fáciles de ajustar.

---

## Cómo jugar

Necesitas **Python 3** instalado. Desde la carpeta raíz del proyecto, ejecuta el punto de entrada:

```bash
python Ejecutable.py
```

> **Importante:** ejecuta siempre `Ejecutable.py` desde la raíz del proyecto. Es el punto de entrada que coordina todos los módulos.

Una vez dentro:
1. Escribe tu nombre (define tu semilla y, con ella, toda tu aventura).
2. Elige tu elemento.
3. Reparte tus puntos de estadística.
4. En cada paso, elige entre el camino `0` y el camino `1`.
5. Sobrevive tanto como puedas. Cuando caes, puedes reiniciar.

---

## Estructura del proyecto

El código está organizado por responsabilidad, con las dependencias apuntando en una sola dirección:

```
MAGOS/
├── Ejecutable.py        # Punto de entrada: el bucle principal del juego
├── Configuracion.py     # Perillas de balance (daño, curación, umbrales, etc.)
├── Clases/              # Los objetos del juego
│   ├── Magos.py             # Clase base Mago
│   ├── Jugador.py           # El mago del jugador
│   ├── Rival.py             # Magos rivales
│   ├── Jefe.py              # Guardianes (jefes)
│   ├── Elementos.py         # Los cinco elementos y su rueda
│   ├── Eventos.py           # Tipos de evento del mapa
│   ├── Generadores.py       # El generador pseudoaleatorio
│   ├── ValoracionCaracter.py # Tabla letra → valor (para la semilla)
│   └── Mapa.py              # La senda, los eventos y su resolución
└── Funciones/           # Las operaciones del juego
    ├── Combate.py           # El motor de enfrentamientos
    ├── Fabrica.py           # Construcción de rivales y jefes
    ├── Interfaz.py          # Títulos, menús e interacción con el jugador
    └── Calculadoras.py      # Utilidades (raíz digital, asignación de elemento)
```

- **`Clases/`** guarda los *qué* (los objetos: magos, elementos, el mapa).
- **`Funciones/`** guarda los *cómo* (las operaciones: pelear, crear enemigos, mostrar la interfaz).

---

## Sobre el diseño

M.A.G.O.S. es un proyecto de **Programación Orientada a Objetos**, y aplica sus pilares de forma deliberada:

- **Herencia:** `Jugador`, `Rival` y `Jefe` heredan de una clase base `Mago`.
- **Polimorfismo:** cada tipo de mago calcula su crítico, su evasión y su reparto de estadísticas a su manera; el motor de combate los trata a todos como "un mago" sin preguntar de qué tipo son.
- **Abstracción:** la clase base define el contrato que sus hijos deben cumplir.
- **Encapsulamiento:** los atributos son privados y se acceden a través de métodos.
- **Composición:** un mago *tiene un* elemento; un mapa *tiene un* generador y un jugador.

La arquitectura está modularizada, con imports explícitos y la configuración del juego centralizada en un único archivo para poder afinar el balance sin tocar la lógica.

---

## Autor

Desarrollado por [SotoR713](https://github.com/SotoR713).
