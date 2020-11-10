import sys
import os
from os import path
import logging
import time
import wget
# pip install searchtweets
import twitter
# pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory

######################################################################
# Constants
"""
Change ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY and CONSUMER_SECRET
to your own. 
"""
ACCESS_TOKEN='70399566-GcJfQqr3VLOuwRuG8yPSFxr44znKJieNl2ASasUUr'
ACCESS_SECRET='K7LlXPCaV2rsbJdJwb7gDw0BUfx8SUn2NluNsGX6G36SP'
CONSUMER_KEY='osUlOXxtORRiLQd2iNtQgPifH'
CONSUMER_SECRET='TULYCcd9b5L678W6OBfXEy7cM3ErtJL6XxQDzMQKDOzOA6ITrt'

# twitter URL parameters
TWITTER_MULTI_SEARCH_BOOLEAN_OPERATOR='%20OR%20'
TWITTER_MEDIA_FILTER='%20filter%3Amedia'
TWITTER_SAFE_SEARCH_FILTER='%20filter%3Asafe'
TWITTER_RETWEETS_PARAMETER='%20-filter%3Aretweets'
TWITTER_LIVE_RESULTS_URL_PARAMETER='&f=live'
TWITTER_RESULT_TYPE_PARAMETER='&result_type=recent'
TWITTER_COUNT_PARAMETER='&count=100'

######################################################################
# Global Variables

# list of search terms
search_terms=[]

###################################


# builds the query using the search terms passed in
def build_search_query():
    complete_search_query='q='

    # get the number of search terms
    loop_count=len(search_terms)

    # loop through the search terms and create the complete search query
    for x in range(loop_count):
        complete_search_query=complete_search_query+search_terms[x]

        # As long as this is not the final loop, add the boolean operator to return results for all search terms
        if x != (loop_count-1):
            complete_search_query=complete_search_query+TWITTER_MULTI_SEARCH_BOOLEAN_OPERATOR

    # add the media filter
    complete_search_query=complete_search_query+TWITTER_MEDIA_FILTER

    # add the exclude retweets parameter to the URL
    complete_search_query=complete_search_query+TWITTER_RETWEETS_PARAMETER

    # add the safe search filter to the URL
    complete_search_query=complete_search_query+TWITTER_SAFE_SEARCH_FILTER

    # add the live results parameter to the URL
    complete_search_query=complete_search_query+TWITTER_LIVE_RESULTS_URL_PARAMETER

    # add the result type parameter to the URL
    complete_search_query=complete_search_query+TWITTER_RESULT_TYPE_PARAMETER

    # add the count parameter
    complete_search_query=complete_search_query+TWITTER_COUNT_PARAMETER

    # replace the # sign with the appropriate character string
    complete_search_query=complete_search_query.replace('#','%23')

    # return the final query string
    return complete_search_query

def scheduler_error_handler(event):
    if hasattr(event,'exception'):
        if event.exception != None:
            print('The job FAILED to execute. Reason: '+str(event.exception))

def folder_picker():
    # open a directory picker
    location=askdirectory()

    # set the value of the output_directory text box to be the full directory selected above (saved as location)
    output_directory.insert(0,location)

def execute_search():
    # get search terms
    search_input=window.children['search_input'].get()
    global search_terms
    search_terms=search_input.split(',')

    # execute search and start downloading media
    t=twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_SECRET)

    search_query=build_search_query()

    results=t.GetSearch(raw_query=search_query)

    return results

def download():
    # execute the search
    tweets=execute_search()

    # check to make sure results came back (str type would indicate an error message)
    if type(tweets) != str:
        # download the media URLs to the selected folder
        for tweet in tweets:
            if tweet.media != None:
                for x in range(len(tweet.media)):
                    # get a video from the tweet (if available)
                    if tweet.media[x].video_info != None:
                        for y in range(len(tweet.media[x].video_info.get('variants'))):
                            video_url=tweet.media[x].video_info.get('variants')[y].get('url')
                            file_name=str(tweet.user.screen_name)+'--'+str(tweet.id)+'--'+str(x)
                            output_directory_full=output_directory.get()+'/'+file_name+'_'+str(y)+'.mp4'
                            # if the file does NOT already exist
                            if (not path.exists(output_directory_full)):
                                # then download it
                                try:
                                    wget.download(video_url,output_directory_full)
                                except Exception as e:
                                    error_lbl.config(fg="red")
                                    error_text.set('ERROR: '+str(e))
                                    window.update()

                    # get a photo from the tweet (if available)
                    if tweet.media[x].media_url_https != None:
                        photo_url=tweet.media[x].media_url_https
                        file_name=str(tweet.user.screen_name)+'--'+str(tweet.id)+'--'+str(x)
                        output_directory_full=output_directory.get()+'/'+file_name+'.png'
                        # if the file does NOT already exist
                        if (not path.exists(output_directory_full)):
                            # then download it
                            try:
                                wget.download(photo_url,output_directory_full)
                            except Exception as e:
                                error_lbl.config(fg="red")
                                error_text.set('ERROR: '+str(e))
                                window.update()

