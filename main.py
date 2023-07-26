import pandas as pd
from data.platos import platosPopulares
from data.helpers.lanzarTabla import lanzarTablaHTML
tablaPlatos=pd.DataFrame(platosPopulares)
lanzarTablaHTML(tablaPlatos,"tabla1")
