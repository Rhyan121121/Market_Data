import os
import subprocess
import time
from typing import Optional

import pyoo


libreoffice_process: Optional[subprocess.Popen] = None

def start_ods_server():
    global libreoffice_process
    command = [
        "soffice",
        "--headless",
        "--nologo",
        "--nodefault",
        "--norestore",
        "--accept=socket,host=localhost,port=2002;urp;"
    ]
    libreoffice_process = subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(2)

def stop_ods_server():
    global libreoffice_process
    if libreoffice_process:
        print("Encerrando o servidor LibreOffice...")
        libreoffice_process.terminate()
        libreoffice_process.wait()
        print("Servidor encerrado.")
    else:
        print("Aviso: Nenhum servidor ativo.")


def create_spreadsheet(shopping_list, output_path):
    desktop = pyoo.Desktop('localhost', 2002)
    document = desktop.create_spreadsheet()

    tab = document.sheets[0]
    tab.name = 'Compras Praia'


    tab[0, 0].value = 'Item'
    tab[0, 1].value = 'Quantidade'

    for current_line, (item, amount) in enumerate(shopping_list, start = 1):
        tab[current_line, 0].value = item
        tab[current_line, 1].value = amount

    absolute_path = os.path.abspath(output_path)

    document.save(absolute_path)

    document.close()




def remove_item_and_shift_up(file_path, item_name):

    abs_path = os.path.abspath(file_path)
    desktop = pyoo.Desktop('localhost', 2002)


    doc = desktop.open_spreadsheet(abs_path)
    sheet = doc.sheets[0]

    row_index = 1
    found = False


    while sheet[row_index, 0].value is not None and sheet[row_index, 0].value != "":

        if str(sheet[row_index, 0].value).strip().lower() == item_name.strip().lower():

            internal_sheet = getattr(sheet, 'target', getattr(sheet, '_target',None))

            if internal_sheet:
                internal_sheet.getRows().removeByIndex(row_index, 1)
                found = True
                print(f"Item '{item_name}' removido com sucesso.")
            else:
                print("Erro: Não foi possível acessar o Motor UNO do LibreOffice.")
            break

        row_index += 1

    if not found:
        print(f"Aviso: O item '{item_name}' não foi encontrado na planilha.")

    doc.save(abs_path)

    doc.close()




