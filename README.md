# About the project
This is a Laboratory of the Cryptography course at Universidad Diego portales that has the objective of learn about the security in different websites in different locations of the work. Here I audited the Chilean website [Solotodo](https://www.solotodo.cl/) and the Spanish website [Pccomponentes](https://www.pccomponentes.com/).

# Selenium Automation
At first I tried to use Selenium for the signin and signup automation but I realized it is way too slow for those tasks.  
## Prerequisites
These are the prerequisites that you need to have installed in order of the Selenium automation to work.
- Python 3
- Selenium
- Google Chrome browser
- Chromedriver with the same version as Google Chrome
### Chromedriver
[Here is](https://chromedriver.chromium.org/getting-started) the Chromedriver's getting-started page where you can download the version that suits you.

# Bash Automation
The second approach was to make bash scripts for the signin, signup, password recovery and password change at the websites. It is a faster approach and a clever one.
## Prerequisites
These are the prerequisites that you need to have installed in order of the Bash automation to work. At the moment these automation only works in UNIX-like OS.
- [jq](https://stackoverflow.com/questions/33184780/install-jq-json-processor-on-ubuntu-10-04)
- [htmlq](https://lindevs.com/install-htmlq-on-ubuntu/)
## Considerations
One little consideration is that if the scripts doesn't run, you should change permissions applying
```
chmod 777 'file.sh'
```
to the files.

