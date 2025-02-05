from typing import Optional, Iterator
from pydantic import BaseModel, fields, Field



class Sport(BaseModel):
    """
    Represents a sport entity with essential attributes.

    Attributes:
        name (str): Name of the sport.
        slug (str): URL-friendly identifier for the sport.
        id (int): Unique identifier for the sport.
    """
    name: str
    slug: str
    id: int


class Category(BaseModel):
    """
    Represents a category associated with a sport.

    Attributes:
        name (str): Name of the category.
        slug (str): URL-friendly identifier for the category.
        sport (Sport): The sport associated with this category.
        priority (Optional[int]): Priority level for the category (if available).
        id (int): Unique identifier for the category.
        flag (str): Country flag or symbol associated with the category.
    """
    name: str
    slug: str
    sport: Sport
    priority: Optional[int] = None
    id: int
    flag: str


class CategoryList(BaseModel):
    """
    Represents a list of Category objects with search functionality.

    Attributes:
        categories (list[Category]): A list containing Category objects.

    Methods:
        find_all_by_name(name: str, search_amateur: bool = False) -> list[Category]:
            Finds categories by name with an optional search for amateur categories.
    """
    categories: list[Category]

    def find_all_by_name(self, name: str, search_amateur=False) -> list[
        Category]:
        """
        Finds all categories whose names contain the given substring.

        Args:
            name (str): The substring to search for in category names.
            search_amateur (bool, optional): Whether to include only amateur categories. Defaults to False.

        Returns:
            list[Category]: A list of categories matching the criteria.
        """
        return [c for c in self.categories if
                name.lower() in c.name.lower() and
                ('amateur' in c.name.lower()) == search_amateur]
    def __iter__(self)->Iterator[Category]:
        return iter(self.categories)

    def __getitem__(self, index: int) -> Category:
        return self.categories[index]

class UniqueTournament(BaseModel):
    """
    Represents a unique soccer tournament.

    Attributes:
        name (str): Name of the tournament.
        slug (str): URL-friendly identifier for the tournament.
        primaryColorHex (Optional[str]): Primary color in hexadecimal format.
        secondaryColorHex (Optional[str]): Secondary color in hexadecimal format.
        category (Category): The category associated with the tournament.
        userCount (int): Number of users following the tournament.
        id (int): Unique identifier for the tournament.
        displayInverseHomeAwayTeams (bool): Flag indicating if home/away teams should be inversed in display.
    """
    name: str
    slug: str
    primaryColorHex: Optional[str] = None
    secondaryColorHex: Optional[str] = None
    category: Category
    userCount: int
    id: int
    displayInverseHomeAwayTeams: bool

class UniqueTournamentsList(BaseModel):
    unique_tournaments: list[UniqueTournament]

    def __iter__(self)->Iterator[UniqueTournament]:
        return iter(self.unique_tournaments)

    def __getitem__(self, index: int) -> UniqueTournament:
        return self.unique_tournaments[index]

class Tournament(BaseModel):
    category: Category
    id: int
    is_group: bool = Field(..., alias="isGroup")
    is_live: bool = Field(..., alias="isLive")
    name: str
    priority: int
    slug: str
    uniqueTournament: UniqueTournament


class Promotion(BaseModel):
    id: int
    text: str


class Team(BaseModel):
    disabled: bool
    entityType: str
    gender: str
    id: int
    name: str
    name_code: str = Field(..., alias="nameCode")
    national: bool
    short_name: str = Field(..., alias="shortName")
    slug: str


class StandingsRow(BaseModel):
    descriptions: list[str]
    draws: int
    id: int
    losses: int
    matches: int
    points: int
    position: int
    promotion: Promotion = None
    score_diff_formatted: str = Field(..., alias="scoreDiffFormatted")
    scores_against: int = Field(..., alias="scoresAgainst")
    scores_for: int = Field(..., alias="scoresFor")
    team: Team
    wins: int


class Standings(BaseModel):
    descriptions: list[str]
    id: int
    name: str
    rows: list[StandingsRow]
    tournament: Tournament


class Season(BaseModel):
    name: str
    year: str
    editor: bool
    id: int


class SeasonList(BaseModel):
    seasons: list[Season]

    def get_season_by_year(self, year: str) -> Season:
        return next((season for season in self.seasons if season.year == year),
                    None)

    def get_current_season(self) -> Season:
        return self.seasons[0]

    def __iter__(self) ->Iterator[Season]:
        return iter(self.seasons)

    def __getitem__(self, index: int) -> Season:
        return self.seasons[index]

class TeamForm(BaseModel):
    avg_rating: str = Field(alias='avgRating')
    form: list[str]
    position: int
    value: str


class PregameTeamForm(BaseModel):
    away_team: TeamForm = Field(alias='awayTeam')
    home_team: TeamForm = Field(alias='homeTeam')


class Duel(BaseModel):
    away_wins: int = Field(alias='awayWins')
    draws: int
    home_wins: int = Field(alias='homeWins')


class H2H(BaseModel):
    manager_duel: Duel = Field(alias='managerDuel')
    team_duel: Duel = Field(alias='teamDuel')


class Manager(BaseModel):
    name: str
    slug: str
    short_name: str = Field(alias='shortName')
    id: str


class EventManagers(BaseModel):
    home_manager: Manager = Field(alias='homeManager')
    away_manager: Manager = Field(alias='awayManager')


class RoundInfo(BaseModel):
    round: int


class City(BaseModel):
    name: str


class VenueCoordinates(BaseModel):
    latitude: str
    longtitude: str


class Country(BaseModel):
    alpha2: str
    alpha3: str
    name: str
    slug: str


class Stadium(BaseModel):
    name: str
    capacity: int


class Venue(BaseModel):
    city: City
    venue_coordinates: VenueCoordinates = Field(alias='venueCoordinates')
    hidden: bool
    slug: str
    name: str
    capacity: int
    id: int
    country: Country
    stadium: Stadium


class Referee(BaseModel):
    name: str
    slug: str
    yellow_cards: int = Field(alias='yellowCards')
    red_cards: int = Field(alias='redCards')
    yellow_red_cards: int = Field(alias='yellowRedCards')
    games: int
    sport: Sport
    id: int
    country: Country


class EventTeam(Team):
    sport: Sport
    manager: Manager
    venue: Venue
    country: Country


# TODO: Create Prematch,live,fulltime Event
class Event(BaseModel):
    tournament: Tournament
    season: Season
    round_info: RoundInfo = Field(alias='roundInfo')
    custom_id: str = Field(alias='customId')
    venue: Venue
    home_team: EventTeam = Field(alias='homeTeam')
    away_team: EventTeam = Field(alias='awayTeam')
