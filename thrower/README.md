# Exploit Thrower

## How CTF Works

In my class CTF, we were put on a box from which we had to automatically exploit several other teams' boxes. The workflow every tick was something like this:

1. Query a central server for service information. Let's say the challenge I'm exploiting is called "backup". I would query the service about team information related to "backup".

2. The central server returns the follow tuple for each team: <service IP, service PORT, flag ID>.

3. Now for each team, I use the IP and PORT to know where the vulnerable service is running and I run my exploit like normal. Once I've exploited the box, I notice that each service actually has a directory of hundreds of flag files. Only one of the files is the "real" flag every tick, and which flag file is the "real" one changes each tick. This is where the flag ID comes in - it gives you the name of the file that is the current real flag for this tick. So I would `cat` the flag ID file, and send that text back to me.

4. Now, I should have a list of several flags from each team that I exploited for this service. All I need to do is use the Python API to submit them all at once, and the API will give me confirmation about the flag submissions' success.

All of the above code can be seen in `submit.py`.

## How this Folder is Structured

Let's say you want to submit an exploit.

- `<servicename>.py` is your pwntools exploit script. It should go in the `exploits` folder.
- `submit.py` is your auto-submission + exploit runner script. It runs your exploit script and expects a flag in stdout.
- `exploit_thrower.py` is your overall "main" function, which just waits every tick to scan the `exploits` directory for `<servicename>.py` scripts. It runs `submit.py` for each of those scripts, which in turn runs your exploits and submits the flags.

### Example

I have an example script for a service I pwned during my class CTF, "backup".

- `run_real_backup.py` contains my exploit. It takes args the IP, PORT, and flag ID.
- `submit_real_backup.py` (not here) gets all the teams' flag IDs, hosts, and ports for backup. Then it runs the exploit on each one, prints the flags, and submits. It takes as args our Team Interface, our Team flag ID, and the service name we're trying to exploit.
- `exploit_thrower.py`, which just keeps running.

## Other Stuff

The design isn't that great because I did most of this stuff on the fly during my class CTF. Feel free to restructure. Also, we may need to update our API functions depending on the code given on the iCTF website.

Lastly, I had the idea to submit "fake" payloads every tick, mixed with our real ones. This way we could throw off teams that are trying to RE our payloads. From my experience though, it wasn't worth the time and effort to come up with fake payloads. Especially as a two person team, I think we're better focused on just developing our own exploits and popping as many boxes as we can. But this is why you see things like `submit_fake_template.py` in this folder.
