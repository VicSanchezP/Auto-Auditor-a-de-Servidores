import json
from modules.scanner import scan_server
from modules.report_generator import generate_report
from dotenv import load_dotenv

load_dotenv()

def main():
    with open('config/servers.json') as f:
        servers = json.load(f)['servers']
    
    audit_data = []
    for server in servers:
        print(f"Escaneando {server['ip']}...")
        data = scan_server(server)
        audit_data.append(data)
    
    generate_report(audit_data, "outputs/audit_report.xlsx")

if __name__ == "__main__":
    main()