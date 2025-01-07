from src.idlixHelper import IdlixHelper, logger
from prettytable import PrettyTable
import inquirer
import os

status_exit = False
while not status_exit:
    idlix_helper = IdlixHelper()

    question = [
        inquirer.List(
            "action",
            message="Select action",
            choices=[
                "Download Movie by URL",
                "Download Episode Series by URL",
                "Download subtitle only by URL",
                "Exit"
            ],
            carousel=True
        )
    ]
    answer = inquirer.prompt(question)

    if answer['action'] == "Download Movie by URL":
        url = input("Enter movie URL ( Ex : https://vip.idlixofficialx.net/movie/kung-fu-panda-4-2024/) : ")
        get_video_data = idlix_helper.get_movie_data(url)
        if get_video_data['status']:
            logger.info("Getting video data | Video ID : " + get_video_data['video_id'] + " | Video Name : " + get_video_data['video_name'])

            get_embed_url = idlix_helper.get_embed_url()
            if get_embed_url['status']:
                logger.info("Getting embed url | Embed URL : " + get_embed_url['embed_url'])

                get_m3u8_url = idlix_helper.get_m3u8_url()
                if get_m3u8_url['status']:
                    logger.info("Getting m3u8 url | M3U8 URL : " + get_m3u8_url['m3u8_url'])
                    if get_m3u8_url['is_variant_playlist']:
                        logger.warning("This video has variant playlist")
                        question = [
                            inquirer.List(
                                "variant",
                                message="Select variant",
                                choices=[str(i.get('id')) + "." + str(i.get('resolution')) for i in get_m3u8_url['variant_playlist']],
                                carousel=True
                            )
                        ]
                        answer = inquirer.prompt(question)
                        for variant in get_m3u8_url['variant_playlist']:
                            if variant['id'] == answer['variant'].split(".")[0]:
                                logger.success("Selected variant : " + variant['resolution'])
                                idlix_helper.set_m3u8_url(variant['uri'])
                                break
                    else:
                        logger.warning("This video has no variant playlist")

                    download_m3u8 = idlix_helper.download_m3u8()
                    if download_m3u8['status']:
                        logger.success("Downloading {} Success".format(get_video_data['video_name']))

                        download_subtitle = idlix_helper.get_subtitle()
                        if download_subtitle['status']:
                            logger.success("Download subtitle success")
                        else:
                            logger.error("Error download subtitle")
                    else:
                        logger.error("Error downloading m3u8")
                else:
                    logger.error("Error getting m3u8 url")
            else:
                logger.error("Error getting embed url")
        else:
            logger.error("Couldn't find the data")

    # 
    # Download episode in series
    # 
    elif answer['action'] == "Download Episode Series by URL":
        url = input("Enter series eipsode URL ( Ex : https://tv7.idlix.asia/episode/squid-game-season-2-episode-2/) : ")
        get_video_data = idlix_helper.get_series_data(url)
        if get_video_data['status']:
            logger.info("Getting video data | Video ID : " + get_video_data['video_id'] + " | Video Name : " + get_video_data['video_name'])

            get_embed_url = idlix_helper.get_embed_url()
            if get_embed_url['status']:
                logger.info("Getting embed url | Embed URL : " + get_embed_url['embed_url'])

                get_m3u8_url = idlix_helper.get_m3u8_url()
                if get_m3u8_url['status']:
                    logger.info("Getting m3u8 url | M3U8 URL : " + get_m3u8_url['m3u8_url'])
                    if get_m3u8_url['is_variant_playlist']:
                        logger.warning("This video has variant playlist")
                        question = [
                            inquirer.List(
                                "variant",
                                message="Select variant",
                                choices=[str(i.get('id')) + "." + str(i.get('resolution')) for i in get_m3u8_url['variant_playlist']],
                                carousel=True
                            )
                        ]
                        answer = inquirer.prompt(question)
                        for variant in get_m3u8_url['variant_playlist']:
                            if variant['id'] == answer['variant'].split(".")[0]:
                                logger.success("Selected variant : " + variant['resolution'])
                                idlix_helper.set_m3u8_url(variant['uri'])
                                break
                    else:
                        logger.warning("This video has no variant playlist")

                    download_m3u8 = idlix_helper.download_m3u8()
                    if download_m3u8['status']:
                        logger.success("Downloading {} Success".format(get_video_data['video_name']))
                        
                        download_subtitle = idlix_helper.get_subtitle()
                        if download_subtitle['status']:
                            logger.success("Download subtitle success")
                        else:
                            logger.error("Error download subtitle")
                    else:
                        logger.error("Error downloading m3u8")
                else:
                    logger.error("Error getting m3u8 url")
            else:
                logger.error("Error getting embed url")
        else:
            logger.error("Couldn't find the series")
    elif answer['action'] == "Download subtitle only by URL":
        url = input("Enter movie/episode URL ( Ex : https://tv7.idlix.asia/episode/squid-game-season-2-episode-2/): \n")
        get_video_data = ''
        if url.startswith(idlix_helper.BASE_WEB_URL + 'movie/'):
            get_video_data = idlix_helper.get_movie_data(url)
        else:
            get_video_data = idlix_helper.get_series_data(url)
        
        if get_video_data['status']:
            get_embed_url = idlix_helper.get_embed_url()
            if get_embed_url['status']:
                get_m3u8_url = idlix_helper.get_m3u8_url()
                if (get_m3u8_url['status']):
                    download_subtitle = idlix_helper.get_subtitle()
                    if download_subtitle['status']:
                        logger.success("Download subtitle success")
                    else:
                        logger.error("Error download subtitle: " + download_subtitle['message'])
                else:
                    logger.error('[ERROR] Failed get get_m3u8_url')
            else:
                logger.error('[ERROR] Failed embeded url.')
        else:
            logger.error('[ERROR] Error getting video data')
    else:
        logger.info("Exiting")
        status_exit = True
