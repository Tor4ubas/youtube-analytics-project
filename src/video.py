from googleapiclient.discovery import build
import os

class Video():
    def __init__(self, video_id):
        self.dict_of_video = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                   id=video_id,).execute()
        self.video_id = video_id
        self.video_title = str(self.dict_of_video['items'][0]['snippet']['title'])
        self.video_url = f"https://youtu.be/gaoc9MPZ4bw/{self.video_id}"
        self.count_views = int(self.dict_of_video['items'][0]['statistics']['viewCount'])
        self.count_likes = int(self.dict_of_video['items'][0]['statistics']['likeCount'])

    @classmethod
    def get_service(cls):
        return build("youtube", "v3", developerKey=os.getenv("YT_API_KEY"))

    def __str__(self):
        return self.video_title

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)

        self.dict_of_video = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                   id=video_id,).execute()
        self.video_title = str(self.dict_of_video['items'][0]['snippet']['title'])
        self.video_url = f"https://youtu.be/gaoc9MPZ4bw/{self.video_id}"
        self.count_views = int(self.dict_of_video['items'][0]['statistics']['viewCount'])
        self.count_likes = int(self.dict_of_video['items'][0]['statistics']['likeCount'])
        self.playlist_id = playlist_id
