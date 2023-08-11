import json
import os
from googleapiclient.discovery import build


# z9Ko9IeMRkJHgeqVyB7tPO9k6Y7tx1t4
#api_key: str = os.getenv("YT_API_KEY")

#youtube = build("youtube", "v3", developerKey=api_key)
#print(api_key)
class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        api_key: str = os.getenv("YT_API_KEY")

        youtube = build("youtube", "v3", developerKey=api_key)
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.dict_of_channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.dict_of_channel.get("items")[0].get("snippet").get("title")
        self.description = self.dict_of_channel.get("items")[0].get("snippet").get("description")
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.count_subscribers = int(self.dict_of_channel.get("items")[0].get("statistics").get("subscriberCount"))
        self.video_count = int(self.dict_of_channel.get("items")[0].get("statistics").get("videoCount"))
        self.all_count_views = int(self.dict_of_channel.get("items")[0].get("statistics").get("viewCount"))

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API """
        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))

    @staticmethod
    def __printj(dict_of_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами."""
        print(json.dumps(dict_of_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """ Выводит в консоль информацию о канале """
        self.__printj(self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute())

    def to_json(self, filename):
        """ Метод, сохраняющий в файл значения атрибутов экземпляра Channel """
        data = {
            "title": self.title,
            "channel_id": self.channel_id,
            "description": self.description,
            "url": self.url,
            "count_subscribers": self.count_subscribers,
            "video_count": self.video_count,
            "all_count_views": self.all_count_views
        }
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)