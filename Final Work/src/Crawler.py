# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Tweet-Lookup/get_tweets_with_bearer_token.py
import os

import requests
import json
import time
from tqdm import tqdm

bearer_token = "AAAAAAAAAAAAAAAAAAAAAAKibgEAAAAAxQFMdEHv6SCEGrimaLdkF2kCGiM%3D1tFMGCibZHM2hbbjARFom1C52fGFer7Hv5yOH0SLzOQSKpprCf"


def create_url(ids):
    tweet_fields = "tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=" + ids
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def bearer_oauth(r):  # Method required by bearer token authentication.
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def crawl_and_save(f_in, f_out):
    id_list = []
    for line in f_in.readlines():
        id_list.extend(line.strip().split(","))
    start_id = 0
    end_id = start_id + 100  # max 100 tweets per request
    split_crawl = []
    while start_id < len(id_list):
        split_crawl.append(",".join(id_list[start_id:end_id]))
        start_id = end_id
        end_id = start_id + 100

    crawl_count = 0
    for ids in tqdm(split_crawl):
        url = create_url(ids)
        json_response = connect_to_endpoint(url)
        for x in json_response["data"]:
            json.dump(x, open(f_out + str(x["id"]) + ".json", "w"))
        crawl_count += 1
        if crawl_count % 299 == 0:  # 299 requests per 15 minutes
            time.sleep(900)  # 15 min sleep


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    # print("Crawling the training data...")
    # create_directory("data/train/")
    # crawl_and_save(open("data/train.data.txt", "r"), "data/train/")
    # print("Training data crawled.")
    #
    # print("Crawling the dev data...")
    # create_directory("data/dev/")
    # crawl_and_save(open("data/dev.data.txt", "r"), "data/dev/")
    # print("Dev data crawled.")
    #
    # print("Crawling the test data...")
    # create_directory("data/test/")
    # crawl_and_save(open("data/test.data.txt", "r"), "data/test/")
    # print("Test data crawled.")

    print("Crawling the data for task 2...")
    create_directory("data/task 2/")
    crawl_and_save(open("data/covid.data.txt", "r"), "data/task 2/")
    print("Task 2 data crawled.\n")

    print("Finished with all data.")


if __name__ == "__main__":
    main()
