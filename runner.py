from app import create_app
from app import logger


app = create_app()
logger.debug('Runner is work!')
app.run(debug=True)