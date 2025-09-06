from JsonBuilder import Project

project = Project('National delicous', "Japanse")

project.SetDivs()

project.AddPng('C:/Users/admin/OneDrive/Desktop/JsonBuilder/udon.png')
project.AddPng('C:/Users/admin/OneDrive/Desktop/JsonBuilder/sushi.png')
project.AddPng('C:/Users/admin/OneDrive/Desktop/JsonBuilder/ramen.png')

project.AddChapter('Udon', 'Udon is a type of thick wheat noodle commonly used in Japanese cuisine. It is usually served hot in a mild broth made from dashi, soy sauce, and mirin. Udon can be enjoyed with various toppings such as tempura, green onions, or kamaboko (fish cake). It is known for its chewy texture and comforting flavor.')
project.AddChapter('Sushi', 'Sushi is a traditional Japanese dish that typically consists of vinegared rice combined with raw or cooked seafood, vegetables, and sometimes tropical fruits. There are many types of sushi, including nigiri (rice topped with fish), maki (rolled sushi), and sashimi (sliced raw fish without rice). Sushi is often served with soy sauce, wasabi, and pickled ginger.')
project.AddChapter('Ramen', 'Ramen is a popular Japanese noodle soup that features Chinese-style wheat noodles served in a meat or fish-based broth. The broth can be flavored with soy sauce, miso, or salt. Ramen is usually topped with ingredients like sliced pork (chashu), boiled eggs, seaweed, and green onions. It is a hearty and flavorful dish enjoyed worldwide.')

project.AddLink('youtube', 'https://youtube')

project.Finish()