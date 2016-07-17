import sys
sys.path.append("packages")
import iron_mq
from iron_worker import *
from video_download import *
from image_extract import *
from upload_s3 import *

payload = IronWorker.payload()
print 'payload: %s' % payload 
url = payload['url']

print "url:", url

url_list = ['www.youtube.com/embed/ag0hsUf9V7Q', 'http://www.youtube.com/embed/PGc9n6BiWXA', 'http://www.youtube.com/embed/DrZhmr_0Wpo', 'http://www.youtube.com/embed/ByLJstEo0fo', 'www.youtube.com/embed\
/1_hvKZlRnM8', 'http://www.youtube.com/embed/1hR4MVL3zCA', 'www.youtube.com/embed/Ka7wBGFSuSE', 'http://www.youtube.com/embed/KNG4zeq9Srw', 'www.youtube.com/embed/LXXQLa-5n5w', 'https://www.youtube.com/e\
mbed/0owbEh54SjY', 'www.youtube.com/embed/RaXbRWMdAB0', 'www.youtube.com/embed/OSAOsm1u-OE', 'www.youtube.com/embed/p1JPKLa-Ofc', 'https://www.youtube.com/embed/LrCHz1gwzTo', 'http://www.youtube.com/embe\
d/LgD_-dRZPgs', 'http://www.youtube.com/embed/xONCQCD3-zU', 'www.youtube.com/embed/56qgO0C82vY', 'www.youtube.com/embed/pZ12_E5R3qc', 'http://www.youtube.com/embed/XWCwc1_sYMY', 'http://www.youtube.com/e\
mbed/5xgjtm4_M20', 'www.youtube.com/embed/x4pPNxUzGvc', 'http://www.youtube.com/embed/YhxjNYvJbgM', 'http://www.youtube.com/embed/eFTLKWw542g', 'http://www.youtube.com/embed/-e_3Cg9GZFU', 'https://www.yo\
utube.com/embed/9NwZdxiLvGo', 'www.youtube.com/embed/FDKuJ3UWmDc', 'http://www.youtube.com/embed/nnReaaJwloI', 'http://www.youtube.com/embed/OJBfv9CHlcw', 'https://www.youtube.com/embed/qv9YI8Oqs30', 'ww\
w.youtube.com/embed/IDvu1ehPq0g', 'www.youtube.com/embed/rWFwqTwZxgc', 'http://www.youtube.com/embed/C3ogFWISPuw', 'www.youtube.com/embed/ulHB2mNlovg', 'http://www.youtube.com/embed/CUOlc_j4rMA', 'http:/\
/www.youtube.com/embed/YJVmu6yttiw', 'https://www.youtube.com/embed/0ljS_XWAA7E', 'http://www.youtube.com/embed/_t2TzJOyops', 'www.youtube.com/embed/rmfmdKOLzVI', 'www.youtube.com/embed/jcF5HtGvX5I', 'ww\
w.youtube.com/embed/K4r4lysSgLE', 'http://www.youtube.com/embed/dcnd55tLCv8', 'http://www.youtube.com/embed/6yYchgX1fMw', 'https://www.youtube.com/embed/c6rP-YP4c5I', 'http://www.youtube.com/embed/BGpzGu\
9Yp6Y', 'www.youtube.com/embed/QwZwnZ4dKpA', 'http://www.youtube.com/embed/FHO6a2H-pqY', 'http://www.youtube.com/embed/i41qWJ6QjPI', 'http://www.youtube.com/embed/hSq4B_zHqPM', 'www.youtube.com/embed/8eJ\
DTcDUQxQ', 'https://www.youtube.com/embed/nntGTK2Fhb0', 'http://www.youtube.com/embed/T0lcOn4dHGE', 'http://www.youtube.com/embed/tMfLKrGvCzI', 'http://www.youtube.com/embed/LVlDSzbrH5M', 'http://www.you\
tube.com/embed/BUULBlDcju4', 'https://www.youtube.com/embed/UQ13nr6urIo', 'www.youtube.com/embed/3xUfCUFPL-8', 'www.youtube.com/embed/Mq-aVCUs2Q0', 'http://www.youtube.com/embed/ph7oZnBH05s', 'http://www\
.youtube.com/embed/42Tah0DCubg']
for url in url_list:
    downloaded_file_path = convert_embed_url_and_download(url)
    print "download file path:", downloaded_file_path 

    upload_s3(downloaded_file_path)

    #images = extract_images(downloaded_file_path)
    #print 'Here is the task_id: %s' %  IronWorker.task_id()
