def plum():    
    import pandas as pd
    organization_path = input("Ingrese el directorio donde se encuentran los archivos: ")
    filePFACIL = organization_path+"PFACIL.xlsx"
    fileRAPIPAGO = organization_path+"RAPIPAGO.xlsx"
    fileLINK = organization_path+"LINK.xlsx"
    filePMC = organization_path+"PMC.xlsx"
    fileCOBEX = organization_path+"COBEX.xlsx"
    fileBAPRO =  organization_path+"BAPRO.xlsx"
    filePLUS = organization_path+"PLUS.xlsx"
    def data_importer(file):
        data = pd.read_excel(file, skiprows=7, skipfooter=1)
        return  pd.DataFrame(data)
    importPFACIL = data_importer(filePFACIL)
    importRAPIPAGO = data_importer(fileRAPIPAGO)
    importLINK = data_importer(fileLINK)
    importPMC = data_importer(filePMC)
    importCOBEX = data_importer(fileCOBEX)
    importBAPRO = data_importer(fileBAPRO)
    importPLUS = data_importer(filePLUS)
    consolidadoCobranzas = pd.concat([importPFACIL,importRAPIPAGO,importLINK,importPMC,importCOBEX,importBAPRO,importPLUS])
    consolidadoCobranzas["Alertas"] = consolidadoCobranzas["Alertas"].fillna("")
    cobranzaNoImputada = consolidadoCobranzas.loc[consolidadoCobranzas["Alertas"].str.contains("SE GENERA")|
                                                  consolidadoCobranzas["Alertas"].str.contains("CANCELADO")|
                                                  consolidadoCobranzas["Alertas"].str.contains("NO IMPUTADO"), :].reset_index(drop=True)
    cobranzaImputada = consolidadoCobranzas.loc[~consolidadoCobranzas["Alertas"].str.contains("SE GENERA")|
                                                ~consolidadoCobranzas["Alertas"].str.contains("CANCELADO")|
                                                ~consolidadoCobranzas["Alertas"].str.contains("NO IMPUTADO"), :].reset_index(drop=True)
    def save():
        with pd.ExcelWriter('consolidado.xlsx') as writer:  
            cobranzaNoImputada.to_excel(writer, sheet_name='CobranzaNoImputada')
            cobranzaImputada.to_excel(writer, sheet_name='CobranzaImputada')
            consolidadoCobranzas.to_excel(writer, sheet_name='CobranzaTotal')
    save()
plum()