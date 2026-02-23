# Juego de Personajes (POO en Python)

Proyecto educativo desarrollado en Python con el objetivo de practicar
Programación Orientada a Objetos (POO), herencia, polimorfismo y diseño
básico de sistemas de combate por turnos.

## 🎮 Descripción

El proyecto consiste en un juego simple de personajes donde distintas
clases (Guerrero, Mago, Arquero, etc.) heredan de una clase base `Personaje`
y cuentan con habilidades y comportamientos propios.

Actualmente el sistema permite:
- Crear personajes con estadísticas básicas
- Realizar ataques entre personajes
- Aplicar daño teniendo en cuenta defensa
- Implementar habilidades especiales según la clase

## 🧩 Estructura del proyecto
- personaje.py # Clase base Personaje
- guerrero.py # Subclase Guerrero
- mago.py # (en desarrollo)
- arquero.py # (en desarrollo)
- main.py # Punto de entrada del programa

## ⚔️ Clases implementadas

### Personaje
Clase base que define:
- Vida
- Ataque
- Defensa
- Lógica de ataque y recepción de daño
- Verificación de estado (vivo / muerto)

### Guerrero
Subclase especializada que:
- Posee mayor defensa y vida
- Puede bloquear el próximo ataque usando un escudo
- Cuenta con un ataque pesado que inflige más daño

## 🚧 Estado del proyecto

🟡 En desarrollo  
El proyecto se irá ampliando progresivamente con:
- Nuevas clases de personajes
- Sistema de turnos
- Combate más avanzado
- Estados (buffs/debuffs)
- Posible sistema de niveles

## ▶️ Ejecución

Requiere Python 3.10 o superior.

```bash
python main.py
 ```

## 📌 Objetivo del proyecto
Este proyecto no busca ser un juego completo, sino una base sólida
para practicar conceptos de POO, diseño de clases y lógica de juegos.
