"""
Script de sincronización y verificación del CV en busqueda_empleo/cv/.
- Si se ejecuta desde el agente de Antigravity (con credenciales OAuth activas de Drive),
  descarga cualquier cambio nuevo desde la carpeta de Google Drive.
- Si se ejecuta desde el kernel local de Jupyter Notebook (que no tiene acceso directo
  al token privado de sesión del plugin), carga instantáneamente los archivos ya
  sincronizados en busqueda_empleo/cv/ y extrae el texto actualizado del PDF.
"""
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

FOLDER_ID = "1XIZPcGc0eDDvf0mdzb8RgVVgOQ5Dt4Oh"
CV_DIR = Path(__file__).resolve().parent.parent / "cv"
META_FILE = CV_DIR / ".drive_sync_meta.json"
GDRIVE_BIN = Path(r"C:\Users\marcm\.gemini\antigravity\bin\gdrive.cmd")

def extraer_texto_pdf():
    pdf_1pag = CV_DIR / "CV_Carlos_Molina_Gil_1Pagina.pdf"
    if not pdf_1pag.exists():
        return ""
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(pdf_1pag))
        texto_pdf = "\n".join(page.extract_text() or "" for page in reader.pages)
        (CV_DIR / "cv_extraido_auto.txt").write_text(texto_pdf, encoding="utf-8")
        return texto_pdf
    except Exception as e:
        print(f"ℹ️ Nota al leer PDF: {e}")
        return ""

def mostrar_estado_local():
    pdfs = sorted(CV_DIR.glob("*.pdf"))
    imgs = sorted(list(CV_DIR.glob("*.png")) + list(CV_DIR.glob("*.jpg")))
    print(f"📂 Carpeta local del CV: {CV_DIR}")
    for p in pdfs:
        mod = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        kb = p.stat().st_size / 1024
        print(f"   📄 {p.name} ({kb:.1f} KB) — Última sincronización: {mod}")
    print(f"   🖼️ Imágenes y fotos disponibles: {len(imgs)} archivos ({', '.join(i.name for i in imgs)})")
    texto = extraer_texto_pdf()
    if texto:
        print(f"✅ Texto extraído del PDF actualizado correctamente ({len(texto)} caracteres).")

def sincronizar_cv_drive(forzar=False):
    CV_DIR.mkdir(parents=True, exist_ok=True)

    # Resolver ejecutable de gdrive (tanto en el agente como en el kernel local del Notebook)
    ejecutable = "gdrive" if shutil.which("gdrive") else (str(GDRIVE_BIN) if GDRIVE_BIN.exists() else None)
    if ejecutable is not None:
        cmd = [ejecutable, "readonly", "ls", FOLDER_ID, "--max", "50", "--json"]
        res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if res.returncode == 0 and res.stdout.strip().startswith("["):
            archivos = json.loads(res.stdout)
            meta_anterior = {}
            if META_FILE.exists():
                try:
                    meta_anterior = json.loads(META_FILE.read_text(encoding="utf-8"))
                except Exception:
                    meta_anterior = {}

            actualizados = []
            nueva_meta = {}
            for arch in archivos:
                nombre = arch["name"]
                file_id = arch["id"]
                mod_time = arch.get("modifiedTime", "")
                nueva_meta[nombre] = mod_time
                destino = CV_DIR / nombre

                if forzar or not destino.exists() or meta_anterior.get(nombre) != mod_time:
                    print(f"⬇️ Descargando desde Google Drive: {nombre} (Modificado: {mod_time[:19]})")
                    dl_cmd = [ejecutable, "readonly", "download", file_id, "--out", str(destino)]
                    subprocess.run(dl_cmd, capture_output=True, text=True, shell=True)
                    actualizados.append(nombre)

            META_FILE.write_text(json.dumps(nueva_meta, indent=2), encoding="utf-8")
            extraer_texto_pdf()
            if actualizados:
                print(f"✅ ¡Sincronizados {len(actualizados)} archivo(s) nuevos directamente desde Google Drive!")
            else:
                print("✅ Conectado a Google Drive: tu carpeta local ya tiene la última versión de todos tus archivos.")
            mostrar_estado_local()
            return actualizados

    # Modo Kernel Local de Jupyter: usa los archivos ya sincronizados por el agente y actualiza la extracción del PDF
    print("✅ Modo Notebook Local: Cargando los archivos de tu CV sincronizados desde Google Drive...")
    mostrar_estado_local()
    print("\n💡 Nota: Como tu carpeta de Drive es privada, cuando subas un PDF nuevo a Drive")
    print("   solo tienes que escribir en el chat de Antigravity: 'sincroniza mi Drive'")
    print("   y el asistente actualizará los PDFs al instante con tu cuenta vinculada.")
    return []

if __name__ == "__main__":
    sincronizar_cv_drive()
