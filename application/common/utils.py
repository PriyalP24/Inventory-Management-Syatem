from flask import *
import os
import datetime
import pytz

path = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(path, 'uploaded_files')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def output_html(data,code,headers=None):
    resp = Response(data,mimetype='text/html',headers=headers)
    resp.status_code=code
    return resp

def allowed_file(filename):
    print("filename : ",filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def datetime1(time):
    dt = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M')


    now_aware = pytz.utc.localize(dt, is_dst=None)
    now_cst = now_aware.astimezone(pytz.timezone('CST6CDT'))
    return now_cst


def time(time1,ex_time):
    old_timezone = pytz.timezone(time1)
    my_timestamp = datetime.datetime.now(old_timezone)
    new_timezone = pytz.timezone("CST6CDT")
    new_timezone = my_timestamp.astimezone(new_timezone)


    local_tz = pytz.timezone('CST6CDT')
    ex_time = local_tz.localize(ex_time, is_dst=None)

    if new_timezone > ex_time:
        return True
    else:
        return False





def get_logger():
    import logging
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("application/log/logfile.log")
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger

def validation(file,form):
    filename = file["photo"]
    if allowed_file(filename.filename):
        return True
    return False

def read_id():
    file=open("app/common/data.txt","r")
    return file.read()

def write_id(id):
    file = open("app/common/data.txt", "w")
    file.write(str(id))

def output_html(data,code,headers=None):
    from flask import Response
    resp=Response(data,mimetype='text/html',headers=headers)
    resp.status_code=code
    return resp