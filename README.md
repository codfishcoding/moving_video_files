# moving_video_files
This is a script to move my video files from the default save location to my external hard drive.
The script is very simple, but I did encounter a bug. The subprocess Popen did not allow me to copy video files (tested on .flv files). It did work though on my first test of just moving .txt files around and was much faster. So, depending on the media you are moving one process may work better than the other.
