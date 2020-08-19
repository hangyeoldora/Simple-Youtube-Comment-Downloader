# Simple-Youtube-Comment-Crawler
You can extract YouTube comments using Selenium. (username, comment) and It can be saved as txt,xlsx file. (default:xlsx) <br>
Just enter your YouTube video ID and you can save the comment in xlsx file.<br>
The xlsx file is saved with a name that includes the current date and time.

## Requirements
+ Python 3.7+
+ A YouTube video ID / ( e.g. 'https://www.youtube.com/watch?v='+ID

## Module
+ You can install what you need to run the program with the freeze module.
```
pip freeze > requirements.txt
```

## Usage
You can run py files on cmd or editor.
```
python youtube_comment.py
```
<br>

Also, you can create and run a single exe file. 
```
c:~~~~\youtube-comment-crawler> pyinstaller --onefile -F --add-binary "chromedriver.exe";"." youtube_comment.py
```

When run the command, an exe file will be created in the dist folder.
just execute it!
