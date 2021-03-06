import turicreate as tc

# Load the starter images
starter_img_path = './images/medical_images/probe_images/probe_image.png'
starter_images = tc.SFrame({'image':[tc.Image(starter_img_path)],
                            'label':['probe']}
                           )

my_custom_background_images = []
vid_name = ['Vid1', 'Vid2', 'Vid3', 'Vid4']
num_img_vid = [192, 213, 169, 152]
prefix = './images/medical_images/converted_mp4/extracted_frames/'

for i in range(len(vid_name)):
    num_img = num_img_vid[i]
    vid = vid_name[i]

    for n in range(num_img):
        filename = prefix + vid + '/'
        filename += 'img'
        filename += str(format(n+1, '04d'))
        filename += '.jpg'

        image = tc.Image(filename)

        my_custom_background_images.append(image)

background_images = tc.SArray(data=my_custom_background_images)

model = tc.one_shot_object_detector.create(starter_images, 'label',
                                           backgrounds=background_images,
                                           max_iterations=1000)

model.save('probe_id_custom_bk.model')

