------------------------------------------------------------------------------
*********************** CRUx INDUCTION TASK **********************************
------------------------------------------------------------------------------


			   AUDIO_PLAYER

This is a basic audio player programmed using python and pygame module. 
To run the program you should have the following installed in your system-
1. Python 2.7.12
2. Pygame (setup in the repo)
3. mutagen (also in the repo)

This player displays the metadata of the music file if available, otherwise it displays 'N/A' in the screen.
The '+' Button on the pygame window is for changing the directory during the play of the music.

This file currently shows the metadata of three types of files ('.mo3','.ogg','.flac'). It can also play other formats but currently it is supported for the above three formats.

The player may show error if -
1. The extension of the music file is unsupported. (currently ('ogg','mp3','flac'))
2. Or the file name may contain character(s) other than alphabets.To rectify this please modify the name of the file.
