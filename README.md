# 🖨️ Brint - the future of print()
Brint offers debugging features, that are both efficient and visually appealing. 

This was higly inspired by the ```discord.py``` library, infact Brint was made just so i could have some prettier prints that fit well in with the ```discord.py``` library's printing.

**What we offer:**
* Time of print
* Nice color theme
* Status
* Highlight and main text


# 📖 Documentation
**General Information**

Every usage of the brint library will need to begin with ```Brint.``` like, ```Brint.success()```.
Please do not 

---
**Success Command**

```Success()``` is the status that will says that the code went smoothly.
```
Brint.success('Highlight', 'Message')
```
This will print:

![image](https://github.com/devjetz/Brint/assets/109991303/f86516eb-7be0-415f-aa9e-e9d488924d96)

Example:
```
Brint.success('Get', 'Successfully fetched id.')
```
---
**Error Command**
The ```Error()``` command shows us if there was an error, and makes it easier to see if you would encounter one.

It's recommended to only use ```Error()``` for debugging, for example, ```Brint.error('Highlight', 'Message')``` will print:

![image](https://github.com/devjetz/Brint/assets/109991303/f5a05b79-4075-4b9e-a2cc-8b6f3b2da984)

Now to use this in code you can do something like this:
```
if response.status_code == 200:
    Brint.success(name,'Message sent successfully.')
else:
    Brint.error(name,f'Failed to send message. Status Code: {response.status_code}.')
```
---
**Info Command**

The ```Info()``` is just like the name says - tells you info.

You would want to use ```info()``` for saying that you're doing something. The way to format ```info()``` is for example, ```Brint.info('Highlight', 'Message')```, this will print:

![image](https://github.com/devjetz/Brint/assets/109991303/1ab1d485-2c72-464c-8d82-c9f4136c87cd)

Now to use this in code you can do something like this:
```
Brint.info('POST', f'Requesting data from {url}.')
```
---
**Input Command**

The ```input()``` command is much more advanced to use than the other functions, as this requires atleast two lines. 

```Brint.input()``` is just like the other commands, but due to some limitations i can't directly add an input command. So first you would want to set up the ```input()``` command just like this: ```input('Highlight','Message').

Now this is the tricky part, add a new line and now you want to add ```input(Brint.inputt['t'])```, 

![image](https://github.com/devjetz/Brint/assets/109991303/ff6fbaf9-2abd-441f-a84c-23d89801bb2a)

If you got confused, heres how the code would look:
```
Brint.input('NUMBER','Please enter in valid option.')
chosenInput = int(input(Brint.inputt['t']))
```
