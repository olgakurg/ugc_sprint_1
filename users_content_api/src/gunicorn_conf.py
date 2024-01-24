from multiprocessing import cpu_count

bind = 'unix:/home/gunicorn.sock'

workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'


loglevel = 'debug'
accesslog = '/home/access_log'
errorlog = '/home/error_log'