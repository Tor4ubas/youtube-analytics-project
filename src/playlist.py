from googleapiclient.discovery import build

import os
from datetime import datetime
import datetime
import isodate

class PlayList():

    """ класс PlayList, который инициализируется id плейлиста """

    def __init__(self, playlist_id):

        """ Инициализация атрибутов """

        self.playlists_videos = (PlayList.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails, snippet', maxResults=50, ).execute())
        self.playlists_video = PlayList.get_service().playlists().list(id=playlist_id, part='snippet', maxResults=50, ).execute()

        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlists_videos['items']]
        self.video_response = self.get_service().videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()

        self.playlist_id = playlist_id
        self.title = self.playlists_video['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"


    @classmethod
    def get_service(cls):

        """ Возвращает объект для работы с YouTube API """

        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))


    @property
    def total_duration(self):

        """ возвращает объект класса datetime.timedelta с суммарной длительность плейлиста """

        all_time = []

        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            durations = isodate.parse_duration(iso_8601_duration)
            all_time.append(durations)

        duration = sum(all_time, datetime.timedelta())

        return duration


    def show_best_video(self):

        """ возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков) """

        global video

        for video in self.video_ids:
            best_video = 0
            count_like = self.video_response["items"][0]["statistics"]["likeCount"]
            if int(count_like) > best_video:
                best_video = count_like

        return f"https://youtu.be/{video}"