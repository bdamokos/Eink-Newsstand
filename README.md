As someone who has never coded before this will probably seem like a mess to most people,
but I have tried my best to lable every thing that must been done before you can get this working.

This code uses RSS feeds to pull news articles, it gets the rss feed, the name of the news source, and the image logo by pulling it from a csv file named rss_list_final.
If you want to add remove or change the list of sources this csv file will be where it is done

**(Until you do this the code will NOT work)**

Next, a few file paths must be set:
1. Line 14 font_pathH (font of headline)
2. Line 15 font_pathB (font of byline)
3. Line 26 file_path (file path of rss_list_final.csv, aka your list of new sources)
4. Line 23 max_headline_num (used to say how many headlines you want from each source to be pulled)

The Cycle:
  The order of headliens is made by a matrix where it will show the first article from every news source in the csv until all are shown. Then it will move on to the second article and so on

There are also 5 GPIO buttons that control the screen
  1. Pause (The screen cycles on a 30 second timer before movign to the next story. this will pause that timer)
  2. Next (This will move you to the next source and article on the list)
  3. Back (Shows previous source and article on list)
  4. Link (Pauses the timer and displays a qr code with a link to the story on screen)
  5. Refresh (Briefly pauses the timer while the e ink display refreshes then unpauses the timer)

Finally for people who really care, within the waveshare folder there are 2 custom built addons
  1. image_converter.py Used to turn any normal image file into one usbale by the eink display
  2. text_wrapper.py Used to figure out where to move text to a new line so it doesnt go off the screen
