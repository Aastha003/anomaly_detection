
import os
import sys
from config import cfg 
from frames import FPS
from imutils import paths
from anomaly_detector import detector
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np
from numpy import asarray


IMG_WIDTH = 225
IMG_HEIGHT = 225

folder = {}
folder['main'] = '/Users/caast/Downloads/RA_Anomaly_Detection/'
if folder['main'] == '':
    folder['main'] = os.getcwd()

sys.path.append(folder["main"])
img_path = ''

cnf = cfg(folder["main"])
args = cnf.args

class img_parser:
    def parser():
        if args['isimage'] == True:
            img_path = list(paths.list_images(args['image']))[0]
            img = Image.open(img_path)
            output_img = detector.detect(img)
            tempname = os.path.splitext(args['image'])
            output_file = tempname[0] + '_anomaly.jpg'
            #plt.imshow(output_img)
            #plt.show()
            img.close()

        elif args['isvideo'] == True:
            video_file = os.listdir(args['video'])
            video_path = args['video'] + video_file[0]
            #print(video_path)
            #video_path = list(paths.list_images(args['video']))[0]
            #print(list(paths.list_images(args['image']))[0])
            cap = cv2.VideoCapture(video_path)
            tempname = os.path.splitext(video_file)
            output_file = tempname[0] + '_anomaly.avi'
            #time_length = 30.0
            #fps=2
            #frame_seq = 749
            #frame_no = (frame_seq /(time_length*fps))
            #cap.set(2,frame_no);

        if not args['isimage']:
            video_writer = cv2.VideoWriter(os.path.join(args['output_videos'], output_file),
                                               cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                               cap.get(cv2.CAP_PROP_FPS), (
                                                   round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                                   round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))


        fps = FPS()
        fps.start()
        while True:
            has_frame, frame = cap.read()

            # Stop the program if reached end of video
            if not has_frame:
                print('Output file is stored at', os.path.join(args['output_videos'], output_file))
                cv2.waitKey(1000)
                break

                # Create a 4D blob from a frame.
            #blob = cv2.dnn.blobFromImage(frame, 1 / 255, (IMG_WIDTH, IMG_HEIGHT),
            #                                 [0, 0, 0], 1, crop=False)

            #print(frame)
            #img = Image.open(frame)
            img = Image.fromarray(frame)
            size = img.size
            output_frame = detector.detect(img)

            output_frame = output_frame.resize(size)
            output_frame = asarray(output_frame)

            #print(output_frame)
            # Save the output video to file
            if args['isimage']:
                cv2.imwrite(os.path.join(args['output_images'], output_file), frame.astype(np.uint8))
            else:
                video_writer.write(output_frame.astype(np.uint8))

            #plt.imshow(output_frame)
            #plt.show()

            key = cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                print('Interrupted by user!')
                break

            fps.update()

        #video_writer.close()
        fps.stop()
        fps.elapsed()
        total_frames = fps.fps()
        #print(total_frames)

        cap.release()
        cv2.destroyAllWindows()
