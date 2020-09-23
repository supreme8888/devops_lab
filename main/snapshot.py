import psutil
import argparse
import datetime
import time
# import os


def main():

    class Message:
        def __init__(self, text):
            self.text = text

        def __str__(self):
            return "Message from App: %s" % self.text

    message = Message("my_first_class")
    print(message)

    parser = argparse.ArgumentParser(description='parser of arguments')
    parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
    parser.add_argument("-t", help="Output file type", default="txt")
    args = parser.parse_args()

    if args.t == "json":
        while True:
            time.sleep(args.i)
            dt = str(datetime.datetime.today())
            disk = str(psutil.disk_usage('/').percent)
            cpu = str(psutil.cpu_percent(interval=1, percpu=False))
            cpuf = str(psutil.cpu_freq().current)
            joinedlist = [dt, cpu, disk, cpuf]
            print(joinedlist)
            f = open("monitor.json", "a")
            f.write("""{
            "snapshot": {
            "timestamp": "%s",
            "CPU usage": "%s"
            "disk": "%s"
            "CPU freq": "%s"
                        }
            }
            """ % (dt, cpu, disk, cpuf))
            f.close()
    else:
        while True:
            time.sleep(args.i)
            dt = str(datetime.datetime.today())
            disk = str(psutil.disk_usage('/').percent)
            cpu = str(psutil.cpu_percent(interval=1, percpu=False))
            cpuf = str(psutil.cpu_freq().current)
            joinedlist = [dt, cpu, disk, cpuf]
            print(joinedlist)
            f = open("monitor.txt", "a")
            f.write("%s CPU usage %s  Disk usage %s CPU freq %s\n" % (dt, cpu, disk, cpuf))
            f.close()


main()
