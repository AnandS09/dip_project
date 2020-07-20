import turicreate as tc

starter_img_path = './images/medical_images/probe_images/probe_image.png'
starter_images = tc.SFrame({'image':[tc.Image(starter_img_path)],
                            'label':['probe']}
                           )

model = tc.one_shot_object_detector.create(starter_images, 'label', max_iterations=1000)
model.save('probe_id2.model')