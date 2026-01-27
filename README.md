# 🛒 Shopping Basket Pricer – Web Application

A supermarket basket-pricing web application that allows users to add and remove products, apply offers, and calculate **subtotals, discounts, and totals** in real time.

<img width="478" height="244" alt="image" src="https://github.com/user-attachments/assets/2567a8f6-304b-4d09-bada-9a259fa90e13" />
<img width="478" height="244" alt="image" src="https://github.com/user-attachments/assets/b688e7df-8a44-4737-a9ae-b88f2b7bc356" />


**TRY FOR YOURSELF:** https://shopping-basket-87c673649f49.herokuapp.com/

---

## ✨ Features

- **Backend:** Python, Flask  
- **Frontend:** JavaScript, Jinja2, HTML, CSS  
- **Database:** NoSQL (MongoDB)  
- **UI/UX:** Bootstrap-based, responsive, user-friendly interface  

### Core Functionality
- User shopping baskets (add / remove items)
- Dynamic calculation of:
  - Sub-total  
  - Discounts  
  - Final total  
- Support for multiple and overlapping offers
- Accurate pricing to two decimal places

---

## 🧠 Design Rationale

I chose to implement this solution as a **full web application** rather than a CLI or desktop-based app for the following reasons:

- The job specification emphasised **Python and JavaScript** with ~3 years of experience, so this approach best demonstrates proficiency in the required stack.
- A web-based solution better reflects **real-world usage**, such as online shopping platforms or in-store systems.
- A polished, interactive website provides a more **refined and portfolio-ready project** compared to a simple CLI or Tkinter application.
- It highlights full-stack skills, including backend logic, frontend rendering, database interaction, and user experience design.

---

## 🚀 Tech Stack Summary

| Layer    | Technology          |
|---------|---------------------|
| Backend | Flask (Python)      |
| Frontend| JavaScript, Jinja2  |
| Styling | HTML, CSS, Bootstrap|
| Database| MongoDB (NoSQL)     |

---

## 🌐 Live Deployment

This application is deployed via **Salesforce Heroku**, so no local installation or setup is required.

## 🗒️ TEST CASES

NOTE: Outputs maybe off by a slight degree due to rounding!

TEST 1
Expected
<img width="268" height="161" alt="image" src="https://github.com/user-attachments/assets/e78f440b-fb2c-4b74-89ef-d7bace5b2a42" />

RESULT
<img width="977" height="576" alt="image" src="https://github.com/user-attachments/assets/59770e02-2710-4d68-a450-37ec1b6fd2de" />

TEST 2
EXPECTED
<img width="230" height="102" alt="image" src="https://github.com/user-attachments/assets/901dca46-b34c-465e-9fec-dbb149330de0" />

RESULT
<img width="988" height="569" alt="image" src="https://github.com/user-attachments/assets/74077b10-c4cb-4c9c-9854-159f179bbe25" />

TEST 3
EXPECTED
<img width="176" height="145" alt="image" src="https://github.com/user-attachments/assets/48004ae9-6153-42fe-9a68-9f3315c93c22" />

RESULT
<img width="998" height="572" alt="image" src="https://github.com/user-attachments/assets/52a5a46f-f178-46f3-8b16-a861ce779065" />


All Test cases passed! (3 / 3)

---

## 📌 Notes

- Pricing rules and offers are **data-driven** and not hard-coded.
- The basket-pricing logic is designed to be reusable and easily testable.
- Focus is placed on correctness, fairness of discounts, and clean separation of concerns.
