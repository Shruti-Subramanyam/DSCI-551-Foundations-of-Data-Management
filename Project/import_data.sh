curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Elizabeth Montgomery",
  "contact": "(555) 123-4567",
  "location": "123 Elm Street, Springfield, IL 62704",
  "product_list": {
    "Canned_Tomato": {"inventory": 48, "price": 4, "rating": 4.7, "review_count": 39},
    "Frozen_Peas": {"inventory": 31, "price": 1, "rating": 3.5, "review_count": 8},
    "Canned_Peas": {"inventory": 72, "price": 7, "rating": 4.9, "review_count": 23}
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "William Harrison",
  "contact": "(555) 234-5678",
  "location": "456 Oak Avenue, Madison, WI 53703",
  "product_list": {
    "Fruits_Orange": {"inventory": 44, "price": 3, "rating": 4.6, "review_count": 42},
    "Vegetables_Lettuce": {"inventory": 86, "price": 4, "rating": 3.5, "review_count": 11},
    "Fruits_Apple": {"inventory": 43, "price": 10, "rating": 4.9, "review_count": 37}
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Sophia Loren",
  "contact": "(555) 345-6789",
  "location": "789 Pine Street, Boulder, CO 80302",
  "product_list": {
    "Vegetables_Onion": {
      "inventory": 36,
      "price": 10,
      "rating": 3.1,
      "review_count": 29
    },
    "Frozen_Broccoli": {
      "inventory": 74,
      "price": 9,
      "rating": 3.6,
      "review_count": 13
    },
    "Vegetables_Lettuce": {
      "inventory": 77,
      "price": 1,
      "rating": 3.4,
      "review_count": 22
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "James Patterson",
  "contact": "(555) 456-7890",
  "location": "101 Maple Drive, Austin, TX 78701",
  "product_list": {
    "Canned_Peas": {
      "inventory": 81,
      "price": 10,
      "rating": 4.4,
      "review_count": 43
    },
    "Frozen_Blueberry": {
      "inventory": 62,
      "price": 9,
      "rating": 3.8,
      "review_count": 9
    },
    "Fruits_Orange": {
      "inventory": 61,
      "price": 5,
      "rating": 4.4,
      "review_count": 44
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Margaret Thatcher",
  "contact": "(555) 567-8901",
  "location": "202 Birch Lane, Cambridge, MA 02138",
  "product_list": {
    "Fruits_Orange": {
      "inventory": 58,
      "price": 5,
      "rating": 4.6,
      "review_count": 23
    },
    "Frozen_Broccoli": {
      "inventory": 80,
      "price": 10,
      "rating": 3.4,
      "review_count": 38
    },
    "Vegetables_Potato": {
      "inventory": 57,
      "price": 1,
      "rating": 4.8,
      "review_count": 45
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Christopher Columbus",
  "contact": "(555) 678-9012",
  "location": "303 Cedar Road, Orlando, FL 32801",
  "product_list": {
    "Vegetables_Potato": {
      "inventory": 37,
      "price": 1,
      "rating": 3.7,
      "review_count": 11
    },
    "Canned_Peas": {
      "inventory": 46,
      "price": 8,
      "rating": 3.9,
      "review_count": 20
    },
    "Canned_Tomato": {
      "inventory": 83,
      "price": 3,
      "rating": 3.9,
      "review_count": 19
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Isabella Stewart Gardner",
  "contact": "(555) 789-0123",
  "location": "404 Willow Way, San Francisco, CA 94102",
  "product_list": {
    "Fruits_Apple": {
      "inventory": 76,
      "price": 7,
      "rating": 4.0,
      "review_count": 9
    },
    "Fruits_Orange": {
      "inventory": 66,
      "price": 9,
      "rating": 3.2,
      "review_count": 38
    },
    "Frozen_Peas": {
      "inventory": 59,
      "price": 7,
      "rating": 3.2,
      "review_count": 11
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Benjamin Franklin",
  "contact": "(555) 890-1234",
  "location": "505 Magnolia Blvd, Philadelphia, PA 19106",
  "product_list": {
    "Frozen_Peas": {
      "inventory": 55,
      "price": 7,
      "rating": 4.7,
      "review_count": 9
    },
    "Frozen_Blueberry": {
      "inventory": 55,
      "price": 3,
      "rating": 3.9,
      "review_count": 8
    },
    "Fruits_Apple": {
      "inventory": 60,
      "price": 8,
      "rating": 3.8,
      "review_count": 40
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Amelia Earhart",
  "contact": "(555) 901-2345",
  "location": "606 Ivy Circle, Seattle, WA 98104",
  "product_list": {
    "Canned_Corn": {
      "inventory": 44,
      "price": 4,
      "rating": 3.1,
      "review_count": 21
    },
    "Vegetables_Potato": {
      "inventory": 73,
      "price": 8,
      "rating": 3.9,
      "review_count": 7
    },
    "Fruits_Orange": {
      "inventory": 69,
      "price": 6,
      "rating": 3.0,
      "review_count": 42
    }
  }
}'

curl -X POST 'http://localhost/farmer/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '
{
  "name": "Nathaniel Hawthorne",
  "contact": "(555) 012-3456",
  "location": "707 Elmwood Avenue, Salem, MA 01970",
  "product_list": {
    "Frozen_Peas": {
      "inventory": 20,
      "price": 2,
      "rating": 3.7,
      "review_count": 50
    },
    "Vegetables_Carrot": {
      "inventory": 32,
      "price": 2,
      "rating": 4.9,
      "review_count": 50
    },
    "Vegetables_Potato": {
      "inventory": 66,
      "price": 3,
      "rating": 3.1,
      "review_count": 40
    }
  }
}'
