Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <last_name>, <address>, <mobile_phone> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name | last_name | address         | mobile_phone |  email          |
  | Andreas    | Mochinos  | 154 Gloria blvd | 204-571-0118 | correo@mail.kom |
  | Benito     | Carleone  | 11 Fake lane    | 464-181-6843 | becarl@mail.kom |


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given new contact data <first_name>, <last_name>, <address>, <mobile_phone> and <email>
  When I modify the contact with new data
  Then the new contact list is equal to the old list with the modified contact

  Examples:
  | first_name | last_name | address         | mobile_phone |  email          |
  | Nico       | Sander    | 154 Gloria road | 300-571-0118 | kolia@mail.kom  |
  | Nadezhda   | Babkina   | Borvikha, 5     | 7(904)111111 | becarl@mail.kom |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact