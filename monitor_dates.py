import os
import panel as pn
class MonitoringAppDates:
    def __init__(self):
        pn.extension()
        # Defina a pasta onde estão os arquivos
        self.examples_dir = "C:/Users/ll7nt/SMNAMonitoringApp/examples"

    def openFile(self, log):
        local_path = os.path.join(self.examples_dir, log)
        
        # Verifica se o arquivo local existe
        if os.path.exists(local_path):
            with open(local_path, 'r') as f:
                return f.read()
        else:
            raise FileNotFoundError(f"O arquivo {local_path} não foi encontrado.")

    def getDates(self):
        start_date = self.openFile("aweekbefore.txt")
        end_date = self.openFile("todaym1H.txt")

        return start_date.strip(), end_date.strip()

# Exemplo de uso
app = MonitoringAppDates()
print(app.getDates())
