#Script to extract facial features from videos and export it to a csv with the same name. 
#The file must be placed in the openface directory.

import subprocess
import os
import glob

# FNULL = open(os.devnull, 'w')
input_path = "C:\\Datasets\\MOUD\\VideoReviews\\*.mp4"
input_root  = "C:\\Datasets\\MOUD\\VideoReviews\\"
output_path = "C:\\Datasets\\MOUD\\OpenFaceFeatures\\"

for f in glob.glob(input_path):
    v_name = f.rsplit('\\',1)[-1]
    args = "FeatureExtraction.exe -f " + f + " -of " + output_path + v_name +".csv -q"
    print(args)
    # subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
    subprocess.call(args, shell=True)