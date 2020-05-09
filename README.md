# HW4 Twitter Video Summarizer

## Assignment Requirements

### Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day

* Convert text into an image in a frame
* Do a sequence of all texts and images in chronological order.
* Display each video frame for 3 seconds

### Tasks

* Establish a processing criteria:
  * How many API calls you can handle simultaneously and why?
  * For example, run different API calls at the same time?
  * Split the processing of an API into multiple threads?*
* Recommendation for working on the homework:  
  * Step 1:
    * Develop a queue system that can exercise your requirements with stub functions.
  * Step 2:
    * Develop the twitter functionality with an API
  * Step 3:
    * Integrate them
* Include tracking interface to show how many processes are going on and success of each

## Documentation For Using This

Before you start you must make sure FFMPEG is installed on your computer

In the videoFFmpeg.py file, either change the values of the consumer_key, consumer_secret, access_token, or access_secret to be those of your keys, or change the FILE_PATH to lead to your own keys.py file with the format:

[consumer key]
[consumer secret]
[access token]
[access secret]

Then when you run this python file locally, it should generate 20 different images which are based on the tweets on your timeline and overlayed on a blue image, these images will always download in the format IMGPXXX.jpg, so it would overwrite any images from the prior run, and ask you if you want to rewrite the old video that was created. An example of one of these images is shown below.

![Example Image of Tweet Frame](./Images/IMGP004.jpg)

FFMPEG then uses threading for the downloading and generating of all of the frames occurring in the video and it is downloaded to a file called twitterTimelineSummary.avi it has 20 images in the video and each frame lasts for 3 seconds which makes it a minute long video.