def get_media():
    # disable the download button since downloading has already started
    download_button.config(state=DISABLED)

    # Get the interval value in seconds from the textbox
    seconds_int=int(interval_input.get())

    # Ensure that the input was an integer value
    if type(seconds_int) != int:
        interval_input.insert(0,'NOT AN INTEGER VALUE!')

    # execute the download action on a schedule as specified by seconds_int
    global scheduler
    scheduler=BackgroundScheduler()
    scheduler.add_job(download,'interval',seconds=seconds_int,coalesce=TRUE)
    scheduler.add_listener(scheduler_error_handler)
    scheduler.start()

    # immediately execute the download action one time
    download()

    error_lbl.config(fg="green")
    error_text.set('First download successful! Specified schedule started...')
    window.update()

def generate_user_interface():
    # continue flag for continuing to download (used in both stop and download)
    global continue_flag
    continue_flag=True

    # Creates a UI to allow you to enter search terms
    global window
    window=Tk()

    window.title("Twitter Media Downloader")

    # Frame for search terms
    search_terms_frame=Frame(window)
    search_terms_frame.pack(side=TOP,pady=10)

    # Enter search terms
    search_lbl=Label(window,text="Comma-separated search terms:        ",font=("Arial Bold",13),anchor="w")
    search_lbl.pack(in_=search_terms_frame,side=LEFT,padx=10)

    search_input=Entry(window,name='search_input',width=50)
    search_input.pack(in_=search_terms_frame,side=RIGHT,padx=10)
    search_input.focus()

    # Frame for interval input
    interval_input_frame=Frame(window)
    interval_input_frame.pack(side=TOP,pady=10)

    # Interval selector
    interval_lbl=Label(window,text="Interval (in secs) between searches:   ",font=("Arial Bold",13),anchor="w")
    interval_lbl.pack(in_=interval_input_frame,side=LEFT,padx=10)

    global interval_input
    interval_input=Entry(window,name='interval_input',width=50)
    interval_input.pack(in_=interval_input_frame,side=RIGHT,padx=10)

    # Frame for selecting download folder
    downloads_folder_frame=Frame(window)
    downloads_folder_frame.pack(side=TOP)

    output_lbl=Label(window,text="Output directory:                                    ",font=("Arial Bold",13),
                     anchor="w")
    output_lbl.pack(in_=downloads_folder_frame,side=LEFT)

    global output_directory
    output_directory=Entry(window,name='output_directory',width=30)
    output_directory.pack(in_=downloads_folder_frame,side=RIGHT,padx=5)

    Button(window,text='Select Folder',width=15,command=folder_picker).pack(in_=downloads_folder_frame,side=RIGHT,
                                                                            padx=0,pady=20)

    # Frame for buttons
    buttons_frame=Frame(window)
    buttons_frame.pack(side=BOTTOM,fill=X,expand=FALSE)

    # Quit button
    global quit_button
    quit_button=Button(window,text='Quit',width=10,command=quit)
    quit_button.pack(in_=buttons_frame,side=RIGHT,padx=10,pady=20)

    # Stop downloading
    global stop_button
    stop_button=Button(window,text='Stop',width=10,command=stop)
    stop_button.pack(in_=buttons_frame,side=RIGHT,padx=10,pady=20)

    # Download
    global download_button
    download_button=Button(window,text='Download',width=10,command=get_media)
    download_button.pack(in_=buttons_frame,side=RIGHT,padx=10,pady=20)

    # Frame for error handling
    error_frame=Frame(window)
    error_frame.pack(side=TOP)

    global error_text
    error_text=StringVar()

    global error_lbl
    error_lbl=Label(window,textvariable=error_text,text="",font=("Arial",10),fg="red",anchor="w")
    error_lbl.pack(in_=error_frame,side=LEFT)

def stop():
    # continue flag for the timer to continue
    global continue_flag
    continue_flag=False

    # stop the schedule
    scheduler.shutdown()

    # restore the download button so that it can be clicked
    download_button.config(state=NORMAL)

    # Update the window status
    error_lbl.config(fg="red")
    error_text.set('NOTICE: Specified schedule Stopped!')
    window.update()

def quit():
    window.destroy()

##############################################################################

def main():
    generate_user_interface()

if __name__ == '__main__':
    # setup logging for the scheduler
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    # execute the main method
    main()

    # keep the UI active
    window.mainloop()