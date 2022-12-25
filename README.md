# SPICED Week09: Bayer04 jersey recognition on live footage using a 'Convolutional_Neural_Networks' (Keras)

## Project Summary

Have you ever wondered which year the Bayer04 vintage jersey in your wardrobe is from? Maybe I can help.

As part of this project, I took between 150 and 200 photos of five different Bayer04 photos and used them to train a 'Convolutional_Neural_Networks' (CNN) using the library 'Keras'. As you can see on the following demonstration video, the programme was subsequently able to classify all six jerseys without errors.

In addition, I trained the pretrained CNN VGG-16 on the two most similar jerseys to test its performance. The user can choose in the script between using the independently trained model or VGG-16.

IMPORTANT: The two models and the photos of the six jerseys in the folder './1_data/' were not uploaded to GitHub because they were too large. So this is only a skeleton that you can use to train and apply your own model.

## Demonstration Video

https://user-images.githubusercontent.com/61935581/209471946-48e37de4-191b-490c-98cf-f49383481eaa.mp4

## Installation

Clone the repository and create a new virtual environment

```bash
python3 -m venv envname # to create the virtual env
source envname/bin/activate # activate it
```

Afterwards install the libraries specified in requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

The project contains three major components:

### 1. Take pictures of your objects

To take pictures of the objects that the CNN should later distinguish, please use the ['imageclassifier' repo](https://github.com/bonartm/imageclassifier) by user 'bonartm', which is already in the order './take_pictures/'. The repo has its own README.md which explains exactly how to use it.

As mentioned above, I took between 150 and 200 photos of the five different jerseys and the blank wall. I rotated the jerseys to get shots from all perspectives.

### 2. Train the CNN model on the pictures

With the jupyter notebook '2_Image_Recognition.ipynb' you can train the CNN model on your pictures. At the end of the notebook you will find a confusion matrix that gives you an impression of how well the model is performing on the test data.

If you also want to train the pretrained VGG-16 model on your photos, you can use the jupyter notebook '3_Transfer_Pretrained_Model.ipynb' to do so.

### 3. Use the model on live footage

Use the script 'image_recognition.py' to perform image recognition on live footage. As it stands, the script asks which model to use for categorisation - the fully self-trained CNN model (option 1) or VGG-16 (option 2).

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
