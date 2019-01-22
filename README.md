```
┌┬┐┬ ┬┌─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐┌─┐┌─┐┬─┐
 │ ├─┤├┤ ├┤  │ ├┤ │ │┌─┘┌─┘├┤ ├┬┘
 ┴ ┴ ┴└─┘└   ┴ └  └─┘└─┘└─┘└─┘┴└─
```
## Introduction:
TheftFuzzer is a tool that fuzzes Cross-Origin Resource Sharing implementations for common misconfigurations.

## Usage:
`python theftfuzzer.py -d 'http://example.com/api/data'`

#### Help:
`python theftfuzzer.py -h`


```
~$ python theftfuzzer.py -h                               
usage: theftfuzzer.py [-h] -d DOMAIN [-c COOKIE]

Cross Origin Resource Sharing Fuzzer by Corben Leo

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        URL / Target to fuzz
  -c COOKIE, --cookie COOKIE
                        File containing cookie to send in fuzzing requests
```


<a href="http://buymeacoff.ee/cdl" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
