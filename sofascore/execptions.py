from aiohttp import ClientResponse


class ResponseParseContentError(Exception):
    def __init__(self,response:ClientResponse,path:str):
        self._response = response
        self._path = path
    @property
    def response(self):
        return self._response

    def __str__(self):
        return ('Response processing error:\n'
                f'api call: {self._path}'
                f'response status:{self._response.status}'
                f'response content:{self._response.content}')