from dash import Dash, html, dcc
import plotly.express as px
import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='Proyecto Final')
    
    print("Conexión exitosa")
    cursor=connection.cursor()
    
    cursor.execute("select u.ciudad, sum(e.precio_total) as suma, rank() over(order by sum(e.precio_total) desc) from envio as e, Cliente as c, Residencia as r, Ubicacion as u where u.Ciudad = r.Ciudad_Ubicacion and u.Codigo_Postal = r.Codigo_postal_Ubicacion and r.ID_Cliente = c.ID and c.ID = e.ID_Cliente group by u.Ciudad order by rank asc")
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    print("\n")
        
    cursor.execute("select p.nombre, sum(e.precio_total) as suma, rank() over(order by sum(e.precio_total) desc) from producto as p, envio as e, Cliente as c, Residencia as r, Ubicacion as u where u.Ciudad = r.Ciudad_Ubicacion and u.Codigo_Postal = r.Codigo_postal_Ubicacion and r.ID_Cliente = c.ID and c.ID = e.ID_Cliente and e.ID_Producto = p.ID and e.Nombre_Producto = p.Nombre and u.Ciudad = 'New York City' group by p.nombre order by rank asc")
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
    print("\n")
        
    cursor.execute("select e.medio, count(e.id) as conteo, rank() over(order by count(e.id) desc) from envio as e, Cliente as c, Residencia as r, Ubicacion as u where u.Ciudad = r.Ciudad_Ubicacion and u.Codigo_Postal = r.Codigo_postal_Ubicacion and r.ID_Cliente = c.ID and c.ID = e.ID_Cliente and u.Ciudad = 'New York City' group by e.medio order by rank asc")
     
    rows=cursor.fetchall()
    for row in rows:
        print(row)
     
    print("\n")
        
    cursor.execute("select p.categoria, count(e.id) as conteo, rank() over(order by count(e.id) desc) from Producto as p, envio as e, Cliente as c, Residencia as r, Ubicacion as u where u.Ciudad = r.Ciudad_Ubicacion and u.Codigo_Postal = r.Codigo_postal_Ubicacion and r.ID_Cliente = c.ID and c.ID = e.ID_Cliente and e.ID_Producto = p.ID and e.Nombre_Producto = p.Nombre and u.ciudad = 'New York City' and e.medio = 'Standard Class' group by p.categoria order by rank asc")
    
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
    app = Dash(__name__)
    fig = px.bar(rows, x=0, y=1, color_discrete_sequence=["#b52a64"])'
    #fig = px.pie(rows, values=1, names=0, color_discrete_sequence=["#b52a64"])

    app.layout = html.Div(children=[
        html.H1(children='Grafico Edicion Cantidad'),

        html.Div(children='''
            Dash: Aplicación para gráficar datos
        '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    
    if __name__ == '__main__':
        app.run_server(debug=True)    

except Exception as ex:
    print(ex)
    
finally:
    connection.close()
    print("Conexion finalizada")
