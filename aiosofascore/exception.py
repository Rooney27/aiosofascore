from aiohttp import ClientResponse

__all__ = ['ResponseParseContentError']
class ResponseParseContentError(Exception):
    def __init__(self,response:ClientResponse,path:str):
        self._response = response
        self._path = path
    @property
    def response(self):
        return self._response

    def __str__(self):
        return ('Response processing error:\n'
                f'Api call: {self._path}\n'
                f'Response status: {self._response.status}\n')