from flask import Flask, jsonify

app = Flask(__name__)


MESSI_STATS = {
    "partidos_jugados": 1001,
    "goles": 804,
    "asistencias": 350
}

@app.route('/')
def messi_stats():
    partidos = MESSI_STATS["partidos_jugados"]
    goles = MESSI_STATS["goles"]
    asistencias = MESSI_STATS["asistencias"]

    total_goles_asistencias = goles + asistencias

    # Calcular promedio solo si hay partidos jugados para evitar división por cero
    if partidos > 0:
        promedio_gol_asistencia_por_partido = total_goles_asistencias / partidos
    else:
        promedio_gol_asistencia_por_partido = 0.0
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Estadísticas de Lionel Messi</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: auto;
                text-align: center;
            }}
            h1 {{
                color: #0056b3;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                margin-bottom: 10px;
                font-size: 1.1em;
            }}
            .highlight {{
                font-weight: bold;
                color: #d63384;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Estadísticas de Lionel Messi</h1>
            <p>Aquí tienes algunos datos impresionantes de la carrera de Messi:</p>
            <ul>
                <li>Partidos Jugados: <span class="highlight">{partidos}</span></li>
                <li>Goles: <span class="highlight">{goles}</span></li>
                <li>Asistencias: <span class="highlight">{asistencias}</span></li>
                <li>Total Goles + Asistencias: <span class="highlight">{total_goles_asistencias}</span></li>
                <li>Promedio Gol/Asistencia por Partido: <span class="highlight">{promedio_gol_asistencia_por_partido:.2f}</span></li>
            </ul>
            <p>¡Leyenda del fútbol!</p>
        </div>
    </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
