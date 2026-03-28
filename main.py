from keep_alive import keep_alive
from bot import main

if __name__ == "__main__":
    keep_alive()   # Arranca el servidor Flask en hilo daemon
    main()         # Arranca el bot (bloqueante)
