### 介绍

本项目主要功能为监控爬虫打日志所用

### 安装

```
pipenv install -e git+https://github.com/cielpy/hiii-monitor-log.git@master#egg=hiii-monitor-log
```

### 使用

```python
from monitor_log import monitor_log

monitor_log.monitor_spider = '爬虫名'

monitor_log.count_log('数据类型', 1)
```
