import os
import rospy
from shutil import move
from tempfile import gettempdir, NamedTemporaryFile
from ipfshttpclient import connect
from rosbag import Bag

def ipfs_download_txt_file(ipfs_hash: str) -> str:
    temp_log = NamedTemporaryFile(delete=False)
    ipfs_download_file(connect(), ipfs_hash, temp_log.name)

    with open(temp_log.name) as f:
        return f.read()

def ipfs_download_file(ipfs_client, multihash, filepath):
    file_dst = filepath
    dst_dir, dst_file = os.path.split(file_dst)

    if not os.path.isdir(dst_dir):
        try:
            os.mkdir(dst_dir)
        except Exception as e:
            rospy.logerr("Directory %s does not exists and cannot be created: %s", e)
            return False

    if os.path.isdir(file_dst):
        rospy.logwarn(
            "Collision between existed directory and IPFS downloading file destination \"%s\". Please fix it manually.",
            file_dst)
        return False

    try:
        tempdir = gettempdir()
        os.chdir(tempdir)
        ipfs_client.get(multihash)
        move(tempdir + os.path.sep + multihash, file_dst)
    except Exception as e:
        rospy.logerr("Failed to download %s to %s with exception: %s", multihash, file_dst, e)
    return True

def ipfs_download(multihash):
    tempdir = gettempdir()
    os.chdir(tempdir)

    temp_obj = NamedTemporaryFile(delete=False)

    res = ipfs_download_file(connect(), multihash.multihash, temp_obj.name)
    if not res:
        raise Exception("Can't download objective")
    messages = {}
    for topic, msg, timestamp in Bag(temp_obj.name, 'r').read_messages():
        messages[topic] = msg
    return messages

