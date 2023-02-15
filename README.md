# generate_sql_BNCC

## Usado para Extrair dados de planilha do excel

`
file01 = ExtractionData(file="files/BNCC_Ensino Fundamental.xlsx",
                  roles=["COMPONENTE", "ANO/FAIXA", "OBJETOS DE CONHECIMENTO",
                         "PRÁTICAS DE LINGUAGEM", "HABILIDADES", "UNIDADES TEMÁTICAS"]
                  )
`
### Objeto retorna (method) execute() -> dict[str, dict[int, dict[str, str]]]
`
data = file01.execute()
`
