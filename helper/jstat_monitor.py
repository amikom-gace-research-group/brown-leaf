import os
import subprocess

class monitor:
    def jstat_start(self, passwd="CloudLab12#$%"):
        subprocess.run(['sudo', '-S', 'tegrastats', '--start', '--logfile', 'tegrastats.txt'],
                       input=passwd,
                       universal_newlines=True)

    def gpu_read(self):
        
        pass
    
    def jstat_stop(self, passwd="CloudLab12#$%"):
        pass