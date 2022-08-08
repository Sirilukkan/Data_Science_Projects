**This project is about how to detect malaria from red blood cells images**  
## **Context**
------
Malaria is one of contagious disease that is serious and sometimes can cause death and it is still a burden to global health. The cause of malaria is from the plasmodium parasites which transmit to human through the bite of female Anopheles mosquitoes. These parasites can damage the red blood cells (RBCs) that carry the oxygen. The symptoms of fever, headache and chills usually appear 10-15 days after the infective mosquito bite, which can be difficult to detect, and some parasites can cause deaths in 24 hours. 
According to the latest report from World Health Organization (WHO),  In 2020, 50% of the world’s population was at risk from malaria. There were also an estimated of 241 million cases of malaria worldwide and 627,000 related deaths reported in 2020. Children under 5 years old are the most vulnerable group of people.
Early state of malaria detection is needed, and traditional diagnosis needs experienced professional to manually detect whether the red blood cell images are parasitized or uninfected and it is also time consuming. Therefore, deep learning has played a key role in increasing detection time and removing human errors in malaria detection. Several deep learning models have been studied and developed. One of the most used deep learning models in image detection and computer vision is CNN. There are several ways and techniques of creating CNN architectures and they needed to be studied carefully. One CNN model might do better in one problem but might do worst in other problems. Therefore, in this project, several CNN models are studied and several metrics to measure accuracy of different CNN models are calculated.  


--------
## **Key Questions**
------  
* How the image of infected and heathy red blood cell looks like? 
* What techniques should we use for image data preprocessing to make the image less complex and more clear to be used in later analysis applying computer vision model.
* How accurate our model can distingush between infected and uninfected red blood cell images? 
* Which CNN models with what structure and parameters are the best?  
* How much labeled training data is necessary for achieving acceptable accuracies?  
* Could successful model be applied on a different disease detection through transfer learning?  
  
----------------------
## **Data Dictionary**
-----------------------  
There are a total of 24,958 train and 2,600 test images (colored) that we have taken from microscopic images. These images are of the following categories:

Parasitized: The parasitized cells contain the Plasmodium parasite which causes malaria
Uninfected: The uninfected cells are free of the Plasmodium parasites
