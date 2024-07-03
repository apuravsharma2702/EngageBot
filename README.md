<h1 align="center">EngageBot - Intelligent University Assistance System</h1>

<h2 align = "center">Software</h2>
This system will comprise of a front end application where the user could ask the queries
which would act as User Interface. The query asked by the user is then processed by our
deep learning model and the response is fetched from from the database .This system is
composed of two parts:

- Back-end: Neural Network model

- Front-end: Implemented using Kivy Python GUI Framework

<h3>Backend</h3>

- **Neural Network Model** - We developed a Multilayer Perceptron (MLP) with two hidden layers of 8 perceptrons each, using linear activation functions. The input and output layers match the number of categories in our database. The model employs Multinomial Logistic Regression and Backpropagation to optimize weights. Backpropagation calculates the gradient of the loss function layer by layer, iterating backward to improve efficiency.

  After 3000 epochs, our model achieved 98% accuracy. The output layer uses the softmax activation function to classify inputs into multiple categories, transforming values to probabilities that sum to 1. Implemented in Python with the Tflearn module, this neural network accurately classifies user input into the correct category.

- **Dataset Overview** - Our dataset includes various categories or tags of data users are expected to ask about. Each category has:
  - User query patterns/questions.
  - Possible responses.
For example, the 'Greeting' category has queries like "Hello" mapped to appropriate responses. Tags group related queries and responses, allowing for easy dataset expansion and improved accuracy. This data trains a neural network to classify inputs and provide relevant responses.

  ![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/c69f1998-0749-43b5-a316-d426199debad)

  The dataset is stored as a JSON object in Python, using the json module. To secure the training data and model weights, we use the pickle module for encoding into a character stream, simplifying storage and ensuring data integrity. This format:

  - Simplifies adding new tags.
  - Ensures easy maintenance and extension.
  - Reduces memory requirements.

- **Data Processing** - Before feeding data to the neural network, we preprocess input using natural language processing (NLP) steps:

  - Word Tokenization: Queries are split into individual words (tokens) to accommodate varied user inputs.
  - Stop Words Removal: Common, non-meaningful words ('a', 'and', 'the') are filtered out to reduce noise.
  - Stemming: Words are reduced to their root forms using the Lancaster Stemmer from the NLTK package (e.g., 'finding', 'found', 'finds' become 'find').
  - One Hot Encoding: Each query is converted into a binary code based on the word list, forming the input for the labeled dataset. The output categories are also one hot encoded.
    
  This labeled dataset is used to train the model. User inputs are preprocessed similarly before classification. The model assigns the category with the highest probability (above 80%) as the output and selects a random response from that category to answer the user's query.

<h3>Frontend - Using Kivy Python GUI Framework</h3>

- **Application Design** - 

![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/a6306877-53b2-415c-9ffc-0c697888ef3f)

- **Features** -
  - Admission Process
  - Location of class rooms/faculties/labs/ staff rooms

    ![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/fa07dd5c-ae57-415a-abb8-04e3f96e10b0)

  - Procedure for Submitting forms such as Bonafide/Railway Concession
  - Access any circulars such as time table, exam schedule, fee details,committees,events

    ![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/1b8a0e3d-c56c-46b0-84ca-8f9cfe662e07)

  - ReadMe manual for users
 
    ![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/38ad76d9-a755-4cd9-922e-1e3a40fb068f)

  - Detect idle activity of the user

    ![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/12ff2e38-5c5a-4eba-a4df-72edb2cf056a)


<h2 align="center">Hardware</h2>

<h3>Proposed Structure of bot</h3>
The chatbot's exterior is designed considering average human height, ensuring sturdy and smooth movement. The bot stands 100-150 cm tall, with a 30 sqcm base to secure components and allow air space. Lightweight materials, such as carbon fiber or high-quality plastics (acetal, thermoplastic polypropylene), are used for encasing to facilitate movement and insulate against heat and electricity. For stability, a heavy base or a hollow metal rod backbone can be added. The total weight is approximately 4-5 kg.

![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/4f298d38-fd0c-452f-b75f-3fb438b66ca7)

<h3>Movement control</h3>

- **Obstacle Avoidance** - Our bot uses ultrasonic sensors for obstacle avoidance. Two front-facing and two side sensors at the base edges are connected to an Arduino Uno. The bot detects obstacles within the sensors' range and adjusts its movement accordingly. If an obstacle is detected, the bot strafes left or right; if all sensors detect an obstacle, the bot stops. Mecanum wheels enable versatile movement based on sensor input.

![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/c215f4f5-83fb-42f7-89d9-e50f46912898)

- **Directional movements** - Mecanum wheels have 45-degree rollers on their circumference, enabling diagonal force for multi-directional movement. Two types exist: left-handed and right-handed, differing by roller orientation. For forward/backward motion, all wheels rotate in the same direction. To strafe right, right wheels rotate inward, and left wheels rotate outward. The opposite pattern strafes left. This design allows the bot to move diagonally and rotate 360 degrees.

![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/5239792b-288e-45fc-93ea-0458d51ca404)

- **Virtual Bot Movement Simulation** - Our bot's virtual simulation includes forward, backward, right, and left movements. Each DC motor is controlled by a potentiometer for RPM regulation. The L293D motor driver IC, with 16 pins, enables individual clockwise and anti-clockwise rotation of two DC motors. Motors are connected to the IC for directional control: positive terminal high for clockwise and negative terminal high for anti-clockwise rotation. Inputs from the serial monitor trigger motor rotations to achieve the desired wheel movement pattern, such as strafing right by rotating right wheels inward and left wheels outward.

![image](https://github.com/apuravsharma2702/EngageBot/assets/75594408/0f92655a-0872-4692-bfd0-ae3fdf305669)
