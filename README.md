# 💼 Buscador de Trabajo — Carlos Molina Gil

Repositorio personal para la búsqueda activa y automatizada de empleo en **Valencia y alrededores** (Oficina Técnica Eléctrica, EPLAN Electric P8, AutoCAD, Automatización Industrial, PLC/HMI, Neumática y Diseño Mecánico con Solid Edge / Siemens NX).

---

## 🚀 Cómo trabajamos en este proyecto

Este repositorio funciona como mi centro de control junto con el asistente de **Antigravity**:

1. **☁️ Sincronización directa con Google Drive:**
   - Los archivos originales de mi CV (PDFs de 1 y 2 páginas, imágenes y fotos) se gestionan directamente desde mi carpeta de Google Drive y se sincronizan automáticamente con [`busqueda_empleo/notebooks/sincronizar_drive.py`](busqueda_empleo/notebooks/sincronizar_drive.py).
2. **💬 Búsqueda y Postulación desde el Chat + Navegador:**
   - A través del chat de Antigravity (conectado a **Google Chrome**, **LinkedIn** e **InfoJobs**), buscamos ofertas nuevas día a día, filtramos las más competitivas con enlaces directos y nos inscribimos directamente en las plataformas.
3. **📓 Notebook de Radar y Recarga de Ofertas:**
   - [`busqueda_empleo/notebooks/buscador_ofertas.ipynb`](busqueda_empleo/notebooks/buscador_ofertas.ipynb): Sincroniza el CV desde Drive, consulta ofertas reales activas en Valencia en tiempo real y actualiza el historial en [`busqueda_empleo/ofertas/ofertas_guardadas.json`](busqueda_empleo/ofertas/ofertas_guardadas.json).
4. **🤖 Guías de Prompts y Perfiles:**
   - [`busqueda_empleo/docs/guia_prompts_empleo.md`](busqueda_empleo/docs/guia_prompts_empleo.md): Plantillas de prompts para adaptar candidaturas, redactar mensajes a reclutadores y preparar entrevistas técnicas.
   - [`busqueda_empleo/docs/optimizacion_linkedin.md`](busqueda_empleo/docs/optimizacion_linkedin.md): Textos base y palabras clave SEO utilizadas en mis perfiles de LinkedIn e InfoJobs.

---

## 🌿 Estructura de Ramas (Git)
- **`main`**: Versión base estable del repositorio.
- **`develop`**: Rama de trabajo diario donde actualizamos las ofertas encontradas, scripts y mejoras.
