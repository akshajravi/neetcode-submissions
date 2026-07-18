class Twitter:

    def __init__(self):
        self.followMap = {} # user:followers     
        self.tweetMap = {} # user:(num tweets,tweetId)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.count += 1
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = set()
        feed.add(userId)
        if userId in self.followMap:
            feed.update(self.followMap[userId])
        for user in feed:
            if user in self.tweetMap:
                for count, tweet in self.tweetMap[user]:
                    heapq.heappush(heap,[-count,tweet])
        res = []
        i = 10
        while heap and i > 0:
            count,tweet = heapq.heappop(heap)
            res.append(tweet)
            i-=1
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
