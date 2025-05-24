import pandas as pd

def generate_report(data, output_path):
    """Genera un reporte en Excel con los datos auditados."""
    df = pd.DataFrame(data)
    
    # Estilo condicional para resaltar problemas
    writer = pd.ExcelWriter(output_path, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name="Auditoría")
    
    # Formato adicional
    workbook = writer.book
    worksheet = writer.sheets["Auditoría"]
    
    # Resaltar alto uso de CPU/RAM
    for col in ["cpu_usage", "ram_usage"]:
        for idx, value in enumerate(df[col]):
            if value > 80:  # Umbral de alerta
                worksheet.cell(row=idx+2, column=df.columns.get_loc(col)+1).fill = "FF0000"
    
    writer.close()