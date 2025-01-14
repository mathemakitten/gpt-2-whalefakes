# search example -- from:@TWITTERHANDLE exclude:replies since:2016-01-01 until:2017-06-29 

tweets = []
num_tweets = 0

TWEET_FILE = "copied_whalefact_tweets.txt" 
OUT_FILE = "whale_tweets.txt" 

with open(TWEET_FILE, "r") as myfile:
    lines = myfile.readlines()

    for i in range(len(lines)):
        line = lines[i]

        if line[0:6] == 'Reply ':
            num_tweets += 1
            print(num_tweets)
            tweets.append(lines[i-2])

# Write the tweets to a corpus for training

text_corpus = ''

for tweet in tweets:
    text_corpus += tweet
    text_corpus += '\n'

text_corpus += '\n\n'

# Save the data to a file for training
with open(OUT_FILE, "w") as f:
    f.write(text_corpus)


#PYTHONPATH=src ./train.py --dataset whale_tweets_all.txt --model_name=345M --val_every 200 --sample_every=250 --learning_rate=0.0001 --run_name='whalefacts'
