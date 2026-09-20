# Phishing Awareness Training — Presentation Slide Deck

**Target Audience:** Employees, Students, and Cybersecurity Beginners  
**Format:** Presentation Deck / Slide Outline with Speaker Notes

---

## Slide 1: Title Slide
- **Slide Title:** Phishing Awareness & Social Engineering Defense
- **Subtitle:** Recognizing Threats, Identifying Red Flags, and Protecting Digital Assets
- **Presenter:** Cyber Security Intern / Analyst
- **Speaker Notes:** "Welcome everyone. Today we are discussing one of the most critical cybersecurity topics—Phishing. Despite multimillion-dollar firewalls, over 90% of successful corporate breaches start with a single human clicking a malicious link."

---

## Slide 2: What is Phishing?
- **Definition:** A social engineering attack where malicious actors deceive individuals into revealing confidential information (passwords, banking details, session tokens) or downloading malware.
- **Key Vectors:**
  - **Email Phishing:** Bulk fraudulent emails.
  - **Spear Phishing:** Customized attacks targeted at a specific individual or team.
  - **Whaling:** Targeted at C-level executives (CEOs, CFOs) for high-value financial fraud.
  - **Smishing (SMS) & Vishing (Voice Calls):** Deception via text messages and phone scams.
- **Speaker Notes:** "Phishing is not just a spam email; it has evolved into sophisticated, targeted campaigns utilizing artificial intelligence and detailed reconnaissance."

---

## Slide 3: Anatomy of a Phishing Email (Spotting Red Flags)
- **1. Sender Address Mismatch:** Display name says "Microsoft Support", but the email header is `@sec-support-mail.net`.
- **2. Sense of Artificial Urgency:** "Action required within 24 hours or your account will be deleted."
- **3. Generic Greetings:** "Dear Customer" or "Dear Employee" rather than your real name.
- **4. Suspicious Attachments:** Files named `Invoice_Report.pdf.exe` or macro-enabled Excel sheets.
- **5. Mismatched Hyperlinks:** Display text points to a legitimate bank, but the actual hover URL points to an attacker's server.
- **Speaker Notes:** "Always hover before you click. Check the domain spelling after the @ sign, and remember that real IT teams do not give 2-hour ultimatums."

---

## Slide 4: Recognizing Fake Websites & URL Spoofing
- **Typosquatting:** Subtle misspellings (e.g., `micros0ft.com`, `paypa1.com`).
- **Subdomain Manipulation:** `www.bankofamerica.com.attacker-controlled-site.com` (The true domain is the last part before the top-level domain).
- **The HTTPS Myth:** A padlock 🔒 only guarantees encrypted communication, not that the website owner is legitimate. Over 80% of phishing sites now use free SSL/TLS certificates.
- **Speaker Notes:** "Never trust a website solely because of a green padlock. Examine the root domain directly before `.com` or `.org`."

---

## Slide 5: Psychological Weapons in Social Engineering
Attackers exploit human emotions rather than software flaws:
1. **Fear / Coercion:** "Legal action will be taken if tax fines are not settled immediately."
2. **Authority:** "I am the CEO, currently in a confidential meeting. Wire \$50,000 to this vendor ASAP." (Business Email Compromise).
3. **Curiosity / Greed:** "Exclusive holiday bonus list attached."
4. **Helpfulness / Trust:** Impersonating a new coworker requesting access credentials.
- **Speaker Notes:** "When you feel rushed, fearful, or excited by an email, pause. That emotional spike is the attacker's primary weapon."

---

## Slide 6: Real-World Case Studies
- **FACC CEO Fraud (Whaling - $50M loss):** Attackers impersonated the CEO via spoofed email requesting an urgent wire transfer for an acquisition.
- **Google & Facebook Vendor Scam ($100M BEC):** A scammer forged invoices from a real hardware supplier (Quanta Computer) and received over $100M in payouts before being detected.
- **Key Takeaway:** Financial approvals and credential requests should always require secondary, out-of-band verification (e.g., phone call or in-person check).

---

## Slide 7: Best Practices & Defensive Playbook
1. **The S.L.I.M. Rule:** Inspect **S**ender, **L**inks, **I**nformation requested, and **M**otivation.
2. **Multi-Factor Authentication (MFA):** Enforce hardware tokens (FIDO2) or authenticator apps.
3. **Password Managers:** Automatically refuse to autofill passwords on spoofed/fake domains.
4. **Out-of-Band Verification:** Call the sender on a known, verified phone number if money or credentials are requested.
5. **Immediate Incident Reporting:** Flag and report suspicious emails to the SOC / IT Security team immediately.

---

## Slide 8: Interactive Q&A and Conclusion
- **Summary:** Security is a collective responsibility. Stop, Think, and Verify.
- **Action Item:** Practice identifying phishing using our interactive web module.
