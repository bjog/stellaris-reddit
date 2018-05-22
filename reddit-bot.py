import praw

def search_dev_diary():
	reddit = praw.Reddit("GCRedditBot")
	subreddit = reddit.subreddit("stellaris")
	submissions = subreddit.search("stellaris dev diary", sort="new", time_filter= "week")
	for submission in submissions:
		print(submission.title)

def main():
	search_dev_diary()
if __name__ == "__main__":
	main()	
