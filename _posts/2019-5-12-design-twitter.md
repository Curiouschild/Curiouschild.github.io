---
title:  "355. Design Twitter"
date:   2019-05-12 22:03:00 +0930
categories: Leetcode
tags: Medium HashMap
---

[{{page.title}}](https://leetcode.com/problems/design-twitter/){:target="_blank"}

    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is
    able to see the 10 most recent tweets in the user's news feed. Your design should support the following
    methods:

        postTweet(userId, tweetId): Compose a new tweet.
        getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the
        news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered
        from most recent to least recent.
        follow(followerId, followeeId): Follower follows a followee.
        unfollow(followerId, followeeId): Follower unfollows a followee.

    Example:

    Twitter twitter = new Twitter();

    // User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5);

    // User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1);

    // User 1 follows user 2.
    twitter.follow(1, 2);

    // User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6);

    // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1);

    // User 1 unfollows user 2.
    twitter.unfollow(1, 2);

    // User 1's news feed should return a list with 1 tweet id -> [5],
    // since user 1 is no longer following user 2.
    twitter.getNewsFeed(1);


* HashMap

Succeed on first submission.

```java

class Twitter {
    HashMap<Integer, HashSet<Integer>> fmap;
    HashMap<Integer, ArrayList<int[]>> tmap;
    int index = 0;
    /** Initialize your data structure here. */
    public Twitter() {
        fmap = new HashMap<>();
        tmap = new HashMap<>();
    }

    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        ArrayList<int[]> ts = tmap.getOrDefault(userId, new ArrayList<>());
        ts.add(new int[] {tweetId, index++});
        tmap.put(userId, ts);
    }

    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        ArrayList<Integer> result = new ArrayList<>();
        HashSet<Integer> set = fmap.getOrDefault(userId, new HashSet<>());
        HashSet<Integer> users = new HashSet<>(set);
        users.add(userId);
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int u : users) map.put(u, tmap.containsKey(u) ? tmap.get(u).size()-1 : -1);
        for(int i = 0; i < 10; i++) {
            int max = -1;
            int choose = -1;
            int tId = -1;
            for(int u : users) {
                if(!tmap.containsKey(u)) continue;
                ArrayList<int[]> ts = tmap.get(u);
                int p = map.get(u);
                if(p == -1) continue;
                int[] t = ts.get(p);
                if(t[1] > max) {
                    max = t[1];
                    choose = u;
                    tId = t[0];
                }
            }
            if(max == -1) break;
            map.put(choose, map.get(choose)-1);
            result.add(tId);
        }
        return result;
    }

    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if(followerId == followeeId) return;
        HashSet<Integer> set = fmap.getOrDefault(followerId, new HashSet<>());
        set.add(followeeId);
        fmap.put(followerId, set);
    }

    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if(!fmap.containsKey(followerId) || !fmap.get(followerId).contains(followeeId)) return;
        HashSet<Integer> set = fmap.getOrDefault(followerId, new HashSet<>());
        set.remove(followeeId);
        fmap.put(followerId, set);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
```
