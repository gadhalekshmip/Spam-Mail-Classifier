# Spam Mail Classification using Naive Bayes Classifier
This project is a simple spam mail classifier that uses the Naive Bayes Classifier algorithm to classify emails as spam or ham. The application uses Tkinter library to create a GUI window to display the email information and buttons to perform actions such as send and delete.

## Installation
To run this project, you will need to install the following packages:

Python 3.7 or higher
Tkinter
NLTK
Scikit-learn
To install these packages, you can use the pip package manager. Run the following command:
"pip install tkinter nltk scikit-learn"
## Usage
To use this spam mail classifier, you need to run the NB.py file. This will launch the Tkinter window where you can enter the email details such as the from, to, and subject.

Once you have entered the email details, click the "Send" button to classify the email as spam or ham. If the email is classified as spam, a pop-up alert will be displayed to inform you that the email is spam. You can then choose to send or delete the email using the respective buttons.

## How it works
This spam mail classifier uses the Naive Bayes Classifier algorithm to classify emails as spam or ham. The classifier is trained using a dataset of spam and ham emails. 

When an email is entered into the application, the text is preprocessed in the same way as the training dataset. The classifier then calculates the probability that the email is spam or ham using the Naive Bayes algorithm. If the probability of spam is higher than the probability of ham, the email is classified as spam.

![image](https://user-images.githubusercontent.com/99868658/236772350-f0410d71-e9b1-4e2f-838f-e6ffee6c30b2.png)

![image](https://user-images.githubusercontent.com/99868658/236772964-9059a65e-6d72-49a0-a51b-f45914ba39fb.png)

![image](https://user-images.githubusercontent.com/99868658/236773108-d4f38db1-e323-4590-99d3-a8d26c558b17.png)




## Contributing
Contributions to this project are welcome. If you find a bug or have a suggestion for a new feature, please open an issue or submit a pull request.

