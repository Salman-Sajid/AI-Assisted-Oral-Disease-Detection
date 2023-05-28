**AI-Assisted-Oral-Disease-Detection**

One Touch Dentistry is a research-based product that leverages computer vision technology to revolutionize the field of dentistry. Our project utilizes the YOLOv5 object detection model, combined with augmented and annotated datasets created using the MakeSense.ai website. The frontend and backend of our application are built using React Native and FastAPI, respectively, providing a seamless user experience.

Key Features
Efficient Object Detection: We have trained our model using YOLOv5, a state-of-the-art deep learning algorithm, to accurately detect and locate dental objects in images. This allows for quick and precise identification of various dental instruments and oral anomalies.

Augmented and Annotated Dataset: We have curated an extensive dataset using the MakeSense.ai website, which provides a user-friendly interface for annotating and augmenting images. This dataset has been meticulously labeled and enhanced to ensure reliable training and robust predictions.

User-Friendly Mobile Application: Our frontend is developed using React Native, a popular framework for building cross-platform mobile applications. With an intuitive and visually appealing interface, users can easily capture images of dental scenarios and receive real-time predictions.

Seamless Integration: The frontend and backend are connected via FastAPI, a modern, fast, and easy-to-use web framework for building APIs. This enables smooth communication between the user's mobile device and the deep learning model, ensuring a responsive and efficient user experience.

Local Deployment: Our application can be deployed locally, allowing users to harness the power of our dental object detection model directly on their own devices. This provides privacy and ensures that sensitive patient data remains secure.

Kaggle Dataset: To further contribute to the research community, we have uploaded our carefully curated dataset to Kaggle. This dataset is available for public use, enabling researchers and developers to train their own dental object detection models or enhance existing ones.
Link: https://www.kaggle.com/datasets/salmansajid05/oral-diseases

How It Works
The user captures an image of a dental scenario using the One Touch Dentistry mobile application.
The image is sent to the backend, powered by FastAPI, for further processing.
Our YOLOv5 model analyzes the image and accurately detects and localizes dental instruments or anomalies within it.
The predictions are then sent back to the mobile application in real-time.
The user receives the annotated image, with identified dental objects outlined, allowing for easier analysis and diagnosis.
