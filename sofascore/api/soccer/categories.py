from typing import Union

from sofascore.api.soccer.schemas.base import CategoryList, Category

__all__ = ['SoccerCategoriesApi']

class SoccerCategoriesApi:
    async def get_categories(self) -> Union[CategoryList,list]:
        """
        Fetches a list of soccer categories.

        Returns:
            CategoryList: A list of soccer categories encapsulated in a CategoryList object.
            Returns an empty list if an error occurs during the request or JSON parsing.
        """
        async with self:
            content = await self._get('api/v1/sport/football/categories/')
            return CategoryList(
                    categories=[Category(**category) for category in
                                content['categories']]
                )