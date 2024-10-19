import pandas as pd
import panel as pn
import hvplot.pandas  # Necessário para habilitar o .hvplot em DataFrames

# Função principal para gerar a visualização do ARMOBS
def monitor_armobs_main():
    csv_path = 'C:\\Users\\ll7nt\\SMNAMonitoringApp\\examples\\obsm\\mon_rec_obs_final.csv'
    dfs = pd.read_csv(csv_path, header=0, parse_dates=['Data do Download', 'Data da Observação'])
    
    pn.extension('tabulator')

    # Exibir os dados em um widget interativo
    df_pane = pn.widgets.Tabulator(dfs, pagination='remote', page_size=10)

    # Configuração do layout com título e a tabela interativa
    layout = pn.Column('# Monitoramento de ARMOBS', df_pane)
    
    return layout

# Função que cria a sidebar, se necessário
def monitor_armobs_sidebar():
    return pn.Column("## Sidebar do Monitoramento ARMOBS", "Controles e filtros podem ser adicionados aqui.")

# Faz o script servable se for executado diretamente
if __name__ == '__main__':
    layout = monitor_armobs_main()
    layout.servable()
