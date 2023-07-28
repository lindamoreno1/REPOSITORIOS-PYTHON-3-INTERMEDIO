# %%
import requests
from bs4 import BeautifulSoup

pagWeb=requests.get("https://juliocepeda.com/rebajas.html")
soup= BeautifulSoup(pagWeb.text,"html.parser")
print(soup.prettify())

# %%
def obtener_contenido_pagina(url):
    response = requests.get(url)
    return response.content


def analizar_contenido_html(html):
    return BeautifulSoup(html, 'html.parser')

# %%
data = []

def procesar_pagina(soup):
   productos=[]
   precios=[]
   aprecios=[]
   
   productos_items=soup.find_all("a",class_="product-item-link")
   for item in productos_items:
      producto=item.text.strip()
      productos.append(producto)
   
   
   precio_items=soup.find_all("span",class_="special-price")
   for item in precio_items:
      precio=item.text.strip()
      precios.append(precio.lstrip("Precio\n"))



   precioo_items=soup.find_all("span",class_="old-price")
   for item in precioo_items:
         precioo=item.text.strip()
         aprecios.append(precioo.lstrip("Precio habitual\n"))


   

# %%
x=len(productos)

# %%
for i in range(0,x):
        data.append({
            "Articulo": productos[i],
            "Precio Regular": aprecios[i],
            "Precio Oferta": precios[i],  
        })

# %%
import pandas as pd

df = pd.DataFrame(data)

# %%
df

# %%
import datetime
fecha_actual=datetime.datetime.now().strftime("%d-%m-%Y")
df.to_csv(f"Jugueteria-(fecha_actual).csv",index=False)



