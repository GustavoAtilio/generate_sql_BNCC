from src.extraction_data.extraction_data import ExtractionData
from src.data.postgres_conn import Postegres


file01 = ExtractionData(file="files/BNCC_Ensino Fundamental.xlsx",
                  roles=["COMPONENTE", "ANO/FAIXA", "OBJETOS DE CONHECIMENTO",
                         "PRÁTICAS DE LINGUAGEM", "HABILIDADES", "UNIDADES TEMÁTICAS"]
                  )

pg = Postegres(dbname='', host='localhost', password='postgres', port=5432, user='postgres')

del pg