from dash import Dash, html, dcc
import plotly.express as px
import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='12345',
        database='Proyecto Final')
    
    print("Conexión exitosa")
    cursor=connection.cursor()
    
    #Consulta1
    cursor.execute("select u.ciudad, sum(e.precio_total) as suma, rank() over(order by sum(e.precio_total) desc) from envio as e, Cliente as c, Residencia as r, Ubicacion as u where u.Ciudad = r.Ciudad_Ubicacion and u.Codigo_Postal = r.Codigo_postal_Ubicacion and r.ID_Cliente = c.ID and c.ID = e.ID_Cliente group by u.Ciudad order by rank asc")
    #Consulta2
    #cursor.execute("select P.Nombre, rank() over(order by sum(Precio_Total))")
    
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
