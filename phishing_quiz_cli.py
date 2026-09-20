"""
Phishing Awareness Training - Python CLI Quiz
----------------------------------------------
Interactive console quiz testing knowledge on phishing red flags,
social engineering tactics, and cyber defense best practices.
"""

import time

QUESTIONS = [
    {
        "scenario": "You receive an email from 'it-support@sec-mycompany.com' with the subject 'URGENT: Password expiring in 1 hour. Click link to retain password.'",
        "question": "What is the primary red flag in this scenario?",
        "options": [
            "A) The email was sent on a weekday.",
            "B) Artificial urgency and an external/spoofed sender domain.",
            "C) The email mentions passwords.",
            "D) The font size is normal."
        ],
        "answer": "B",
        "explanation": "Attackers induce panic with tight deadlines and use spoofed lookalike domains."
    },
    {
        "scenario": "You visit a login page with the URL: 'https://login.microsoft.com.account-auth.ru/login'.",
        "question": "Is this a legitimate Microsoft login page?",
        "options": [
            "A) Yes, because it starts with 'login.microsoft.com'.",
            "B) Yes, because it uses HTTPS.",
            "C) No, the actual root domain is 'account-auth.ru'.",
            "D) Yes, all .ru sites are verified."
        ],
        "answer": "C",
        "explanation": "The root domain right before the top-level domain determines the real host. Here, it is 'account-auth.ru'."
    },
    {
        "scenario": "An employee receives a message from someone claiming to be the CEO asking for an urgent \$25,000 vendor wire transfer while in a meeting.",
        "question": "What type of social engineering attack is this?",
        "options": [
            "A) Ransomware",
            "B) Business Email Compromise (BEC) / CEO Fraud",
            "C) Distributed Denial of Service (DDoS)",
            "D) SQL Injection"
        ],
        "answer": "B",
        "explanation": "BEC / CEO fraud exploits authority to bypass standard accounting protocols."
    },
    {
        "scenario": "An attacker sends an SMS text message claiming you won a lottery and asks you to tap a link.",
        "question": "What is the specific term for phishing carried out via SMS?",
        "options": [
            "A) Smishing",
            "B) Vishing",
            "C) Pharming",
            "D) Whaling"
        ],
        "answer": "A",
        "explanation": "Phishing over SMS is known as Smishing; voice phishing over phone is Vishing."
    },
    {
        "scenario": "You want to protect your accounts against credential theft even if you accidentally enter your password on a phishing page.",
        "question": "Which security measure provides the strongest defense against stolen passwords?",
        "options": [
            "A) Multi-Factor Authentication (MFA / 2FA)",
            "B) Clearing browser cookies",
            "C) Changing desktop wallpaper",
            "D) Restarting your router"
        ],
        "answer": "A",
        "explanation": "MFA prevents unauthorized logins even if the attacker has captured the password."
    }
]

def run_quiz():
    print("=" * 60)
    print("      🛡️ PHISHING AWARENESS & DEFENSE INTERACTIVE QUIZ 🛡️")
    print("=" * 60)
    print("Answer each question by entering A, B, C, or D.\n")

    score = 0

    for i, q in enumerate(QUESTIONS, 1):
        print(f"Scenario {i}: {q['scenario']}")
        print(f"Question: {q['question']}\n")
        for opt in q['options']:
            print(f"  {opt}")

        while True:
            choice = input("\nYour answer (A/B/C/D): ").strip().upper()
            if choice in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if choice == q["answer"]:
            print("  [✓] CORRECT!")
            score += 1
        else:
            print(f"  [✗] INCORRECT! Correct answer was ({q['answer']}).")
        
        print(f"  💡 Explanation: {q['explanation']}\n")
        print("-" * 60)
        time.sleep(0.5)

    print("\n" + "=" * 60)
    print("                     QUIZ RESULTS")
    print("=" * 60)
    percentage = (score / len(QUESTIONS)) * 100
    print(f"Final Score: {score} / {len(QUESTIONS)} ({percentage:.1f}%)")
    
    if score == len(QUESTIONS):
        print("Rating: 🌟 Master of Cyber Defense! Excellent awareness.")
    elif score >= 3:
        print("Rating: 👍 Good awareness! Keep practicing identifying subtle red flags.")
    else:
        print("Rating: ⚠️ Needs Improvement. Review the training module slides.")
    print("=" * 60)

if __name__ == "__main__":
    run_quiz()
