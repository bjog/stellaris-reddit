import praw

def main():
	reddit = praw.Reddit("GCRedditBot")
	subreddit = reddit.subreddit("stellaris")
	
	for submission in subreddit.hot(limit=5):
		print("Title: ", submission.title)

if __name__ == "__main__":
	main()	
