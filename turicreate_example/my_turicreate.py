import turicreate as tc

# Load the starter images
starter_img_path = '../medical_data/probe_images/probe_image_resized.png'
starter_images = tc.SFrame({'image':[tc.Image(starter_img_path)],
                            'label':['probe']}
                           )

my_custom_background_images = []
vid_name = ['Vid1', 'Vid2', 'Vid3', 'Vid4']
num_img_vid = [192, 213, 169, 152]
prefix = '../medical_data/converted_mp4/extracted_frames/'

for i in range(len(vid_name)):
    vid = vid_name[i]
    num_img = num_img_vid[i]

    for n in range(num_img):
        filename = prefix + vid + '/'
        filename += 'img'
        filename += str(format(n+1, '04d'))
        filename += '.jpg'

        my_custom_background_images.append(filename)

#print(my_custom_background_images[0])

background_images = tc.SFrame({'image':my_custom_background_images})

model = tc.one_shot_object_detector.create(starter_images, 'label',
                                           backgrounds=background_images)


