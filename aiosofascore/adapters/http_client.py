from aiohttp import ClientSession, ClientResponse, TCPConnector
import certifi
import ssl

from aiosofascore.exception import ResponseParseContentError

__all__ = ['HttpSessionManager']

class HttpSessionManager:
    def __init__(self, base_url:str):
        self.BASE_URL = base_url
        self.cookies = {}
    
    def set_cookies(self, cookies: dict):
        """Set cookies for requests"""
        self.cookies.update(cookies)
    
    async def __aenter__(self):
        headers = {
            'accept': 'application/json',
            'accept-language': 'ru,en;q=0.9',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36',
            'referer': 'https://www.sofascore.com/',
            'origin': 'https://www.sofascore.com',
            'accept-encoding': 'gzip, deflate, br',
            'connection': 'keep-alive'
        }
        
        # Cookies from browser
        cookies = {
            '_ga': 'GA1.1.729489537.1752538361',
            'FCCDCF': '%5Bnull%2Cnull%2Cnull%2C%5B%22CQUmAQAQUmAQAEsACBRUBzFoAP_gAEPgAA6IKkAB5C5GTSFBYT51KIsEYAAHwBAAIsAgAgYBAwABQJKU4JQCBGAAEAhAhiICkAAAKlSBIAFACBAQAAAAAAAAIAAEIAAQgAAIICAAAAAAAABICAAoAIoAEAAAwDiABAUAkBgMANIISNyQCQAABSCAQgAAEACAAQAAAEhgAAAAIAAAEGgEEIBAWAAAEEEYABlMhAAoIAgAAAAAQAgAQCQBRQACgAAAADQgABAMFRwA8hciJpCgsBwqkEWCEAAL4AgAEWAQAAMAwYAAoElKcEIBCjAAAAQAABEACAAAESoAkACAAAwAAAAAAAAAEAASAAAIQAAEEBAAABAAAAAgAAAEAEUACAAAYBQAAgKAQIQGAGkAJC5IBIAQApBAIEAACABAAIAAACQwAAAAEAAACCAACEAgLAAACAAIAAymQgAQEAAAAAAAIAQAIBIQogABAAAAABoQAAAEAAA.dngACAAAAAA%22%2C%222~55.70.89.108.135.147.149.184.211.259.272.313.314.358.385.415.442.486.540.621.938.981.1029.1031.1033.1046.1067.1092.1097.1126.1205.1268.1301.1329.1514.1516.1558.1579.1584.1598.1616.1651.1697.1716.1753.1782.1810.1832.1859.1917.1985.1987.2010.2068.2069.2140.2224.2271.2282.2316.2328.2331.2373.2387.2440.2501.2567.2571.2572.2575.2577.2628.2629.2642.2646.2650.2657.2677.2767.2778.2822.2860.2878.2887.2889.2898.2922.2970.3100.3169.3182.3190.3194.3215.3226.3234.3290.3292.3300.3330.3331.4631.10631.14332.28031.29631~dv.%22%2C%2200128800-CAA4-414D-BA10-8A7A7A8F1C8D%22%5D%5D',
            '__gads': 'ID=1d26fdee75e0a99a:T=1752538364:RT=1752538364:S=ALNI_MaIbn6v5BlT8MeusLQdVebaLAmkXg',
            '__gpi': 'UID=000011789a38d607:T=1752538364:RT=1752538364:S=ALNI_Mb1Z4-t04ogU6ngSyLAVyw7PYUF4w',
            '__eoi': 'ID=847c7becb190d20b:T=1752538364:RT=1752538364:S=AA-AfjZW9zgojew7EAiV84GT49Cn',
            'FCNEC': '%5B%5B%22AKsRol8-lIhFHDzBNFHYUCg4kz_Q-9-jgxZdUr4hycjlum5ptWGdw0nJT7iJM4pGHbXNsGBlSbwjaZw7WLkuFGWtTIF2GJwmL7Zq82_NWXTcALyEfHVnnHwPp4b0pqbNKtjUU_L5pxaTrIR61eJoRXDOQCMF6evyzA%3D%3D%22%5D%5D',
            'cto_bundle': 'Sb2Hhl9iJTJGWFFjSG1NY1U3bXlCeDVrVk9vJTJGeUY5cllHb25wNnR6ME9oWVZWbFhxWFp5ckdJdGczZFF3cWoxRGxhM1glMkZCQ1dOVUxKa1pXN25HMEptMXREZ3NoakRCTE0lMkJVTEtCajQxMGFHZFdoNjJjdldoJTJCWlNjNkxzVkhyM0ViblRBTnQ',
            'cto_bidid': 'L2_xZF9UTFZ1cnhDYURLSU1ialU3QiUyRkVMN3NPUUdTVXFiU0ZhaU55bnNCUFVQazklMkJmd3MlMkY2cU84WiUyQkF5JTJGYzJaNGVUWXlKczklMkJNZk9PR3BnUFdCOG96VE85USUzRCUzRA',
            '_ga_HNQ9P9MGZR': 'GS2.1.s1752538360$o1$g1$t1752538382$j42$l0$h0'
        }
        
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.session = ClientSession(headers=headers, cookies=cookies)
        return self

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
        if params is None:
            params = {}
        result = await self.session.get(self.BASE_URL + path, params=params, allow_redirects=False)
        if result.ok:
            return await result.json()
        raise ResponseParseContentError(result,path)
