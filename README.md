# Duplicate Email Detection

## Problem
Given a file containing **100 million email addresses**, some emails may appear multiple times.  
The goal is to efficiently identify all duplicate email addresses.

---

## Algorithm

1. Read the file **line by line** so we don’t load all 100 million emails into memory at once, keeps RAM usage low.
2. Create a **set called `seen`** to store emails that have already been encountered.
3. Create another **set called `duplicates`** to store emails that appear more than once.
4. For each email in the file:
   - If the email is **not in `seen`**, add it to `seen`.
   - If the email **already exists in `seen`**, add it to `duplicates`.
5. Continue this process until the entire file has been processed.
6. At the end, the `duplicates` set contains all email addresses that appeared more than once.

---

## Data Structures Used

### Hash Set (`seen`)
- Stores emails that have already been processed.
- Enables **O(1) average lookup time**.

### Hash Set (`duplicates`)
- Stores emails that occur more than once.
- Prevents storing the same duplicate multiple times.

---

## Complexity Analysis

**Time Complexity:**  
`O(N)`  
Each email is processed exactly once.

**Space Complexity:**  
`O(N)` in the worst case if all emails are unique and must be stored in memory.
