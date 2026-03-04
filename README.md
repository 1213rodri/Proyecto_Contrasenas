<div align="center">

# 🔐 RobustPro

**Evaluador de Robustez de Contraseñas en Python**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Security](https://img.shields.io/badge/Focus-CyberSecurity-ef4444?style=for-the-badge&logo=shield&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()

*Detecta patrones inseguros · Clasifica por nivel de fortaleza · Proporciona retroalimentación técnica*

</div>

---

## 📋 Tabla de Contenidos
- [🎯 Descripción](#-descripción)
- [⚠️ Contexto de Seguridad](#️-contexto-de-seguridad)
- [✨ Características](#-características)
- [🚀 Instalación](#-instalación)
- [💻 Uso](#-uso)
- [📊 Sistema de Puntuación](#-sistema-de-puntuación)
- [🔍 Detección de Patrones](#-detección-de-patrones)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [📄 Licencia](#-licencia)

---

## 🎯 Descripción

**RobustPro** es un programa en Python para la **evaluación cuantitativa de la robustez de contraseñas**, aplicando criterios técnicos de seguridad informática. Determina objetivamente qué tan segura es una contraseña y proporciona retroalimentación específica para mejorarla.

> 💡 El uso inadecuado de contraseñas sigue siendo una de las principales causas de vulnerabilidades en sistemas informáticos modernos.

---

## ⚠️ Contexto de Seguridad

Las contraseñas débiles facilitan ataques como:

| Tipo de Ataque | Descripción |
|---|---|
| 💥 **Fuerza Bruta** | Prueba exhaustiva de todas las combinaciones posibles |
| 📖 **Diccionario** | Uso de listas de contraseñas comunes conocidas |
| 🔄 **Credential Stuffing** | Reutilización de credenciales filtradas en brechas previas |
| 🔀 **Ataques Híbridos** | Combinación de diccionario + mutaciones de caracteres |

---

## ✨ Características
```
┌─────────────────────────────────────────────────────────┐
│                    FUNCIONALIDADES                      │
├─────────────────────────────────────────────────────────┤
│  ✅  Evaluación cuantitativa con puntaje de 0 a 100     │
│  ✅  Clasificación en 5 niveles de fortaleza            │
│  ✅  Detección de secuencias (1234, abcd...)            │
│  ✅  Detección de repeticiones (aaaa, 1111...)          │
│  ✅  Verificación contra palabras comunes               │
│  ✅  Retroalimentación específica por criterio          │
│  ✅  Interfaz de terminal con colores y estilo          │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Instalación

**Prerrequisitos:** Python 3.8+ y `pip`
```bash
# 1. Clona el repositorio
git clone https://github.com/rodrigo/robustpro.git
cd robustpro

# 2. (Opcional) Entorno virtual
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta
python main.py
```

---

## 💻 Uso
```
╔══════════════════════════════════════════════╗
║       🔐  EVALUADOR DE CONTRASEÑAS           ║
╚══════════════════════════════════════════════╝

  Ingresa tu contraseña: ••••••••••••

  ┌──────────────────────────────────────────┐
  │  RESULTADO DE EVALUACIÓN                 │
  ├──────────────────────────────────────────┤
  │  Longitud ≥ 12          ✅  +20 pts      │
  │  Mayúsculas             ✅  +15 pts      │
  │  Minúsculas             ✅  +15 pts      │
  │  Números                ✅  +15 pts      │
  │  Símbolos               ✅  +15 pts      │
  │  Sin patrones comunes   ✅  +20 pts      │
  ├──────────────────────────────────────────┤
  │  PUNTAJE TOTAL:        100 / 100         │
  │  NIVEL:          🟢  MUY FUERTE          │
  └──────────────────────────────────────────┘
```

---

## 📊 Sistema de Puntuación

| Criterio | Puntos |
|---|:---:|
| 📏 Longitud ≥ 12 caracteres | **+20** |
| 🔠 Incluye mayúsculas | **+15** |
| 🔡 Incluye minúsculas | **+15** |
| 🔢 Incluye números | **+15** |
| 🔣 Incluye símbolos | **+15** |
| 🛡️ Sin patrones comunes | **+20** |
| | **Total: 100** |

### Niveles de Clasificación
```
  0 ──────── 20 ──────── 40 ──────── 60 ──────── 80 ──────── 100
  🔴          🟠          🟡          🔵           🟢
MUY DÉBIL   DÉBIL       MEDIA      FUERTE    MUY FUERTE
```

| Rango | Nivel |
|:---:|---|
| 0 – 20 | 🔴 Muy Débil |
| 21 – 40 | 🟠 Débil |
| 41 – 60 | 🟡 Media |
| 61 – 80 | 🔵 Fuerte |
| 81 – 100 | 🟢 Muy Fuerte |

---

## 🔍 Detección de Patrones

El programa identifica automáticamente:

**Secuencias** — `1234`, `abcd`, `qwerty`, `asdf`  
**Repeticiones** — `aaaa`, `1111`, `!!!!`  
**Palabras comunes** — `password`, `admin`, `123456`, `letmein`

---

## 📁 Estructura del Proyecto
```
robustpro/
├── main.py              # Punto de entrada
├── evaluador.py         # Lógica de evaluación y puntuación
├── patrones.py          # Detección de patrones inseguros
├── ui.py                # Interfaz de usuario en terminal
├── wordlist.py          # Lista de palabras comunes
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

Desarrollado por **Rodrigo** · Ingeniería en Ciberseguridad · 2026

*"Una contraseña fuerte es tu primera línea de defensa."*

</div>
```

---

## 📄 LICENSE (MIT)
```
MIT License

Copyright (c) 2026 Rodrigo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
