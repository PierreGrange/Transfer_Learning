from ultralytics import YOLO
import cv2
import math
import numpy as np
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("yolo-Weights/yolov8n-oiv7.pt")

classNames = ['Accordion', 'Adhesive tape', 'Aircraft', 'Airplane', 'Alarm clock', 'Alpaca', 'Ambulance', 'Animal', 'Ant', 'Antelope', 'Apple', 'Armadillo', 'Artichoke', 'Auto part', 'Axe', 'Backpack', 'Bagel', 'Baked goods', 'Balance beam', 'Ball', 'Balloon', 'Banana', 'Band-aid', 'Banjo', 'Barge', 'Barrel', 'Baseball bat', 'Baseball glove', 'Bat (Animal)', 'Bathroom accessory', 'Bathroom cabinet', 'Bathtub', 'Beaker', 'Bear', 'Bed', 'Bee', 'Beehive', 'Beer', 'Beetle', 'Bell pepper', 'Belt', 'Bench', 'Bicycle', 'Bicycle helmet', 'Bicycle wheel', 'Bidet', 'Billboard', 'Billiard table', 'Binoculars', 'Bird', 'Blender', 'Blue jay', 'Boat', 'Bomb', 'Book', 'Bookcase', 'Boot', 'Bottle', 'Bottle opener', 'Bow and arrow', 'Bowl', 'Bowling equipment', 'Box', 'Boy', 'Brassiere', 'Bread', 'Briefcase', 'Broccoli', 'Bronze sculpture', 'Brown bear', 'Building', 'Bull', 'Burrito', 'Bus', 'Bust', 'Butterfly', 'Cabbage', 'Cabinetry', 'Cake', 'Cake stand', 'Calculator', 'Camel', 'Camera', 'Can opener', 'Canary', 'Candle', 'Candy', 'Cannon', 'Canoe', 'Cantaloupe', 'Car', 'Carnivore', 'Carrot', 'Cart', 'Cassette deck', 'Castle', 'Cat', 'Cat furniture', 'Caterpillar', 'Cattle', 'Ceiling fan', 'Cello', 'Centipede', 'Chainsaw', 'Chair', 'Cheese', 'Cheetah', 'Chest of drawers', 'Chicken', 'Chime', 'Chisel', 'Chopsticks', 'Christmas tree', 'Clock', 'Closet', 'Clothing', 'Coat', 'Cocktail', 'Cocktail shaker', 'Coconut', 'Coffee', 'Coffee cup', 'Coffee table', 'Coffeemaker', 'Coin', 'Common fig', 'Common sunflower', 'Computer keyboard', 'Computer monitor', 'Computer mouse', 'Container', 'Convenience store', 'Cookie', 'Cooking spray', 'Corded phone', 'Cosmetics', 'Couch', 'Countertop', 'Cowboy hat', 'Crab', 'Cream', 'Cricket ball', 'Crocodile', 'Croissant', 'Crown', 'Crutch', 'Cucumber', 'Cupboard', 'Curtain', 'Cutting board', 'Dagger', 'Dairy Product', 'Deer', 'Desk', 'Dessert', 'Diaper', 'Dice', 'Digital clock', 'Dinosaur', 'Dishwasher', 'Dog', 'Dog bed', 'Doll', 'Dolphin', 'Door', 'Door handle', 'Doughnut', 'Dragonfly', 'Drawer', 'Dress', 'Drill (Tool)', 'Drink', 'Drinking straw', 'Drum', 'Duck', 'Dumbbell', 'Eagle', 'Earrings', 'Egg (Food)', 'Elephant', 'Envelope', 'Eraser', 'Face powder', 'Facial tissue holder', 'Falcon', 'Fashion accessory', 'Fast food', 'Fax', 'Fedora', 'Filing cabinet', 'Fire hydrant', 'Fireplace', 'Fish', 'Flag', 'Flashlight', 'Flower', 'Flowerpot', 'Flute', 'Flying disc', 'Food', 'Food processor', 'Football', 'Football helmet', 'Footwear', 'Fork', 'Fountain', 'Fox', 'French fries', 'French horn', 'Frog', 'Fruit', 'Frying pan', 'Furniture', 'Garden Asparagus', 'Gas stove', 'Giraffe', 'Girl', 'Glasses', 'Glove', 'Goat', 'Goggles', 'Goldfish', 'Golf ball', 'Golf cart', 'Gondola', 'Goose', 'Grape', 'Grapefruit', 'Grinder', 'Guacamole', 'Guitar', 'Hair dryer', 'Hair spray', 'Hamburger', 'Hammer', 'Hamster', 'Hand dryer', 'Handbag', 'Handgun', 'Harbor seal', 'Harmonica', 'Harp', 'Harpsichord', 'Hat', 'Headphones', 'Heater', 'Hedgehog', 'Helicopter', 'Helmet', 'High heels', 'Hiking equipment', 'Hippopotamus', 'Home appliance', 'Honeycomb', 'Horizontal bar', 'Horse', 'Hot dog', 'House', 'Houseplant', 'Human arm', 'Human beard', 'Human body', 'Human ear', 'Human eye', 'Human face', 'Human foot', 'Human hair', 'Human hand', 'Human head', 'Human leg', 'Human mouth', 'Human nose', 'Humidifier', 'Ice cream', 'Indoor rower', 'Infant bed', 'Insect', 'Invertebrate', 'Ipod', 'Isopod', 'Jacket', 'Jacuzzi', 'Jaguar (Animal)', 'Jeans', 'Jellyfish', 'Jet ski', 'Jug', 'Juice', 'Kangaroo', 'Kettle', 'Kitchen & dining room table', 'Kitchen appliance', 'Kitchen knife', 'Kitchen utensil', 'Kitchenware', 'Kite', 'Knife', 'Koala', 'Ladder', 'Ladle', 'Ladybug', 'Lamp', 'Land vehicle', 'Lantern', 'Laptop', 'Lavender (Plant)', 'Lemon', 'Leopard', 'Light bulb', 'Light switch', 'Lighthouse', 'Lily', 'Limousine', 'Lion', 'Lipstick', 'Lizard', 'Lobster', 'Loveseat', 'Luggage and bags', 'Lynx', 'Magpie', 'Mammal', 'Man', 'Mango', 'Maple', 'Maracas', 'Marine invertebrates', 'Marine mammal', 'Measuring cup', 'Mechanical fan', 'Medical equipment', 'Microphone', 'Microwave oven', 'Milk', 'Miniskirt', 'Mirror', 'Missile', 'Mixer', 'Mixing bowl', 'Mobile phone', 'Monkey', 'Moths and butterflies', 'Motorcycle', 'Mouse', 'Muffin', 'Mug', 'Mule', 'Mushroom', 'Musical instrument', 'Musical keyboard', 'Nail (Construction)', 'Necklace', 'Nightstand', 'Oboe', 'Office building', 'Office supplies', 'Orange', 'Organ (Musical Instrument)', 'Ostrich', 'Otter', 'Oven', 'Owl', 'Oyster', 'Paddle', 'Palm tree', 'Pancake', 'Panda', 'Paper cutter', 'Paper towel', 'Parachute', 'Parking meter', 'Parrot', 'Pasta', 'Pastry', 'Peach', 'Pear', 'Pen', 'Pencil case', 'Pencil sharpener', 'Penguin', 'Perfume', 'Person', 'Personal care', 'Personal flotation device', 'Piano', 'Picnic basket', 'Picture frame', 'Pig', 'Pillow', 'Pineapple', 'Pitcher (Container)', 'Pizza', 'Pizza cutter', 'Plant', 'Plastic bag', 'Plate', 'Platter', 'Plumbing fixture', 'Polar bear', 'Pomegranate', 'Popcorn', 'Porch', 'Porcupine', 'Poster', 'Potato', 'Power plugs and sockets', 'Pressure cooker', 'Pretzel', 'Printer', 'Pumpkin', 'Punching bag', 'Rabbit', 'Raccoon', 'Racket', 'Radish', 'Ratchet (Device)', 'Raven', 'Rays and skates', 'Red panda', 'Refrigerator', 'Remote control', 'Reptile', 'Rhinoceros', 'Rifle', 'Ring binder', 'Rocket', 'Roller skates', 'Rose', 'Rugby ball', 'Ruler', 'Salad', 'Salt and pepper shakers', 'Sandal', 'Sandwich', 'Saucer', 'Saxophone', 'Scale', 'Scarf', 'Scissors', 'Scoreboard', 'Scorpion', 'Screwdriver', 'Sculpture', 'Sea lion', 'Sea turtle', 'Seafood', 'Seahorse', 'Seat belt', 'Segway', 'Serving tray', 'Sewing machine', 'Shark', 'Sheep', 'Shelf', 'Shellfish', 'Shirt', 'Shorts', 'Shotgun', 'Shower', 'Shrimp', 'Sink', 'Skateboard', 'Ski', 'Skirt', 'Skull', 'Skunk', 'Skyscraper', 'Slow cooker', 'Snack', 'Snail', 'Snake', 'Snowboard', 'Snowman', 'Snowmobile', 'Snowplow', 'Soap dispenser', 'Sock', 'Sofa bed', 'Sombrero', 'Sparrow', 'Spatula', 'Spice rack', 'Spider', 'Spoon', 'Sports equipment', 'Sports uniform', 'Squash (Plant)', 'Squid', 'Squirrel', 'Stairs', 'Stapler', 'Starfish', 'Stationary bicycle', 'Stethoscope', 'Stool', 'Stop sign', 'Strawberry', 'Street light', 'Stretcher', 'Studio couch', 'Submarine', 'Submarine sandwich', 'Suit', 'Suitcase', 'Sun hat', 'Sunglasses', 'Surfboard', 'Sushi', 'Swan', 'Swim cap', 'Swimming pool', 'Swimwear', 'Sword', 'Syringe', 'Table', 'Table tennis racket', 'Tablet computer', 'Tableware', 'Taco', 'Tank', 'Tap', 'Tart', 'Taxi', 'Tea', 'Teapot', 'Teddy bear', 'Telephone', 'Television', 'Tennis ball', 'Tennis racket', 'Tent', 'Tiara', 'Tick', 'Tie', 'Tiger', 'Tin can', 'Tire', 'Toaster', 'Toilet', 'Toilet paper', 'Tomato', 'Tool', 'Toothbrush', 'Torch', 'Tortoise', 'Towel', 'Tower', 'Toy', 'Traffic light', 'Traffic sign', 'Train', 'Training bench', 'Treadmill', 'Tree', 'Tree house', 'Tripod', 'Trombone', 'Trousers', 'Truck', 'Trumpet', 'Turkey', 'Turtle', 'Umbrella', 'Unicycle', 'Van', 'Vase', 'Vegetable', 'Vehicle', 'Vehicle registration plate', 'Violin', 'Volleyball (Ball)', 'Waffle', 'Waffle iron', 'Wall clock', 'Wardrobe', 'Washing machine', 'Waste container', 'Watch', 'Watercraft', 'Watermelon', 'Weapon', 'Whale', 'Wheel', 'Wheelchair', 'Whisk', 'Whiteboard', 'Willow', 'Window', 'Window blind', 'Wine', 'Wine glass', 'Wine rack', 'Winter melon', 'Wok', 'Woman', 'Wood-burning stove', 'Woodpecker', 'Worm', 'Wrench', 'Zebra', 'Zucchini']

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2),(255,255,0), 2)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls] + " : " + str(confidence), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()