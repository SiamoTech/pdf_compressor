# Importa il modulo PySimpleGUI e lo rinomina come sg
import PySimpleGUI as sg
# Importa il modulo os
import os

# Importa le classi PdfReader e PdfWriter dal modulo PyPDF2
from PyPDF2 import PdfReader, PdfWriter

# Definisce una funzione chiamata compress_pdf che accetta due argomenti
def compress_pdf(file_path, output_path):
    # Crea un'istanza della classe PdfReader utilizzando il percorso del file PDF fornito come argomento
    pdf_reader = PdfReader(file_path)
    # Crea un'istanza della classe PdfWriter
    pdf_writer = PdfWriter()
    # Scorre tutte le pagine del file PDF utilizzando l'attributo pages dell'istanza di PdfReader
    for page in range(len(pdf_reader.pages)):
        # Aggiunge la pagina corrente del file PDF all'istanza di PdfWriter
        pdf_writer.add_page(pdf_reader.pages[page])
    # Apre il file specificato dal percorso di output in modalità scrittura binaria e lo assegna alla variabile out
    with open(output_path, 'wb') as out:
        # Scrive il contenuto dell'istanza di PdfWriter nel file aperto
        pdf_writer.write(out)

# Definisce l'aspetto dell'interfaccia grafica
layout = [[sg.Text('Seleziona il file PDF da comprimere')],
          [sg.Input(key='-IN-'), sg.FileBrowse()],
          [sg.Button('Comprimi'), sg.Button('Esci')]]

# Crea una finestra utilizzando il layout definito in precedenza
window = sg.Window('Compressore PDF', layout)

# Gestisce gli eventi dell'interfaccia grafica
while True:
    event, values = window.read()
    # Se l'evento è la chiusura della finestra o la pressione del pulsante 'Esci', interrompe il ciclo
    if event == sg.WIN_CLOSED or event == 'Esci':
        break
    # Se l'evento è la pressione del pulsante 'Comprimi'
    if event == 'Comprimi':
        # Ottiene il percorso del file selezionato dall'utente
        file_path = values['-IN-']
        # Se è stato selezionato un file
        if file_path:
            # Genera automaticamente un percorso di output
            output_path = os.path.join(os.path.dirname(file_path), 'compressed.pdf')
            # Esegue la funzione compress_pdf utilizzando i percorsi di input e output
            compress_pdf(file_path, output_path)
            # Visualizza un messaggio popup per informare l'utente del successo dell'operazione
            sg.popup('File compresso con successo:', output_path)
        else:
            # Visualizza un messaggio popup per informare l'utente di selezionare un file PDF
            sg.popup('Seleziona un file PDF')

# Chiude la finestra
window.close()
