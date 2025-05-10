# Admin-GrafomotorIA 🧠✨

Sistema de administración para **GrafomotorIA**, desarrollado para Teletón.  
Permite gestionar usuarios, pacientes, sesiones y más, sobre una base de datos real conectada a MySQL.

## 🔧 Tecnologías utilizadas

- Django 5.2.1
- MySQL
- HTML y CSS puro (sin frameworks)
- Bootstrap (complementario para interfaz)
- Visual Studio Code
- Git + GitHub

## 📂 Funcionalidades

- Inicio de sesión personalizado
- Panel de usuarios con creación y visualización
- Conexión directa a base de datos `teleton` en MySQL (AWS)
- Modelos reflejados con `db_table`
- Panel de administración completo en `/admin`

## 🔑 Acceso

Para ingresar al sistema:
- Visita `http://127.0.0.1:8000/` para iniciar sesión
- Usa credenciales cargadas previamente en la base de datos

## ▶️ Instrucciones para correr localmente

```bash
git clone https://github.com/elshishapablo/Admin-GrafomotorIA.git
cd Admin-GrafomotorIA
python -m venv env
env\Scripts\activate     # En Windows
pip install -r requirements.txt
python manage.py runserver


Proyecto creado por @elshishapablo
Contacto: pab.aravena.16@gmail.com