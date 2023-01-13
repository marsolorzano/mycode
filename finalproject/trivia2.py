#!/usr/bin/env python3 

def main():
  results: [
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Who wrote the novel &quot;Moby-Dick&quot;?",
      "correct_answer": "Herman Melville",
      "incorrect_answers": [
        "William Golding",
        "William Shakespeare",
        "J. R. R. Tolkien"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "easy",
      "question": "Which of the following is the world&#039;s best-selling book?",
      "correct_answer": "The Lord of the Rings",
      "incorrect_answers": [
        "The Little Prince",
        "Harry Potter and the Philosopher&#039;s Stone",
        "The Da Vinci Code"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "medium",
      "question": "In the Lord of the Rings, who is the father of the dwarf Gimli?",
      "correct_answer": "Gloin",
      "incorrect_answers": [
        "Thorin Oakenshield",
        "Bombur",
        "Dwalin"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "easy",
      "question": "Who wrote the novel &#039;Fear And Loathing In Las Vegas&#039;?",
      "correct_answer": "Hunter S. Thompson",
      "incorrect_answers": [
        "F. Scott Fitzgerald",
        "Henry Miller",
        "William S. Burroughs"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "easy",
      "question": "&quot;Green Eggs And Ham&quot; is a book by which author?",
      "correct_answer": "Dr. Seuss",
      "incorrect_answers": [
        "Beatrix Potter",
        "Roald Dahl",
        "A.A. Milne"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "medium",
      "question": "By what name was the author Eric Blair better known?",
      "correct_answer": "George Orwell",
      "incorrect_answers": [
        "Aldous Huxley",
        "Ernest Hemingway",
        "Ray Bradbury"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "easy",
      "question": "What&#039;s Harry Potter&#039;s dad&#039;s name?",
      "correct_answer": "James Potter",
      "incorrect_answers": [
        "Joey Potter",
        "Frank Potter",
        "Hairy Potter Sr."
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of these book series is by James Patterson?",
      "correct_answer": "Maximum Ride",
      "incorrect_answers": [
        "Harry Potter",
        "The Legend of Xanth",
        "The Bartemaeus Trilogy"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "easy",
      "question": "Which is NOT a book in the Harry Potter Series?",
      "correct_answer": "The House Elf",
      "incorrect_answers": [
        "The Chamber of Secrets",
        "The Prisoner of Azkaban",
        "The Deathly Hallows"
      ]
    },
    {
      "category": "Entertainment: Books",
      "type": "multiple",
      "difficulty": "hard",
      "question": "In The Lies Of Locke Lamora, what does &quot;Lamora&quot; mean in Throne Therin?",
      "correct_answer": "Shadow",
      "incorrect_answers": [
        "Thievery",
        "Justice",
        "Chaos"
      ]
    }
  ]
print("Hello, welcome to the book quiz. Answer the questions as they are presented.")
for question in results:
    print(f"{question}")
userInput = input()
