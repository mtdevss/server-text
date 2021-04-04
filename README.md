# Server Text
A simple flask service that allows you to run commands on the server/computer over sms.

**Watch Demo Video [Here](https://vimeo.com/532760635)**

## Installation

You can view installation demo [here](https://asciinema.org/a/404971)
_Note: I use python version 3.9 but 3.6 is being widely used_

- Before you clone the repo make sure you have `python3` and `pipenv` installed on your machine.You can always verify `python` by running `python3 --version` on commandline and if you don't have `pipenv` installed you can refer to the [docs](https://pipenv-fork.readthedocs.io/en/latest/install.html)

- Once you have `python` and `pipenv` installed now you can clone the repo 
`git clone https://github.com/mtdevss/server-text.git`.

- Now `cd server-text/` and run `pipenv shell` to activate the virtual environment and `pipenv install` to install the dependencies.

- Once you have installed the dependencies before you run the script make sure to populate the script with your `email`,`pas` ,`number` from which you will be sending texts from, and `imap server` of your email provider

#### Example

```python
mail = 'your_email@domain.com'# Where you will be receiving texts sent from number
pas = '<email_pass>'
number = '+1[number]@SMS_GATEWAY'# from which you will be sending
imap_server = '<your_email_provider_imap>'
```
- Now you can start the server by following command `python3 script.py`

- Before you view the output makesure to send a command like `ls -la` from your phone to the email and open `localhost:5000` on your browser to see the output of your command.

### SMS GATEWAYS

You can find your sms gateway [here](https://www.freecarrierlookup.com/)

- AT&T: [number]@txt.att.net
- Sprint: [number]@messaging.sprintpcs.com or [number]@pm.sprint.com
- T-Mobile: [number]@tmomail.net
- Verizon: [number]@vtext.com
- Boost Mobile: [number]@myboostmobile.com
- Cricket: [number]@sms.mycricket.com
- Metro PCS: [number]@mymetropcs.com
- Tracfone: [number]@mmst5.tracfone.com
- U.S. Cellular: [number]@email.uscc.net
- Virgin Mobile: [number]@vmobl.com
- Google Fi: [number]@msg.fi.google.com
- Ting: [number]@message.ting.com
- Telus Mobile: [number]@msg.telus.com
- Viaero: [number]@viaerosms.com

**NOTE**: Make sure to add **+1** before the number.


## Contribution
- This is available under MIT license and contributions are welcomed.
- Currently its `version 1.0` we do plan to improve this further.
- If you would like to contribute to this feel free to fork and create a PR and we would be happy to merge your contribution.


## Note
- This script was tested using `tmobile` and `googlefi` network.
- If you are using gmail make sure you have `less secure apps` turned off
- There's a time delay in the request since it takes around 10 seconds to receive message from phone to email
