#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,argparse,string,sys,itertools,os
from http.cookies import SimpleCookie
from urllib.parse import urlsplit
from urllib.parse import unquote

parser = argparse.ArgumentParser(description='Cross Origin Resource Sharing Fuzzer by Corben Leo')
parser.add_argument('-d','--domain',dest='domain',required=True,help="URL / Target to fuzz")
parser.add_argument('-c', '--cookie',dest='cookie',required=False,help="File containing cookie to send in fuzzing requests")
args = parser.parse_args()

## ascii :)
top = '''\033[F\033[K\033[1;35m
┌┬┐┬ ┬┌─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐┌─┐┌─┐┬─┐
 │ ├─┤├┤ ├┤  │ ├┤ │ │┌─┘┌─┘├┤ ├┬┘
 ┴ ┴ ┴└─┘└   ┴ └  └─┘└─┘└─┘└─┘┴└─
 \033[1;33mby Corben Leo - https://hacking.us.com
\033[1;0m\n'''
print(top)
## variables
target = args.domain
base_url = "{0.scheme}://{0.netloc}".format(urlsplit(target))
bypass = ['','-','"','{','}','+','_','^','%60','!','~','`',';','|','&',"'",'(',')','*',',','$','=','+',"%0b"]
domains = ["https://localhost","http://localhost",base_url]
permutations = [base_url+"example.com",base_url+"example.com"]

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

if args.cookie is not None:
    if os.path.isfile(args.cookie):
        with open(args.cookie) as file:
            cookie = file.read().replace('\n', '')
            session_cookie = dict(x.split('=') for x in cookie.split(';'))
        def fuzz(origin):
            return requests.get(target,headers={'Origin': origin,'User-Agent':ua},cookies=session_cookie, allow_redirects=True)
    else:
        print('\033[1;31m[!] Error: Cookie file does not exist\033[1;0m')
        os._exit(0)
else:
    def fuzz(origin):
        return requests.get(target,headers={'Origin': origin,'User-Agent':ua}, allow_redirects=True)


for r in itertools.product(domains,bypass):
    attempt = r[0]+r[1]+".example.com"
    permutations.append(attempt)
permutations.append('null')

for perm in permutations:
    sent = "Sending -> Origin: "+ perm
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print(sent)
    try:
        result = fuzz(perm).headers['access-control-allow-origin']
        if result == perm:
            print('\033[F\033[K\033[1;31m[-] Response: Access-Control-Allow-Origin: '+perm+'\033[1;0m\n\n\n')
        else:
            sys.stdout.write("\033[K")
    except KeyError:
        sys.stdout.write("\033[K")
    except requests.exceptions.RequestException:
        print("\033[1;31m[!] Aborted: Connection Error!\033[1;0m")
        os._exit(0)
    except KeyboardInterrupt:
        os._exit(0)
sys.stdout.write("\033[F\033[K")
print('\n...we done\n\tpeaceee!\n\t\tᕕ( ᐛ )ᕗ ')
