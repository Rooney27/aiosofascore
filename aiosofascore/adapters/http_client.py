from aiohttp import ClientSession, ClientResponse, TCPConnector
import certifi
import ssl

from aiosofascore.exception import ResponseParseContentError

__all__ = ['HttpSessionManager']

class HttpSessionManager:
    def __init__(self, base_url:str):
        self.BASE_URL = base_url
    async def __aenter__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'
        }
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.session = ClientSession(connector=TCPConnector(ssl=ssl_context), headers=headers)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get(self, path: str, params: dict = None) -> ClientResponse:
        """
        Executes an HTTP GET request to the given API path.

        Args:
            path (str): The API path to request.
            params (dict, optional): Query parameters for the request.

        Returns:
            ClientResponse: The response from the API.
        """
        result = await self.session.get(self.BASE_URL + path, params=params)
        if result.ok:
            return await result.json()
        raise ResponseParseContentError(result,path)
