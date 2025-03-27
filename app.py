import logging
import time
import os

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/app/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Criar diretório de logs se não existir
os.makedirs('/var/log/app', exist_ok=True)

# Gerar logs continuamente
if __name__ == "__main__":
    counter = 0
    while True:
        logger.info(f"Esta é uma mensagem de log de informação #{counter}")
        if counter % 5 == 0:
            logger.warning(f"Este é um log de aviso #{counter}")
        if counter % 10 == 0:
            logger.error(f"Este é um log de erro #{counter}")
        
        counter += 1
        time.sleep(2)