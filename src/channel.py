import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__youtube = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.__youtube['items'][0]['snippet']['title']
        self.description = self.__youtube['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.quantity_subscribers = self.__youtube['items'][0]['statistics']['subscriberCount']
        self.video_count = self.__youtube['items'][0]['statistics']['videoCount']
        self.quantity_views = self.__youtube['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__youtube, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self):
        return self.__channel_id

    def to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file, indent=2)

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other) -> int:
        return int(self.quantity_subscribers) + int(other.quantity_subscribers)

    def __sub__(self, other) -> int:
        return int(self.quantity_subscribers) - int(other.quantity_subscribers)

    def __ge__(self, other) -> bool:
        return int(self.quantity_subscribers) >= int(other.quantity_subscribers)

    def __gt__(self, other) -> bool:
        return int(self.quantity_subscribers) > int(other.quantity_subscribers)

    def __le__(self, other) -> bool:
        return int(self.quantity_subscribers) <= int(other.quantity_subscribers)

    def __lt__(self, other) -> bool:
        return int(self.quantity_subscribers) < int(other.quantity_subscribers)

    def __eq__(self, other) -> bool:
        return int(self.quantity_subscribers) == int(other.quantity_subscribers)

    def __ne__(self, other) -> bool:
        return int(self.quantity_subscribers) != int(other.quantity_subscribers)
