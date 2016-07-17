import sys
sys.path.append("packages")
import iron_mq
from iron_worker import *
from video_download import *
from image_extract import *
from upload_s3 import *
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('avajams.download')

def main():
    payload = IronWorker.payload()
    print 'payload: %s' % payload 
    url = payload['url']
    _, video_id = convert_embed_to_watch(url)
    video_file_name = "video_%s.mp4" % video_id
    logger.info("processing %s %s", url, video_file_name)

    if not file_exists_s3(video_file_name):
        logger.info("%s does not exists downloading it from %s", video_file_name, url)
        try:
            downloaded_file_path = convert_embed_url_and_download(url)
        except Exception,e:
            logger.error("could not download file: %s", e)
            return
        logger.info("uploading %s to %s", downloaded_file_path, "https://s3.amazonaws.com/avajams/"+video_file_name)
        upload_s3(downloaded_file_path)
        logger.info("task complete")
    else:
        logger.info("file already downloaded")
        #images = extract_images(downloaded_file_path)

if __name__ == '__main__':
    main()
