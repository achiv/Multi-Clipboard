#! python3
# mclip.py - A multi clipboard program

TEXT = {'sick': """Hi Team, I will not be able to come to office today. I am not feeling well and will be taking sick leave for the day.
Please reach out to me on my personal phone if anything urgent.
Thank you.""",
    'busy': """Sorry, can we do this later this week or next week? 
I am currently preoccupied with some priority tasks that are needed to be completed this week."""}

import sys, pyperclip
if len(sys.argv) > 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1];    # first command line is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
