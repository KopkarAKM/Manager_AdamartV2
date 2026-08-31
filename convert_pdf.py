import subprocess
import os
import time

html_path = os.path.abspath("panduan_po.html")
pdf_path = os.path.abspath("Panduan_Pembuatan_PO_Adamart.pdf")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

print(f"HTML: {html_path}")
print(f"PDF: {pdf_path}")
print(f"Browser: {chrome_path}")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-margins",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)

time.sleep(2)
if os.path.exists(pdf_path):
    print(f"SUCCESS! PDF created: {os.path.getsize(pdf_path)} bytes")
else:
    print("PDF not found yet.")
