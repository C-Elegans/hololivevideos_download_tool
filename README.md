# Hololivevideos.download comparator tool
## Purpose
This tool searches the tables of videos on hololivevideos.download for any videos that are no longer on youtube (such as those taken down from copyright strikes) and displays the videos found

## Usage

1. Install python, git, pandas, and youtube-dl

	I can't really help you much here. Google it.

1. Download this tool


1. Choose a channel and download the table of videos from hololivevideos.download.

	Click on one of the channels available on hololivevideos.download. Once on the page showing the list of videos available for that channel, right on the page and select 'Save As'. Save the file somewhere easily accessible from the command line, and make sure the saved file is a '.html' file

1. Download a list of video ids available from the corresponding youtube channel with youtube-dl

	1. Navigate to the youtube channel of the person you selected in the previous step (if you selected Coco on hololivevideos.download, go to Coco's youtube channel).
	1. Copy the url of the youtube channel
	1. Run the following command, pasting the channel url in place of "URL\_HERE":

	Feel free to change `channel_ids.txt` to a filename of your choice

	```console
	youtube-dl -i --skip-download --get-id 'URL_HERE' > channel_ids.txt
	```
	
1. Generate a list of previously unavailable videos 
	
	Run the following command, subtituting the filenames you chose in the previous steps for the html file and text file listed:
	
	```console
	python compare_videos.py downloaded_page.html channel_ids.txt 
	```

	You can also add `-u urls_output.txt` to have the tool generate a list of urls for the videos it found.
	
## Notes

If you do decide to use an automated tool to download videos from this site, please note the following text at the top of the front page (translated with DeepL):

Note: Please ensure that the number of clicks on the download link per minute is less than or equal to 15, otherwise the IP will be blocked for 1 hour.
Therefore, please do not use multi-threaded downloaders such as Xunlei, IDM, etc. to avoid download tools from initiating multiple download requests in a short period of time, resulting in IP being blocked by mistake.
