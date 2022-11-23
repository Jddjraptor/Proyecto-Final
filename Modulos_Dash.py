from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='12345',
        database='Proyecto Final'
    )
    print("Conexión exitosa")
    #Consulta1
    cursor=connection.cursor()
    cursor.execute("select distinct u.Ciudad, sum(e.Precio_Total), rank() over(partition by u.ciudad order by e.Precio_Total desc) from Ubicacion as u, Envio as e, Cliente as c, Residencia as r where u.Ciudad = r.Ciudad_Ubicacion and r.ID_Cliente = c.ID and e.ID_cliente = c.ID group by u.Ciudad, e.Precio_Total order by rank asc")
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
