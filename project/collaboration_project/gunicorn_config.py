from multiprocessing import cpu_count


def max_workers():
    return cpu_count() + 1


bind = '0.0.0.0:8001'
max_requests = 10000
worker_class = 'socketio.sgunicorn.GeventSocketIOWorker'
workers = max_workers()


def def_post_fork(server, worker):
    from psycogreen.gevent import psyco_gevent
    psyco_gevent.make_psycopg_green()
