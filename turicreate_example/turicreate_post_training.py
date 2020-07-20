import turicreate as tc

# Load the model
model_file = './probe_id_model_dir/probe_id.model'
model = tc.load_model(model_file)

# Load the test images
path_prefix = '../medical_data/mp4_probe_overlayed/extracted_frames/vid1/'
filename = 'img0002.jpg'
file = path_prefix + filename

test_image = tc.SFrame({'image':[tc.Image(file)]})

test_image['predictions'] = model.predict(test_image, confidence_threshold=0)
print(test_image['predictions'])

'''
test_image['annotated_predictions'] = \
    tc.one_shot_object_detector.util.draw_bounding_boxes(
        test_image['image'],
        test_image['predictions']
    )

print(test_image['annotated_predictions'])

test_image.explore()
'''
