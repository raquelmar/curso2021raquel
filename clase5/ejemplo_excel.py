import pandas as pd
leer_fichero = pd.read_csv(r'catalogo_csv_ext.csv', encoding="ISO-8859-1")

leer_fichero.to_excel(r'catalogo_cf.xlsx', index=None, header=True)