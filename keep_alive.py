"""
Self-ping: servidor Flask mínimo + hilo que se hace ping a sí mismo
cada 4 minutos para que Replit no duerma. Sin servicios externos.
"""
import os
import time
import logging
import requests
from flask import Flask
from threading import Thread

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    return "♿ Bot de Aparcamiento PMR activo ✅"

@app.route("/ping")
def ping():
    return "pong", 200

def run_server():
    app.run(host="0.0.0.0", port=8080)

def self_ping():
    """Hace ping a sí mismo cada 4 minutos para evitar el sleep de Replit."""
    url = os.environ.get("REPLIT_URL", "http://localhost:8080") + "/ping"
    time.sleep(30)  # Espera inicial para que el servidor arranque
    while True:
        try:
            requests.get(url, timeout=10)
            logger.info("Self-ping OK")
        except Exception as e:
            logger.warning(f"Self-ping fallido: {e}")
        time.sleep(240)  # 4 minutos

def keep_alive():
    # Hilo del servidor Flask
    t_server = Thread(target=run_server)
    t_server.daemon = True
    t_server.start()

    # Hilo del self-ping
    t_ping = Thread(target=self_ping)
    t_ping.daemon = True
    t_ping.start()
