#part 2
#reddit bot that will look for "s a masterpiece" and reply with a link to my soundcloud

###########SCRIPT WORKS!!!##############
import praw
import pdb
import re
import os
import time

#reddit = praw.Reddit("masterpeace_bot")  <--- DOESNT WORK
start = time.time()

END_TIME = 300
#works!
reddit = praw.Reddit(client_id = "YOUR INFO",
client_secret = "YOUR INFO",
password = "YOUR INFO",
username = "YOUR INFO",
user_agent = "masterpeace bot 1.0")


if not os.path.isfile("comments_replied.txt"):
	comments_replied = []
else:
	with open("comments_replied.txt", "r") as f:
		comments_replied = f.read()
		comments_replied = comments_replied.split("\n")
		comments_replied = list(filter(None, comments_replied))


subreddit = reddit.subreddit('all')


#to reply to comments that say "s a masterpiece"
for comment in subreddit.stream.comments():
	#print(comment.body) #livestream of current comments
	if comment.id not in comments_replied:
		if re.search("s a masterpiece", comment.body, re.IGNORECASE):
			if re.search("A masterpiece you say", comment.body, re.IGNORECASE):
				pass
			else:
				comment.reply("A masterpiece you say? Well check this out! https://soundcloud.com/masterpeacerecords/tracks")
				comments_replied.append(comment.id) #add comment id to list

				#this is just to check where the script is, not necessary
				print('##################################################')
				print(comment.author, "SAID \"S A MASTERPIECE\"")
				print("REPLYING")
				print("##################################################")



	if time.time() > start + END_TIME:
		break

print("THE PROGRAM RAN FOR THIS LONG: ",start+END_TIME)

with open("posts_replied_to.txt", "w") as f:
	for comment_id in comment_replied:
		f.write(comment_id + "\n")

f.close()
