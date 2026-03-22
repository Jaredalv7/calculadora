#!/bin/bash

echo "Creando entorno virtual..."
python -m venv venv

echo "Activando entorno..."
source venv/bin/activate

echo "Instalando dependencias..."
pip install -r requirements.txt