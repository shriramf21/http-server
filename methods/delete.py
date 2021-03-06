import os
from logger import Logger
from response import createResponse
import pathlib

docRootPath = str(pathlib.Path().absolute()) + "/assets/"
logger = Logger()

def parseDeleteReq(headers, client):
    headerValues ={}
    body = []
    logger.clientAddr = client

    for i in headers[1:]:
        try:
            print(i)
            headerField = i[:i.index(':')]
            headerValues[headerField] = i[i.index(':') + 2:len(i) - 1]
        except:
            if i != '\r' and i != '\n':
                body.append(i)
    
    path = headers[0].split(' ')[1]
    path = docRootPath + path

    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)

            res = createResponse(0, 204)
            logger.createLog(headers[0], res)
            return res

        else:
            res = createResponse(0, 403)
            logger.createErrorLog(headers[0], res)
            return res
    
    else:
        res = createResponse(0, 404)
        logger.createErrorLog(headers[0], res)
        return res