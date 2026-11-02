import os
from flask import Flask, render_template, request, redirect, url_for
from data_base import database

app = Flask(__name__)

@app.route('/')
def inicio():
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT prompt FROM card")
    prompts = cursor.fetchall()
    conn.close()
    
    return render_template ('index.html', prompts = prompts) 

@app.route('/guardar_prompt', methods = ['POST'])
def guardar_prompt():
    prompts = request.form.get('prompts')

    conn = database()
    cursor = conn.cursor()

    cursor.execute ("INSERT INTO card (prompt) VALUES (?)", (prompts,))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('inicio'))

if __name__ == '__main__':
    # Asigna el puerto de Render en la nube o el 5000 en local
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)