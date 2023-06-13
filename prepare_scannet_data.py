import os
import shutil


scannet_data = "/home/pierre/dev/scannet2/scans/scene0580_00/out/"
out_folder = "/home/pierre/dev/tsdf-fusion-python/data"
nb_cameras = 4764



shutil.copyfile(os.path.join(scannet_data, "intrinsic", "intrinsic_depth.txt"), os.path.join(out_folder, "camera-intrinsics.txt"))
# need to manually convert from 4x4 to 3x3


for i in range(nb_cameras):
    shutil.copyfile(os.path.join(scannet_data, "color", "%d.jpg" % i), os.path.join(out_folder, "frame-%06d.color.jpg" % i))
    shutil.copyfile(os.path.join(scannet_data, "depth", "%d.png" % i), os.path.join(out_folder, "frame-%06d.depth.png" % i))
    shutil.copyfile(os.path.join(scannet_data, "pose", "%d.txt" % i), os.path.join(out_folder, "frame-%06d.pose.txt" % i))

