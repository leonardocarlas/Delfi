from plistlib import InvalidFileException
import openpyxl
import shutil
import os


FILE = "model.xlsx"

# Write market_cap to cell B17 in the 'Indexes' sheet of model.xlsx.
# Optionally fetch market_cap from FMP API if ticker and api_key are provided.

# Returns:
# - dict: Status and message indicating success or failure.
def write_value_within_cell(value:str =None, excel_file: str=FILE, sheet_name: str ="", cell: str =""):

    try:
        # If market_cap is not provided, fetch it from FMP
        # Load the Excel file
        workbook = openpyxl.load_workbook(excel_file)
        
        # Check if the sheet exists
        if sheet_name not in workbook.sheetnames:
            return {
                "status": "error", 
                "message": f"Sheet '{sheet_name}' not found in {excel_file}"
            }
        
        # Select the sheet
        sheet = workbook[sheet_name]
        
        # Write market_cap to the specified cell (B17)
        sheet[cell] = value
        
        # Save the workbook
        workbook.save(excel_file)
        workbook.close()
        
        return {"status": "success", "message": f"Market cap {value:,.2f} written to {cell} in {sheet_name} sheet of {excel_file}"}
    
    except InvalidFileException:
        return {"status": "error", "message": f"File {excel_file} is not a valid Excel file or does not exist"}
    except Exception as e:
        return {"status": "error", "message": f"Error writing to Excel: {str(e)}"}
    


def create_excel_file(file_name: str):
    # Percorso del file modello
    modello = 'lib/model.xlsx'
    
    # Verifica se il file modello esiste
    if not os.path.exists(modello):
        raise FileNotFoundError(f"Il file modello '{modello}' non è stato trovato.")
    
    # Aggiunge estensione se non presente
    if not file_name.endswith('.xlsx'):
        file_name += '.xlsx'
    
    # Copia il file
    shutil.copy(modello, file_name)
    print(f"File copiato con successo: {file_name}")