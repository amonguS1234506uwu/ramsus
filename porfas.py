import sys, subprocess

if len(sys,argv)<>2:
    print("psweep.py 10.0.0")
else:
    cmdping = "ping -c1 "+sys.argv[1]
    for x in range (2,255):
        p = subprocess.Popen(cmdping+str(x), shell=True, stderr=subprocess.PIPE)
        while True:
            out = p.stderr.read(1)
            if out == '' and p.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
