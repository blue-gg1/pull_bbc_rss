:start
curl https://podcast.voice.api.bbci.co.uk/rss/audio/p002vsmz?api_key=Wbek5zSqxz0Hk1blo5IBqbd9SCWIfNbT --output content.rss
grep 'mp3' content.rss

grep -o 'https://open.*[mp3]' content.rss | cut -b1-129>url.txt
wget -i url.txt

pause
stat w* | xargs| cut -b270-288>namenew.txt
set /p newname=<namenew.txt

mv w* "%n

goto start
