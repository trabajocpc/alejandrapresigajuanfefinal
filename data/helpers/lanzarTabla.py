def lanzarTablaHTML(dataframe,nombretabla):
    fileHtml=dataframe.to_html()
    file=open(f"./tablas/{nombretabla}.html","w", encoding= 'utf-8')
    file.write(fileHtml)
    file.close()