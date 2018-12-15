if '__name__' == '__main__':

    import urllib.request
    from datetime import datetime
    from apscheduler.schedulers.blocking import BlockingScheduler

    current_time = current_time = str(datetime.now()).split('.')[0]
    hour = int(current_time.split(' ')[1].split(':')[0])
    current_time = current_time.replace(' ', '_')

    sched = BlockingScheduler()

    @sched.scheduled_job('interval', minutes=30)
    def get_cowells_image():
        print('This job is run every thirty minutes.')

        # Only scrape images during daylight hours
        if 7 < hour < 18:

            resource = urllib.request.urlopen("https://argusdata.s3.amazonaws.com/dreaminn/latest/c2_snap.jpg")
            output = open("{}.jpg".format(current_time),"wb")
            output.write(resource.read())
            output.close()

    sched.start()
