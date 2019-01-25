from ffmpy import FFmpeg
from sys import argv

#self explanatory
script_name, input_filepath = argv
output_filepath = "out%d.png"

#simple script uses FFMPEG library to split the video to frame by frame, second by second
ff = FFmpeg(
        inputs={input_filepath:None},
        outputs={output_filepath:None}
    )

ff.cmd 
'ffmpeg -i input.mp4 -vf fps=1 out%d.png'
ff.run()