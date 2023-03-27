from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, DAILY, MO, WE


def get_lastday_by_datetime():
    # 下个月的最后一天 = 下下个月的前一天
    now_time = datetime.now()
    # 获取下下个月第一天的日期对象
    if now_time.month in [11, 12]:
        first_day_of_after_two_month = datetime(now_time.year, now_time.month+2-12, 1)
    else:
        first_day_of_after_two_month = datetime(now_time.year, now_time.month+2, 1)
    # 获取下个月最后一天的日期对象
    last_day_of_next_month = first_day_of_after_two_month - timedelta(days=1)
    # 输出结果
    print("下个月的最后一天: %s" % last_day_of_next_month.date())


def get_lastday_by_relativedelta():
    now_time = datetime.now()
    last_day_of_next_month = now_time + relativedelta(months=2, day=1, days=-1)
    print("下个月的最后一天: %s" % last_day_of_next_month.date())


# 获取2012年1月1日到2012年2月1日之间的周一和周三
def get_mon_and_wed_by_rrule():
    # 生成rrule对象
    rrule_obj = rrule(DAILY, byweekday=(MO, WE), dtstart=datetime(2012, 1, 1), until=datetime(2012, 2, 1))
    print("2012年1月1日到2012年2月1日之间的周一和周三:")
    for dt in rrule_obj:
        print(dt.date())


get_lastday_by_datetime()
get_lastday_by_relativedelta()
get_mon_and_wed_by_rrule()
