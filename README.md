# 🛒 Shopping Basket Pricer – Web Application

A supermarket basket-pricing web application that allows users to add and remove products, apply offers, and calculate **subtotals, discounts, and totals** in real time.

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

👉 **Live app:**  
https://shopping-basket-87c673649f49.herokuapp.com/

Simply open the link in a browser to explore the functionality.

---

## 📌 Notes

- Pricing rules and offers are **data-driven** and not hard-coded.
- The basket-pricing logic is designed to be reusable and easily testable.
- Focus is placed on correctness, fairness of discounts, and clean separation of concerns.
