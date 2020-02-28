import time
import schedule


def f():
    print("doing it")


def main():

    job = schedule.every(10).seconds.do(f)
    print(job)

    while True:
        schedule.run_pending()
        time.sleep(1)



main()
