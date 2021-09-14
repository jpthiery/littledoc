import logging

import smalldoc
import os

WORKING_DIR = f'{os.path.dirname(__file__)}/data'
MODULE_NAME = 'fakemodule'

logger = logging.getLogger(__name__)

def test_write_doc():
    parsed_module = smalldoc.parse(WORKING_DIR, MODULE_NAME)
    result = smalldoc.write(parsed_module)
    logger.debug(result)
