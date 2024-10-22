## Profile montage creator

I took photos from 4 different phones over the course of 7 yeards and I needed to structure and format for a video compilation I use ffmpeg to actaully generate it using a command like this

ffmpeg -framerate 10 -pattern_type glob -i '/home/david/Projects/Profile-Montage/output-final/*.jpg' -vf scale=512:512 -r 30 -vcodec libx264 -pix_fmt yuv420p output_512x512_video.mp4

I was going to use a video editor but then I saw I could do it with code and said why not try and it and I finished it in one night. I think there was over 1250 images check out the end result here: 
https://www.youtube.com/watch?v=leP5AOvfzk0&feature=youtu.be
