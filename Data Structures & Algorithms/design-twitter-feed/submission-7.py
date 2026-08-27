#heap is constructed and deconstructed when getNewsFeed is called
#follow is an adjacency list?? kind of like nodes connecting to each other

class Twitter:

    def __init__(self):
        self.user_posts = {}
        self.follows = {}
        self.count = 0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_posts:
            self.user_posts[userId] = []
        self.user_posts[userId].append((self.count, tweetId))
        self.count += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        tracking = self.follows.get(userId, set()) | {userId}


        for uid in tracking:
            if uid in self.user_posts and self.user_posts[uid]:
                index = len(self.user_posts[uid]) - 1
                count,tweetId = self.user_posts[uid][index]
                heapq.heappush(heap, (-count, tweetId, uid, index))

        res = []
        while heap and len(res) < 10:
            negCount, tweetId, uid, index = heapq.heappop(heap)
            res.append(tweetId)

            index -=1
            if index >= 0:
                count, nextTweetId = self.user_posts[uid][index]
                heapq.heappush(heap,(-count, nextTweetId, uid, index))
        
        return res

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        self.follows[followerId].discard(followeeId)


        
