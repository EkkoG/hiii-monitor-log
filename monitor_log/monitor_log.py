import json
import time

monitor_spider = None

def count_log(data_type, count, spider=None):
    obj = {
        'log_type': 'count',
        'time': time.time(),
        'data_type': data_type,
        'count': count
    }
    if spider:
        obj['spider'] = spider
    if monitor_spider:
        obj['spider'] = monitor_spider

    assert obj['spider'] is not None

    print('爬虫监控统计信息：{}'.format(json.dumps(obj)))

if __name__ == "__main__":
    pass