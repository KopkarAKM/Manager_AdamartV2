import subprocess
import os

html_path = os.path.abspath("panduan_po.html")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
screenshot_full = os.path.abspath("Panduan_Pembuatan_PO_Lengkap.png")

# Ambil screenshot full page
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--force-device-scale-factor=2",
    "--window-size=1200,4600",
    f"--screenshot={screenshot_full}",
    f"file:///{html_path.replace(os.sep, '/')}"
]
subprocess.run(cmd, capture_output=True, text=True)

# Re-convert PDF untuk memastikan versi PDF paling fresh dan sempurna
pdf_path = os.path.abspath("Panduan_Pembuatan_PO_Adamart.pdf")
cmd_pdf = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-margins",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path.replace(os.sep, '/')}"
]
subprocess.run(cmd_pdf, capture_output=True, text=True)

print("Full screenshot and PDF successfully generated!")
