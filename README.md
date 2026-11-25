# 🚀 Espacio de Proyectos — Carlos Molina Gil

Repositorio principal organizado en módulos independientes para el desarrollo de proyectos y automatización con el asistente **Antigravity**.

---

## 📂 Organización de Módulos

El repositorio está estructurado en módulos completamente separados para mantener el código y los recursos aislados y ordenados:

### 💼 1. Módulo: Búsqueda de Empleo (`busqueda_empleo/`)
Centro de control para la búsqueda activa y automatizada de empleo en **Valencia y alrededores** (Oficina Técnica Eléctrica, EPLAN Electric P8, AutoCAD, Automatización Industrial y Diseño Mecánico):
- **☁️ Sincronización Google Drive:** [`busqueda_empleo/notebooks/sincronizar_drive.py`](busqueda_empleo/notebooks/sincronizar_drive.py) mantiene actualizados los PDFs y fotos del CV.
- **📓 Notebook Radar de Ofertas:** [`busqueda_empleo/notebooks/buscador_ofertas.ipynb`](busqueda_empleo/notebooks/buscador_ofertas.ipynb) para consultar, filtrar y recargar ofertas activas en [`busqueda_empleo/ofertas/ofertas_guardadas.json`](busqueda_empleo/ofertas/ofertas_guardadas.json).
- **🤖 Documentación & Perfiles:** Guías de prompts y optimización SEO para LinkedIn e InfoJobs en [`busqueda_empleo/docs/`](busqueda_empleo/docs/).

---

### 🚗 2. Módulo: Proyecto GTA (`gta/`)
Entorno de desarrollo y prototipado inspirado en Grand Theft Auto (mecánicas de jugador, conducción, misiones y mapa urbano):
- **📓 Notebook Interactivo:** [`gta/notebooks/gta_proyecto.ipynb`](gta/notebooks/gta_proyecto.ipynb) con simulación paso a paso de entidades, misiones y mini-radar gráfico 2D con Matplotlib.
- **⚙️ Código Fuente Modular (`gta/src/`):**
  - [`motor.py`](gta/src/motor.py): Clases base `Jugador`, `Vehiculo` y `Mision`.
  - [`config.py`](gta/src/config.py): Ajustes de física, velocidades y dimensiones.
- **🗺️ Documentación & Hoja de Ruta (`gta/docs/`):**
  - [`roadmap_gta.md`](gta/docs/roadmap_gta.md): Opciones de desarrollo (Juego 2D con Pygame, Servidores FiveM, Bot/Visión artificial con OpenCV, o Análisis de datos).
  - [`recursos_gta.md`](gta/docs/recursos_gta.md): Enlaces y documentación recomendada.
- **💾 Datos y Partidas (`gta/data/`):** Guardado de estado de juego en JSON.

---

## 🌿 Estructura de Ramas (Git)
- **`main`**: Versión base estable del repositorio.
- **`develop`**: Rama de trabajo diario donde actualizamos ofertas, notebooks y prototipos.
