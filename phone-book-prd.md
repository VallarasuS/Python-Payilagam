# Phone Book

## Functional Requirements

- **Add contact**
	- Name and phone are required
	- Phone can contain only digits, spaces, -, +, (, )
	- No duplicate names allowed (case-insensitive)
	- class init, validation, set / list append
- **List all contacts**
	- Shows numbered list or clean table
	- Columns: #, Name, Phone (optionally Email)
	- formatting, loops, enumerate, string alignment
- **Search by name**
 	- Case-insensitive partial match
	- Returns all matching contacts
	- list comprehension, str.lower(), any()/filter()
- **Delete contact**
	- Can delete by exact name or by number shown in list
    - remove from list/dict, index handling