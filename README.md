As someone who has never coded before this will probably seem like a mess to most people,
but I have tried my best to lable every thing that must been done before you can get this working.

This code uses RSS feeds to pull news articles, it gets the rss feed, the name of the news source, and the image logo by pulling it from a csv file named rss_list_final.
If you want to add remove or change the list of sources this csv file will be where it is done

(Until you do this the code will NOT work)
Next, a few file paths must be set:
  Line 14 font_pathH (font of headline)
  Line 15 font_pathB (font of byline)
  Line 26 file_path (file path of rss_list_final.csv, aka your list of new sources)

Finally for people who really care, within the waveshare
