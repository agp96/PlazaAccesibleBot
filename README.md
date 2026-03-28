# ♿ Bot de Aparcamiento para Discapacitados

Bot de Telegram que localiza plazas de aparcamiento reservadas para PMR
usando datos de OpenStreetMap (Overpass API). Gratis, sin APIs de pago.

## Estructura

```
main.py          ← punto de entrada (arranca keep_alive + bot)
bot.py           ← lógica del bot
keep_alive.py    ← servidor Flask para que Replit no duerma
requirements.txt
```

## Despliegue en Replit

### 1. Variables de entorno (Secrets)
En Replit → *Secrets* añade:
| Key | Value |
|-----|-------|
| `TELEGRAM_TOKEN` | El token que te da @BotFather |

### 2. Instalar dependencias
Replit lo hace automáticamente al detectar `requirements.txt`.
Si no: abre la Shell y ejecuta:
```bash
pip install -r requirements.txt
```

### 3. Run
Configura el botón Run para ejecutar `main.py` o en `.replit`:
```toml
[run]
entrypoint = "main.py"
```

### 4. Keep-alive (automático, sin servicios externos)
El bot se hace ping a sí mismo cada 4 minutos. Solo añade en Secrets:

| Key | Value |
|-----|-------|
| `REPLIT_URL` | `https://tu-repl.tuuser.repl.co` |

Si no añades `REPLIT_URL` hace ping a localhost igualmente.

## Uso del bot

1. `/start` — Mensaje de bienvenida
2. `/ayuda` — Instrucciones
3. Enviar 📍 ubicación → devuelve hasta 8 plazas PMR en 800 m ordenadas por distancia

## Datos

- Fuente: [OpenStreetMap](https://www.openstreetmap.org) vía Overpass API
- Cobertura: depende de lo mapeado por la comunidad OSM
- Actualización: en tiempo real (la API siempre tiene los datos más recientes)

## Posibles mejoras futuras

- [ ] Ampliar radio si no hay resultados (ej: reintentar a 1500 m)
- [ ] Botón para reportar plaza nueva (enlace directo a OSM editor)
- [ ] Inline mode para compartir resultados en grupos
- [ ] Cache de consultas recientes para reducir llamadas a Overpass
