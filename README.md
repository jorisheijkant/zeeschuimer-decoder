# Zeeschuimer decoder
This tool converts the Zeeschuimer data from the [Zeeschuimer scraping tool](https://github.com/digitalmethodsinitiative/zeeschuimer) to a readable CSV file. It's opinionated, as in that it only converts certain data in order to keep files small and managable. 

In the future, the script might not work as intended anymore, as the Zeeschuimer/social media data structures might change.

## Prerequisites
In order to run this script you need Python. If you do not have Python installed, download it [here](https://www.python.org/). 

## Installation
1. Download this repository to your pc, using either the download button at the top of this page or by cloning the repository using git.
2. Open a terminal and navigate to the folder where you downloaded the repository. See [here](https://openclassrooms.com/en/courses/4614926-learn-the-command-line-in-terminal/4634356-navigate-your-system) for instructions on how to navigate with your terminal. 
3. Add the script as a command line alias by running the following command: `alias zeeschuimer="python3 /path/to/zeeschuimer.py"`. Replace `/path/to/zeeschuimer.py` with the path to the `zeeschuimer.py` file. You can find this path by navigating to the folder where you downloaded the repository and running the command `readlink -f zeeschuimer.py`.
4. Use the script now whenever you are in a directory with a Zeeschuimer `.ndjson` file by running the command `zeeschuimer` in the following way:
```
zeeschuimer <filename> <type> (i.e. zeeschuimer data.ndjson tiktok)
```
Replace `<filename>` with the name of the `.ndjson` file and `<type>` with the type of data you want to convert. The following types are supported:
- tiktok (if no type is specified, this is the default type)
- twitter