# File Renaming Utility Tool
### I created this console app for my brother [Alaa Amari](https://www.linkedin.com/in/alaa-amari/) as per his request since he is a video editor and found himself wasting precious time on renaming his files. so I AUTOMATED the process

## Commands
1. Beautify mp4 file name:
This asks for a folder path and then renames all mp4 files using his criterias:
    - Transform all letter to lower case
    - Remove consecutive whitespaces (keep one)
    - Replace all the left whitespaces with a hyphen -
    - Transfrom all é and è to e and à to a
Example: 'Great  VIDEO  àààà.mp4' -> becomes 'great-video-aaaa.mp4'
2. Add date to file names
This asks for a folder path and then adds the current date to all mp4 files.
Date format: _yyyymmdd
Example: 'great-video-aaaa.mp4' -> becomes 'great-video-aaaa_20210814.mp4' (I'm writing this in 14/08/201)
3. Remove date from file names (reverse [2])
In case he used the second command he can reverse it's effect. This asks for a folder path and then deletes the date from all file names (Simply deletes the last 9 characters)
Example: 'great-video-aaaa_20210814.mp4' -> becomes 'great-video-aaaa.mp4' (I'm writing this in 14/08/201)