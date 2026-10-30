class Twitter:

    def __init__(self):
        self.users_to_tweets = collections.defaultdict(set)
        self.users_to_followees = collections.defaultdict(set)
        self.date = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users_to_tweets[userId].add((self.date, tweetId))
        self.date += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_by_user = self.users_to_tweets[userId]
        heap = [ (-data, tweetId) for data, tweetId in tweets_by_user]
        heapq.heapify(heap)

        for followee in self.users_to_followees[userId]:
            for data, tweet in self.users_to_tweets[followee]:
                heapq.heappush(heap, (-data, tweet))

        top_tweets = heapq.nsmallest(10, heap)
        return [tweetId for _, tweetId in top_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_to_followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_to_followees[followerId]:
            self.users_to_followees[followerId].remove(followeeId)
        
