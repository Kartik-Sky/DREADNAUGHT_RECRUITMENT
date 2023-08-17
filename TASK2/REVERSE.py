import cv2
cap=cv2.VideoCapture("video.mp4")
success=True
frame_list=[]
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (success==True):
    success,frame=cap.read()
    frame_list.append(frame)

frame_list.pop()
original_frame_rate = int(cap.get(cv2.CAP_PROP_FPS))


slow_down_factor = 2


output_video_path = 'output_video_slowed_down2.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
output_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_frame_rate = original_frame_rate // slow_down_factor  

out = cv2.VideoWriter(output_video_path, fourcc, output_frame_rate, (output_width, output_height))


for i in range(len(frame_list)-1,-1,-1):
    frame=frame_list[i]
    
    
    
    for _ in range(slow_down_factor):
        out.write(frame)

    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("VIDEO REVERSED SUCCESSFULLY")
cap.release()
out.release()
cv2.destroyAllWindows()


