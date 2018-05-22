import praw

def search_dev_diary():
	reddit = praw.Reddit("GCRedditBot")
	subreddit = reddit.subreddit("stellaris")
	submissions = subreddit.search("stellaris dev diary", sort = "new",time_filter= "week")

	for submission in submissions:
		if(submission.link_flair_text == "Dev diary"):
			return submission
	return None

def main():
	submission = search_dev_diary()
	if(submission == None):
		print("no dev diary found.")
	else:
		print(submission.url)

if __name__ == "__main__":
	main()	
