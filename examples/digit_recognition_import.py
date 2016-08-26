from mnist import MNIST

from pylearn.neural_network import NeuralNetwork
from pylearn.preprocess import InputData

from neural_network_io import json_import
from preprocess_image import image_to_vector


mndata = MNIST('.\data\\numbers')
mndata.load_testing()

test_images_wrap, test_labels_wrap = InputData.image_matrix_normalizer(
    mndata.test_images, mndata.test_labels, range(10))

net = NeuralNetwork([784, 20, 10], 3)

json_import(net, 'examples/precomputed_nets/digit_recognition_2.json')

print("{0} / {1}, Cost: {2}".format(
        net.test_network(test_images_wrap, test_labels_wrap),
        len(test_images_wrap),
        net.batch_cost(test_images_wrap, test_labels_wrap)))

image = image_to_vector("C:/Users/Np/Desktop/7.jpg")
print(net.predict(image))
