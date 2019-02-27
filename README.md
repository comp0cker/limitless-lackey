# Limitless Scraper for LackeyCCG

A Python script that scrapes [Limitless](http://limitlesstcg.com/) for both Japanese/English versions of the new sets (currently SM9a, SM9b, SM10). Special thanks to Rukan Shao for recommending this and David Hochmann for the hard work on the site + creating all of the English translations.

This tool was made to be optimized for many many sets in the future past SM9-SM10, unless Limitless changes the syntax of their database somehow. So, all runs of this program in a few years from now should still fetch in the latest unreleased sets!

Also, if you don't know how to use Python, don't worry, I manually uploaded the files as well!

## Usage

As a general note, Japanese cards are a lot more likely to be in the database (however as of right now all English proxies are available) due to Hochmann's limited time and energy. Also, the cards do not need to be English in order for them to work with Lackey.

### Recommended Method

It's not that bad - all you need is Python 3.x installed (download from [here](https://www.python.org/downloads/)). Either clone this repository or download as a .zip file to your computer by hitting the green button in the upper right. Run the script by opening the terminal on your device, nagivating to the directory you just installed it to (`cd C:/users/username/Dowloads/limitless-lackey` for Windows), and typing `python source.py`. This should run the script in the terminal, just follow the prompts and you'll have new cards in Lackey in no time.

The Get English Cards? prompt chooses whether or not to pull Japanese cards into Lackey, or Hochmann's English translations into Lackey. Keep in mind that if the translations aren't complete/uploaded, the script will fail to pull all of the images (since they won't all be up yet). The script can only do as much as Limitless can!

The directory scanner can actually install the cards right to your Lackey folder without you even doing anything! This only works on Windows since I don't know directories for Lackey on Mac, so if anyone could let me know who has a Mac that'd be stellar! For Mac users and people who don't have Lackey currently installed alike, you can opt to install to a subdirectory `./lackey` on the folder you're currently in.

If you install it to the local subdirectory, you'll have to manually copy and paste all contents in the folder into your LackeyCCG folder (for Windows it's `C:/Users/username/Documents/LackeyCCGWin/LackeyCCG/plugins/pokemon`, for Mac it's something like `xxx/LackeyCCGMac/LackeyCCG/plugins/pokemon`).

### Manual Method

Alternatively, you can download the files for Japanese cards [here](https://1drv.ms/u/s!ArcVtit_vwwUjK4PwBsSx7Tp0WxNtw) and English translations [here](https://1drv.ms/u/s!ArcVtit_vwwUjK4RUAaxk-dTOM5nbw) (updated 2/27/2019 for SM9a, SM9b, SM10, SMK and SM-P). Then, extract whichever zip you've downloaded into `C:/Users/username/Documents/LackeyCCGWin/LackeyCCG/plugins/pokemon` for Windows, for Mac it's something like `xxx/LackeyCCGMac/LackeyCCG/plugins/pokemon`).

#### Questions?

Please submit an issue if there's something wrong with this program, shoot me a DM, or email me at [jaredlgrimes@hotmail.com](mailto:jaredlgrimes@hotmail.com). 