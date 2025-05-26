import psutil
import platform
import subprocess
from datetime import datetime

def scan_server(server):
    """Recolecta datos de un servidor local o remoto."""
    data = {
        "ip": server["ip"],
        "os": server["os"],
        "timestamp": datetime.now().isoformat(),
        "vulnerabilities": []
    }

    try:
        if server["os"] == "Windows":
            # Ejemplo: Obtener programas instalados (Windows)
            cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion"'
            result = subprocess.run(cmd, capture_output=True, text=True)
            data["software"] = parse_software(result.stdout)
            
        elif server["os"] == "Linux":
            # Ejemplo: Obtener paquetes instalados (Linux)
            cmd = "dpkg-query -l"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            data["software"] = parse_software(result.stdout)
        
        # Detección de vulnerabilidades (simplificado)
        data["vulnerabilities"] = check_vulnerabilities(data["software"])
        
        # Uso de recursos
        data["cpu_usage"] = psutil.cpu_percent(interval=1)
        data["ram_usage"] = psutil.virtual_memory().percent
        
    except Exception as e:
        data["error"] = str(e)
    
    return data

def parse_software(output):
    """Convierte la salida de comandos en una lista de software."""
    # Implementar según el formato de tu OS
    return [line.strip() for line in output.split('\n') if line.strip()]

def check_vulnerabilities(software_list):
    """Compara software con una DB de vulnerabilidades (simplificado)."""
    # En una app real, usaría NVD API o una DB local
    return ["OpenSSL 1.1.1 (CVE-2022-3602)"] if "openssl" in str(software_list).lower() else []